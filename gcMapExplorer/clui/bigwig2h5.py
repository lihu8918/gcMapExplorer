#!/usr/bin/env python3
#
# Author: Rajendra Kumar
#
# This file is part of gcMapExplorer
# Copyright (C) 2016  Rajendra Kumar, Ludvig Lizana, Per Stenberg
#
# gcMapExplorer is a free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# gcMapExplorer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gcMapExplorer.  If not, see <http://www.gnu.org/licenses/>.
#
#=============================================================================

import os
import sys
import re
import argparse

import gcMapExplorer.lib as gmlib

from gcMapExplorer.config import getConfig

# get configuration
config = getConfig()

description = \
"""Import a bigWig file to HDF5 format h5 file
============================================

bigWig file can be converted into gcMapExplorer compaitable HDF5 file using
this tool. This HDF5 file can be loaded into gcMapExplorer browser for
interactive visualization.

Requirements
============
1) bigWigToWig : It converts binary bigWig file to ascii Wig file.
2) bigWigInfo : It fetches the information about chromosomes from bigWig file.

Both tools can be downloaded from http://hgdownload.cse.ucsc.edu/admin/exe/
for linux and Mac platform. However, these tools are not yet available for
Windows OS.

Path to these tools can be set using gcMapExplorer configure utility or can be
given with the command.

Resolutions
===========
By default, original data are downsampled to following resolutions:  '1kb',
'2kb', '4kb', '5kb', '8kb', '10kb', '20kb', '40kb', '80kb', '100kb', '160kb',
'200kb', '320kb', '500kb', '640kb',  and '1mb'. The output file HDF5 contains
original data including all the above resolutions.

The data are downsampled at this stage only to speed up the visualization
process as downsampling might slow down the interactive visualization.
"""

inputFileHelp = \
"""Input bigWig file.

"""

bigWigToWigHelp = \
"""Path to bigWigToWig tool.

This is not neccessary when bigWigToWig path is already set using gcMapExplorer
configure utility.

It can be downloaded from http://hgdownload.cse.ucsc.edu/admin/exe/
for linux and Mac platform.

"""

bigWigInfoHelp = \
""" Path to bigWigInfo tool.

This is not neccessary when bigWigInfo path is already set using gcMapExplorer
configure utility.

It can be downloaded from http://hgdownload.cse.ucsc.edu/admin/exe/
for linux and Mac platform.

"""

resolutionHelp = \
"""Additional input resolutions other than these resolutions: 1kb', '2kb',
'4kb', '5kb', '8kb', '10kb', '20kb', '40kb', '80kb', '100kb', '160kb','200kb',
'320kb', '500kb', '640kb',  and '1mb'.

Resolutions should be provided in comma seprated values. For Example:
-r "25kb, 50kb, 75kb"

"""

outHelp = \
"""Output h5 file.

If file is already present, it will replace the data. Therefore, be careful
if a file with same name is present.

"""

overwriteHelp = \
"""If a output file is already present, overwrite the datasets in the output
file.

"""

def main():
    # Construct command line arguments and parsed it
    parser, args = parseArguments()

    # Check for bigWigToWig program
    bigWigToWig = args.bigWigToWig
    if bigWigToWig == 'None':
        showErrorAndExit(parser, '\nPath to bigWigToWig not provided!!!\n')
    checkFileExist(bigWigToWig, parser)

    # Check for bigWigInfo program
    bigWigInfo = args.bigWigInfo
    if bigWigInfo == 'None':
        showErrorAndExit(parser, '\nPath to bigWigInfo not provided!!!\n')
    checkFileExist(bigWigInfo, parser)

    # Check for input bigWig File
    inputBigWigFile = args.inputBigWigFile.name
    if inputBigWigFile is None:
        showErrorAndExit(parser, '\nInput bigWig file is not given!!!\n')
    args.inputBigWigFile.close()

    # Check for additional resolutions
    resolution = args.resolution
    if resolution is not None:
        resolution = get_resolution_list(resolution, parser)

    # Check for output file
    outFile = args.h5Name
    if outFile is not None:
        check_overwrite_status(outFile, args.overwrite, parser)
    else:
        showErrorAndExit(parser, '\nNo output file!!!\n')

    # Check for scratch directory
    if not os.path.isdir(args.workDir):
        showErrorAndExit(parser, '\nScratch Dirctory "{0}" not found !!!\n'.format(args.workDir))

    # Main conversion start here
    bigwig = gmlib.genomicsDataHandler.BigWigHandler(inputBigWigFile, bigWigToWig, bigWigInfo, resolutions=resolution, workDir=args.workDir)
    bigwig.saveToH5(outFile, title=args.title, compression=args.compression)
    del bigwig

def get_resolution_list(resolution, parser):
    rlist = []
    temp = re.split(',', resolution)
    for r in temp:
        r = r.rstrip().lstrip()
        if not r.strip():
            continue
        try:
            b = gmlib.ccmap.resolutionToBinsize(r)
        except ValueError:
            showErrorAndExit(parser, '\n"{0}" contains resolution "{1}", which is not an acceptable resolution.\n'.format(resolution, r))

        rlist.append(r)

    return rlist

def check_overwrite_status(outFile, overwrite, parser):

    # Nothing to do if overwrite
    if overwrite:
        return

    # Else do check other stuffs
    if os.path.isfile(outFile):
        print('\nWARNING: Output File "{0}" already exist.!!!'.format(outFile))

        s = input('\n Are you sure to overwrite datasets [y/n] (default: n): ')
        while(True):
            if not s:
                s = 'n'
                break

            s = s.lstrip().rstrip()

            if s != 'n' and s != 'y':
                s = input('\n Are you sure to overwrite datasets [y/n] (default: n): ')
            else:
                break

        if str(s) == 'n':
            showErrorAndExit(parser, '\nPlease provide another output file name.\n')

def parseArguments():
    parser = argparse.ArgumentParser(
                prog='gcMapExplorer bigwig2h5',
                description=description,
                formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('-i', '--input', action='store',
                        type=argparse.FileType('rb'), metavar='input.bigWig',
                        dest='inputBigWigFile', help=inputFileHelp)

    parser.add_argument('-t', '--title', action='store',
                        dest='title', metavar='"Genomic Dataset"',
                        default='"Genomic Dataset"',
                        help='Title of the dataset.\n')

    parser.add_argument('-b2w', '--bigWigToWig', action='store',
                        type=str, metavar='bigWigToWig',
                        default=config['Programs']['bigWigToWig'],
                        dest='bigWigToWig', help=bigWigToWigHelp)

    parser.add_argument('-binfo', '--bigWigInfo', action='store', type=str,
                        metavar='bigWigInfo', dest='bigWigInfo',
                        default=config['Programs']['bigWigInfo'],
                        help=bigWigInfoHelp)

    parser.add_argument('-r', '--resolution', action='store', type=str,
                        metavar='"List of Resolutions"', dest='resolution',
                        help=resolutionHelp)

    parser.add_argument('-cmeth', '--compression-method', action='store',
                        dest='compression', metavar='lzf',
                        choices=['lzf', 'gzip'], default='lzf',
                        help='Data compression method for gcmap file.\n')

    parser.add_argument('-o', '--out', action='store', dest='h5Name',
                        metavar='out.h5', help=outHelp)

    parser.add_argument('-ow', '--overwrite', action='store_true',
                        dest='overwrite', help=overwriteHelp)

    parser.add_argument('-wd', '--work-dir', action='store', dest='workDir',
                        default=config['Dirs']['WorkingDirectory'],
                        metavar=config['Dirs']['WorkingDirectory'],
                        help='Directory where temporary files will be stored.')

    idx = sys.argv.index("bigwig2h5")+1
    args = parser.parse_args(args=sys.argv[idx:])

    return parser, args

def checkFileExist(filename, parser):
    if not os.path.isfile(filename):
        parser.print_help()
        print("\n===== ERROR =======")
        print("File: {0} does not exist !!!\n".format(filename))
        print("See Usage Above!!!")
        sys.exit(-1)

def showErrorAndExit(parser, message):
    parser.print_help()
    print("\n===== ERROR =======")
    print(message)
    print("See Usage Above!!!")
    sys.exit(-1)


if __name__ == "__main__":
    main()