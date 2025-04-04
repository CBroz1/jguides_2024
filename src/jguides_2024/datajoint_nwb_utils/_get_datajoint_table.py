def _get_table(table_name):
    # Avoid circular import
    import os

    os.chdir("/home/jguidera/Src/jguides_2024")
    from src.jguides_2024.edeno_decoder.jguidera_edeno_decoder_error import (
        EdenoDecodeErr,
        EdenoDecodeErrParams,
        EdenoDecodeErrSel,
        EdenoDecodeErrSumm,
        EdenoDecodeErrSummBinParams,
        EdenoDecodeErrSummParams,
        EdenoDecodeErrSummSel,
    )
    from src.jguides_2024.edeno_decoder.jguidera_edeno_decoder_helpers import (
        EDPathGroups,
        StackedEdgeTrackGraph,
        TrackGraphSourceSortedSpikesClassifierParams,
    )
    from src.jguides_2024.edeno_decoder.jguidera_edeno_decoder_run import (
        EDAlgorithmParams,
        EDComputeParams,
        EDCrossValidationParams,
        EDDecodeVariableParams,
        EdenoDecode,
        EdenoDecodeMAP,
        EdenoDecodeMAPSel,
        EdenoDecodeParams,
        EdenoDecodeSel,
        EDStorageParams,
    )
    from src.jguides_2024.firing_rate_map.jguidera_ppt_firing_rate_map import (
        CorrFrmapPptSm,
        FrmapPpt,
        FrmapPptSel,
        FrmapPptSm,
        FrmapPptSmParams,
        FrmapPupt,
        FrmapPuptSm,
        OverlapFrmapPptSm,
        STFrmapPupt,
        STFrmapPuptSm,
    )
    from src.jguides_2024.firing_rate_map.jguidera_well_arrival_departure_firing_rate_map import (
        FrmapWADParams,
        FrmapWADSmParams,
        FrmapWADSmWT,
        FrmapWADSmWTParams,
        STFrmapWAD,
        STFrmapWADSm,
        STFrmapWADSmWT,
        STFrmapWADSmWTSel,
    )
    from src.jguides_2024.firing_rate_map.jguidera_well_arrival_firing_rate_map import (
        FrmapUniqueWellArrival,
        FrmapUniqueWellArrivalSm,
        FrmapWellArrival,
        FrmapWellArrivalParams,
        FrmapWellArrivalSel,
        FrmapWellArrivalSm,
        FrmapWellArrivalSmParams,
        STFrmapWellArrival,
        STFrmapWellArrivalSm,
    )
    from src.jguides_2024.firing_rate_vector.jguidera_firing_rate_difference_vector import (
        FRDiffVec,
        FRDiffVecParams,
        FRDiffVecSel,
    )
    from src.jguides_2024.firing_rate_vector.jguidera_firing_rate_difference_vector_similarity import (
        FRDiffVecCosSim,
        FRDiffVecCosSimSel,
    )
    from src.jguides_2024.firing_rate_vector.jguidera_firing_rate_difference_vector_similarity_ave import (
        FRDiffVecCosSimPptNnAve,
        FRDiffVecCosSimPptNnAveParams,
        FRDiffVecCosSimPptNnAveSel,
        FRDiffVecCosSimPptNnAveSumm,
        FRDiffVecCosSimPptNnAveSummParams,
        FRDiffVecCosSimPptNnAveSummSel,
        FRDiffVecCosSimWANnAve,
        FRDiffVecCosSimWANnAveParams,
        FRDiffVecCosSimWANnAveSel,
        FRDiffVecCosSimWANnAveSumm,
        FRDiffVecCosSimWANnAveSummParams,
        FRDiffVecCosSimWANnAveSummSel,
    )
    from src.jguides_2024.firing_rate_vector.jguidera_firing_rate_vector import (
        FRVec,
        FRVecSel,
    )
    from src.jguides_2024.firing_rate_vector.jguidera_firing_rate_vector_embedding import (
        FRVecEmb,
        FRVecEmbParams,
        FRVecEmbSel,
    )
    from src.jguides_2024.firing_rate_vector.jguidera_firing_rate_vector_euclidean_distance import (
        FRVecEucDist,
        FRVecEucDistSel,
    )
    from src.jguides_2024.firing_rate_vector.jguidera_path_firing_rate_vector import (
        PathAveFRVec,
        PathAveFRVecParams,
        PathAveFRVecSel,
        PathAveFRVecSumm,
        PathAveFRVecSummParams,
        PathAveFRVecSummSel,
        PathFRVec,
        PathFRVecParams,
        PathFRVecSel,
        PathFRVecSTAve,
        PathFRVecSTAveParams,
        PathFRVecSTAveSel,
        PathFRVecSTAveSumm,
        PathFRVecSTAveSummParams,
        PathFRVecSTAveSummSel,
    )
    from src.jguides_2024.firing_rate_vector.jguidera_well_event_firing_rate_vector import (
        TimeRelWAAveFRVec,
        TimeRelWAAveFRVecParams,
        TimeRelWAAveFRVecSel,
        TimeRelWAAveFRVecSumm,
        TimeRelWAAveFRVecSummParams,
        TimeRelWAAveFRVecSummSel,
        TimeRelWAFRVec,
        TimeRelWAFRVecParams,
        TimeRelWAFRVecSel,
        TimeRelWAFRVecSTAve,
        TimeRelWAFRVecSTAveParams,
        TimeRelWAFRVecSTAveSel,
        TimeRelWAFRVecSTAveSumm,
        TimeRelWAFRVecSTAveSummParams,
        TimeRelWAFRVecSTAveSummSel,
    )
    from src.jguides_2024.glm.jguidera_basis_function import (
        RaisedCosineBasis,
        RaisedCosineBasisParams,
    )
    from src.jguides_2024.glm.jguidera_el_net import (
        ElNet,
        ElNetParams,
        ElNetSel,
    )
    from src.jguides_2024.glm.jguidera_measurements_interp_pool import (
        Intercept,
        InterceptSel,
        XInterpPool,
        XInterpPoolCohort,
        XInterpPoolCohortEpsCohort,
        XInterpPoolCohortEpsCohortParams,
        XInterpPoolCohortParamName,
        XInterpPoolCohortParams,
        XInterpPoolSel,
    )
    from src.jguides_2024.metadata.jguidera_brain_region import (
        BrainRegionCohort,
        BrainRegionColor,
        BrainRegionSortGroup,
        BrainRegionSortGroupParams,
        CurationSet,
        CurationSetSel,
        ElectrodeGroupTargetedLocation,
        SortGroupTargetedLocation,
    )
    from src.jguides_2024.metadata.jguidera_epoch import (
        DistinctRunEpochPair,
        EpochArtifactFree,
        EpochCohort,
        EpochCohortParams,
        EpochFullLen,
        EpochsDescription,
        EpochsDescriptions,
        HomeEpoch,
        RecordingSet,
        RunEpoch,
        RunEpochPair,
        SleepEpoch,
        TrainTestEpoch,
        TrainTestEpochSet,
    )
    from src.jguides_2024.metadata.jguidera_histology import ValidShank
    from src.jguides_2024.metadata.jguidera_metadata import (
        JguideraNwbfile,
        JguideraNwbfileSel,
        TaskIdentification,
    )
    from src.jguides_2024.metadata.jguidera_premaze_durations import (
        PremazeDurations,
    )
    from src.jguides_2024.position_and_maze.jguidera_maze import (
        AnnotatedTrackGraph,
        AnnotatedUniversalTrackGraph,
        EnvironmentColor,
        ForkMazePathEdges,
        ForkMazePathEdgesSel,
        ForkMazeRewardWellPathPair,
        ForkMazeRewardWellPathPairSel,
        MazeEdgeType,
        RewardWell,
        RewardWellColor,
        RewardWellPath,
        RewardWellPathColor,
        RewardWellPathTurnDirection,
        RewardWellPathTurnDirectionParams,
        TrackGraphAnnotations,
        TrackGraphUniversalTrackGraphMap,
        TrackGraphUniversalTrackGraphMapParams,
        UniversalForkMazePathEdgePathFractionMap,
        UniversalTrackGraphAnnotations,
        UniversalTrackGraphPosBinEdges,
        UniversalTrackGraphPosBinEdgesParams,
    )
    from src.jguides_2024.position_and_maze.jguidera_position import (
        IntervalLinearizedPositionRelabel,
        IntervalLinearizedPositionRelabelParams,
        IntervalLinearizedPositionRescaled,
        IntervalPositionInfoRelabel,
        IntervalPositionInfoRelabelParams,
    )
    from src.jguides_2024.position_and_maze.jguidera_ppt import (
        Ppt,
        PptBinEdges,
        PptBinEdgesParams,
        PptParams,
        PptSel,
    )
    from src.jguides_2024.position_and_maze.jguidera_ppt_interp import (
        PptDig,
        PptDigParams,
        PptDigSel,
        PptInterp,
        PptInterpSel,
        PptRCB,
        PptRCBSel,
    )
    from src.jguides_2024.spike_sorting_curation.jguidera_artifact import (
        ArtifactDetectionAcrossSortGroups,
        ArtifactDetectionAcrossSortGroupsParams,
        ArtifactDetectionAcrossSortGroupsSelection,
    )
    from src.jguides_2024.spike_sorting_curation.jguidera_reference_electrode import (
        ReferenceElectrode,
    )
    from src.jguides_2024.spike_sorting_curation.jguidera_spikesorting import (
        SpikeSortingRecordingCohort,
        SpikeSortingRecordingCohortParams,
    )
    from src.jguides_2024.spikes.jguidera_res_spikes import (
        ResEpochSpikeCounts,
        ResEpochSpikeCountsSel,
        ResEpochSpikesSm,
        ResEpochSpikesSmDs,
        ResEpochSpikesSmDsParams,
        ResEpochSpikesSmParams,
        ResEpochSpikesSmSel,
        ResEpochSpikeTimes,
        ResEpochSpikeTimesSel,
    )
    from src.jguides_2024.spikes.jguidera_spikes import (
        EpochMeanFiringRate,
        EpochSpikeTimes,
        EpochSpikeTimesRelabel,
        EpochSpikeTimesRelabelParams,
    )
    from src.jguides_2024.spikes.jguidera_unit import (
        BrainRegionUnits,
        BrainRegionUnitsCohortType,
        BrainRegionUnitsFail,
        BrainRegionUnitsParams,
        BrainRegionUnitsSel,
        EpsUnits,
        EpsUnitsParams,
        EpsUnitsSel,
    )
    from src.jguides_2024.task_event.jguidera_dio_event import (
        DioEvents,
        ProcessedDioEvents,
        PumpDiosComplete,
    )
    from src.jguides_2024.task_event.jguidera_dio_trials import (
        DioWellADTrials,
        DioWellADTrialsParams,
        DioWellArrivalTrials,
        DioWellArrivalTrialsParams,
        DioWellArrivalTrialsSub,
        DioWellArrivalTrialsSubParams,
        DioWellArrivalTrialsSubSel,
        DioWellDATrials,
        DioWellDATrialsParams,
        DioWellDDTrials,
        DioWellDDTrialsParams,
        DioWellDepartureTrials,
        DioWellDepartureTrialsParams,
        DioWellTrials,
    )
    from src.jguides_2024.task_event.jguidera_statescript_event import (
        ProcessedStatescriptEvents,
        ProcessedStatescriptEventsDioMismatch,
        StatescriptEventInt,
        StatescriptEvents,
    )
    from src.jguides_2024.task_event.jguidera_task_event import (
        ContingencyEnvironmentColor,
        EventNamesMapDioStatescript,
        PumpTimes,
    )
    from src.jguides_2024.task_event.jguidera_task_performance import (
        AlternationTaskPerformance,
        AlternationTaskPerformanceStatistics,
        AlternationTaskRule,
        AlternationTaskWellIdentities,
        ContingencyActiveContingenciesMap,
        PerformanceOutcomeColors,
    )
    from src.jguides_2024.task_event.jguidera_task_value import (
        TimeExpecVal,
        TimeExpecValSel,
        TrialExpecVal,
        TrialExpecValParams,
        TrialExpecValSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_condition_trials import (
        ConditionTrials,
        ConditionTrialsParams,
        ConditionTrialsSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_cross_validation_pool import (
        TrainTestSplitPool,
        TrainTestSplitPoolSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_epoch_interval import (
        EpochInterval,
    )
    from src.jguides_2024.time_and_trials.jguidera_interval import (
        EpochIntervalListName,
    )
    from src.jguides_2024.time_and_trials.jguidera_kfold_cross_validation import (
        KFoldTrainTestSplit,
        KFoldTrainTestSplitParams,
        KFoldTrainTestSplitSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_leave_one_out_condition_trials_cross_validation import (
        LOOCTTrainTestSplit,
        LOOCTTrainTestSplitSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_ppt_trials import (
        PptTrials,
        PptTrialsParams,
        PptTrialsSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_relative_time_at_well import (
        RelTimeDelay,
        RelTimeDelaySel,
        RelTimeWell,
        RelTimeWellPostDelay,
        RelTimeWellPostDelaySel,
        RelTimeWellSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_res_set import (
        ResSet,
        ResSetParamName,
        ResSetParams,
    )
    from src.jguides_2024.time_and_trials.jguidera_res_time_bins import (
        ResDioWATrialsTimeBins,
        ResDioWATrialsTimeBinsSel,
        ResDioWellADTrialsTimeBins,
        ResDioWellADTrialsTimeBinsSel,
        ResEpochTimeBins,
        ResEpochTimeBinsSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_res_time_bins_pool import (
        ResTimeBinsPool,
        ResTimeBinsPoolCohort,
        ResTimeBinsPoolCohortParamName,
        ResTimeBinsPoolCohortParams,
        ResTimeBinsPoolSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_time_bins import (
        DioWATrialsSubTimeBins,
        DioWATrialsSubTimeBinsParams,
        DioWATrialsSubTimeBinsSel,
        DioWATrialsTimeBins,
        DioWATrialsTimeBinsParams,
        DioWATrialsTimeBinsSel,
        DioWellADTrialsTimeBins,
        DioWellADTrialsTimeBinsParams,
        DioWellADTrialsTimeBinsSel,
        DioWellDATrialsTimeBins,
        DioWellDATrialsTimeBinsParams,
        DioWellDATrialsTimeBinsSel,
        EpochTimeBins,
        EpochTimeBinsParams,
    )
    from src.jguides_2024.time_and_trials.jguidera_time_relative_to_well_event import (
        TimeRelWA,
        TimeRelWADig,
        TimeRelWADigParams,
        TimeRelWADigSel,
        TimeRelWADigSingleAxis,
        TimeRelWADigSingleAxisParams,
        TimeRelWADigSingleAxisSel,
        TimeRelWARCB,
        TimeRelWARCBSel,
        TimeRelWASel,
    )
    from src.jguides_2024.time_and_trials.jguidera_timestamps import (
        EpochTimestamps,
    )
    from src.jguides_2024.time_and_trials.jguidera_trials_pool import (
        TrialsPool,
        TrialsPoolCohort,
        TrialsPoolCohortParamName,
        TrialsPoolCohortParams,
        TrialsPoolEpsCohort,
        TrialsPoolEpsCohortParams,
        TrialsPoolSel,
    )
    from src.jguides_2024.time_and_trials.jguidera_warped_axis_bins import (
        WarpedAxisBins,
        WarpedAxisBinsParams,
    )

    # Return table
    return eval(table_name)
