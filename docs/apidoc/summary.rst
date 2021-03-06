.. |json link| raw:: html

    <a href="https://docs.python.org/3/library/json.html" target="_blank">json module</a>



.. |markov chain link| raw:: html

    <a href="https://en.wikipedia.org/wiki/Markov_chain#Example" target="_blank">Markov-chain example</a>




Summary of Python Modules
-------------------------

.. currentmodule:: gcMapExplorer.config

config module
~~~~~~~~~~~~~
.. autosummary::
    updateConfig
    getConfig
    printConfig
    cleanScratch

.. currentmodule:: gcMapExplorer.lib

ccmap module
~~~~~~~~~~~~
.. autosummary::
    ccmap.CCMAP.copy
    ccmap.CCMAP.get_ticks
    ccmap.CCMAP.make_readable
    ccmap.CCMAP.make_unreadable
    ccmap.CCMAP.make_writable
    ccmap.CCMAP.make_editable
    ccmap.jsonify
    ccmap.dejsonify
    ccmap.save_ccmap
    ccmap.load_ccmap
    ccmap.export_cmap
    ccmap.checkCCMapObjectOrFile
    ccmap.downSampleCCMap
    ccmap.getOutputShapeFor2DMapDownsampling
    ccmap.downSample2DMap


ccmapHelpers module
~~~~~~~~~~~~~~~~~~~~
.. autosummary::
    ccmapHelpers.MemoryMappedArray
    ccmapHelpers.MemoryMappedArray.copy
    ccmapHelpers.MemoryMappedArray.copy_from
    ccmapHelpers.MemoryMappedArray.copy_to
    ccmapHelpers.get_nonzeros_index
    ccmapHelpers.remove_zeros


util module
~~~~~~~~~~~
.. autosummary::
    util.resolutionToBinsize
    util.binsizeToResolution
    util.sorted_nicely
    util.locate_significant_digit_after_decimal
    util.kth_diag_indices
    util.detectOutliers1D
    util.getRandomName
    util.MapNotFoundError
    util.ResolutionNotFoundError


gcmap module
~~~~~~~~~~~~
.. autosummary::
    gcmap.GCMAP
    gcmap.GCMAP.checkMapExist
    gcmap.GCMAP.changeMap
    gcmap.GCMAP.changeResolution
    gcmap.GCMAP.toFinerResolution
    gcmap.GCMAP.toCoarserResolution
    gcmap.GCMAP.loadSmallestMap
    gcmap.GCMAP.genMapNameList
    gcmap.GCMAP.performDownSampling
    gcmap.GCMAP.downsampleMapToResolution
    gcmap.GCMAP.downsampleAllMapToResolution
    gcmap.loadGCMapAsCCMap
    gcmap.addCCMap2GCMap
    gcmap.changeGCMapCompression


importer module
~~~~~~~~~~~~~~~
.. autosummary::
    importer.CooMatrixHandler
    importer.CooMatrixHandler.save_ccmaps
    importer.CooMatrixHandler.save_gcmap
    importer.CooMatrixHandler.setLabels
    importer.CooMatrixHandler.setOutputFileList
    importer.PairCooMatrixHandler
    importer.PairCooMatrixHandler.setGCMapOptions
    importer.PairCooMatrixHandler.runConversion
    importer.HomerInputHandler
    importer.HomerInputHandler.save_ccmaps
    importer.HomerInputHandler.save_gcmap
    importer.BinsNContactFilesHandler
    importer.BinsNContactFilesHandler.save_ccmaps
    importer.BinsNContactFilesHandler.save_gcmap
    importer.gen_map_from_locations_value


normalizer module
~~~~~~~~~~~~~~~~~
.. autosummary::
    normalizer.NormalizeKnightRuizOriginal
    normalizer.normalizeCCMapByKR
    normalizer.normalizeGCMapByKR
    normalizer.normalizeCCMapByIC
    normalizer.normalizeGCMapByIC
    normalizer.normalizeCCMapByMCFS
    normalizer.normalizeGCMapByMCFS
    normalizer.normalizeCCMapByVCNorm
    normalizer.normalizeGCMapByVCNorm


cmstats module
~~~~~~~~~~~~~~~~~
.. autosummary::
    cmstats.correlateCMaps
    cmstats.correlateGCMaps
    cmstats.getAvgContactByDistance


corrMatrix module
~~~~~~~~~~~~~~~~~
.. autosummary::
    corrMatrix.calculateCorrMatrix
    corrMatrix.calculateCovMatrix
    corrMatrix.calculateCorrelation
    corrMatrix.calculateCovariance
    corrMatrix.calculateCorrMatrixForCCMap
    corrMatrix.calculateCorrMatrixForGCMaps


statDist module
~~~~~~~~~~~~~~~
.. autosummary::
    statDist.calculateTransitionProbabilityMatrix
    statDist.transitionProbabilityMatrixForCCMap
    statDist.transitionProbabilityMatrixForGCMap
    statDist.statDistrByEigenDecompForCCMap
    statDist.statDistrByEigenDecompForGCMap
    statDist.stationaryDistributionByEigenDecomp


genomicsDataHandler module
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
    genomicsDataHandler.HDF5Handler
    genomicsDataHandler.HDF5Handler.setTitle
    genomicsDataHandler.HDF5Handler.getChromList
    genomicsDataHandler.HDF5Handler.getResolutionList
    genomicsDataHandler.HDF5Handler.getDataNameList
    genomicsDataHandler.HDF5Handler.buildDataTree
    genomicsDataHandler.BigWigHandler
    genomicsDataHandler.BigWigHandler.getBigWigInfo
    genomicsDataHandler.BigWigHandler.bigWigtoWig
    genomicsDataHandler.BigWigHandler.saveAsH5
    genomicsDataHandler.WigHandler
    genomicsDataHandler.WigHandler.parseWig
    genomicsDataHandler.WigHandler.setChromosome
    genomicsDataHandler.WigHandler.saveAsH5
    genomicsDataHandler.WigHandler.getRawWigDataAsDictionary
    genomicsDataHandler.BEDHandler
    genomicsDataHandler.BEDHandler.parseBed
    genomicsDataHandler.BEDHandler.setChromosome
    genomicsDataHandler.BEDHandler.saveAsH5
    genomicsDataHandler.EncodeDatasetsConverter
    genomicsDataHandler.EncodeDatasetsConverter.saveAsH5
    genomicsDataHandler.TextFileHandler
    genomicsDataHandler.TextFileHandler.readData
    genomicsDataHandler.TempNumpyArrayFiles
    genomicsDataHandler.TempNumpyArrayFiles.updateArraysByBigWig
    genomicsDataHandler.TempNumpyArrayFiles.updateArraysByChromSize
    genomicsDataHandler.TempNumpyArrayFiles.addChromSizeInfo
    genomicsDataHandler.TempNumpyArrayFiles.generateAllTempNumpyFiles
    genomicsDataHandler.TempNumpyArrayFiles.generateTempNumpyFile
    genomicsDataHandler.TempNumpyArrayFiles.fillAllArraysWithZeros
