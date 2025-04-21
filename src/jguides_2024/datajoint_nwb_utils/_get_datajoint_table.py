def _get_table(table_name):
    print(
        "WARNING: This function uses eval() to import tables. "
        +f"This is not recommended and should be avoided if possible."
    )
    # Avoid circular import
    from jguides_2024.metadata.jguidera_histology import ValidShank
    from jguides_2024.metadata.jguidera_brain_region import BrainRegionColor, ElectrodeGroupTargetedLocation, SortGroupTargetedLocation, BrainRegionSortGroupParams, BrainRegionSortGroup, BrainRegionCohort, CurationSetSel, CurationSet
    from jguides_2024.metadata.jguidera_premaze_durations import PremazeDurations
    from jguides_2024.metadata.jguidera_epoch import EpochFullLen, EpochCohortParams, EpochCohort, RunEpoch, DistinctRunEpochPair, RunEpochPair, SleepEpoch, HomeEpoch, EpochsDescription, EpochArtifactFree, EpochsDescriptions, RecordingSet, TrainTestEpoch, TrainTestEpochSet
    from jguides_2024.metadata.jguidera_metadata import JguideraNwbfileSel, JguideraNwbfile, TaskIdentification
    from jguides_2024.spike_sorting_curation.jguidera_spikesorting import SpikeSortingRecordingCohortParams, SpikeSortingRecordingCohort
    from jguides_2024.spike_sorting_curation.jguidera_reference_electrode import ReferenceElectrode
    from jguides_2024.spike_sorting_curation.jguidera_artifact import ArtifactDetectionAcrossSortGroupsParams, ArtifactDetectionAcrossSortGroupsSelection, ArtifactDetectionAcrossSortGroups
    from jguides_2024.position_and_maze.jguidera_position_stop import StopLikeWellArrivalParams, StopLikeWellArrivalSel, StopLikeWellArrival
    from jguides_2024.position_and_maze.jguidera_ppt import PptParams, PptSel, Ppt, PptBinEdgesParams, PptBinEdges
    from jguides_2024.position_and_maze.jguidera_position import IntervalPositionInfoRelabelParams, IntervalPositionInfoRelabel, IntervalLinearizedPositionRelabelParams, IntervalLinearizedPositionRelabel, IntervalLinearizedPositionRescaled
    from jguides_2024.position_and_maze.jguidera_maze import RewardWell, RewardWellPath, ForkMazeRewardWellPathPairSel, ForkMazeRewardWellPathPair, RewardWellColor, RewardWellPathColor, RewardWellPathTurnDirectionParams, RewardWellPathTurnDirection, MazeEdgeType, TrackGraphAnnotations, UniversalTrackGraphAnnotations, AnnotatedTrackGraph, AnnotatedUniversalTrackGraph, TrackGraphUniversalTrackGraphMapParams, UniversalTrackGraphPosBinEdgesParams, UniversalTrackGraphPosBinEdges, ForkMazePathEdgesSel, ForkMazePathEdges, UniversalForkMazePathEdgePathFractionMap, TrackGraphUniversalTrackGraphMap, EnvironmentColor
    from jguides_2024.position_and_maze.jguidera_ppt_interp import PptInterpSel, PptInterp, PptDigParams, PptDigSel, PptDig, PptRCBSel, PptRCB
    from jguides_2024.time_and_trials.jguidera_ppt_trials import PptTrialsParams, PptTrialsSel, PptTrials
    from jguides_2024.time_and_trials.jguidera_res_time_bins import ResEpochTimeBinsSel, ResEpochTimeBins, ResDioWATrialsTimeBinsSel, ResDioWATrialsTimeBins, ResDioWellADTrialsTimeBinsSel, ResDioWellADTrialsTimeBins
    from jguides_2024.time_and_trials.jguidera_trials_pool import TrialsPoolSel, TrialsPool, TrialsPoolCohortParamName, TrialsPoolCohortParams, TrialsPoolCohort, TrialsPoolEpsCohortParams, TrialsPoolEpsCohort
    from jguides_2024.time_and_trials.jguidera_interval import EpochIntervalListName
    from jguides_2024.time_and_trials.jguidera_res_time_bins_pool import ResTimeBinsPoolSel, ResTimeBinsPool, ResTimeBinsPoolCohortParamName, ResTimeBinsPoolCohortParams, ResTimeBinsPoolCohort
    from jguides_2024.time_and_trials.jguidera_time_bins import EpochTimeBinsParams, EpochTimeBins, DioWATrialsTimeBinsParams, DioWATrialsTimeBinsSel, DioWATrialsTimeBins, DioWATrialsSubTimeBinsParams, DioWATrialsSubTimeBinsSel, DioWATrialsSubTimeBins, DioWellDATrialsTimeBinsParams, DioWellDATrialsTimeBinsSel, DioWellDATrialsTimeBins, DioWellADTrialsTimeBinsParams, DioWellADTrialsTimeBinsSel, DioWellADTrialsTimeBins
    from jguides_2024.time_and_trials.jguidera_kfold_cross_validation import KFoldTrainTestSplitParams, KFoldTrainTestSplitSel, KFoldTrainTestSplit
    from jguides_2024.time_and_trials.jguidera_time_relative_to_well_event import TimeRelWASel, TimeRelWA, TimeRelWADigParams, TimeRelWADigSel, TimeRelWADig, TimeRelWADigSingleAxisParams, TimeRelWADigSingleAxisSel, TimeRelWADigSingleAxis, TimeRelWARCBSel, TimeRelWARCB
    from jguides_2024.time_and_trials.jguidera_cross_validation_pool import TrainTestSplitPoolSel, TrainTestSplitPool
    from jguides_2024.time_and_trials.jguidera_warped_axis_bins import WarpedAxisBinsParams, WarpedAxisBins
    from jguides_2024.time_and_trials.jguidera_relative_time_at_well import RelTimeWellSel, RelTimeWell, RelTimeDelaySel, RelTimeDelay, RelTimeWellPostDelaySel, RelTimeWellPostDelay, RelTimeWellPostDelayDigParams, RelTimeWellPostDelayDigSel, RelTimeWellPostDelayDig
    from jguides_2024.time_and_trials.jguidera_timestamps import EpochTimestamps
    from jguides_2024.time_and_trials.jguidera_leave_one_out_condition_trials_cross_validation import LOOCTTrainTestSplitSel, LOOCTTrainTestSplit
    from jguides_2024.time_and_trials.jguidera_res_set import ResSetParamName, ResSetParams, reset
    from jguides_2024.time_and_trials.jguidera_epoch_interval import EpochInterval
    from jguides_2024.time_and_trials.jguidera_condition_trials import ConditionTrialsParams, ConditionTrialsSel, ConditionTrials
    from jguides_2024.firing_rate_map.jguidera_ppt_firing_rate_map import FrmapPptSel, FrmapPpt, FrmapPptSmParams, FrmapPptSm, CorrFrmapPptSm, OverlapFrmapPptSm, FrmapPupt, FrmapPuptSm, STFrmapPupt, STFrmapPuptSm
    from jguides_2024.firing_rate_map.jguidera_well_arrival_departure_firing_rate_map import FrmapWADParams, STFrmapWAD, FrmapWADSmParams, STFrmapWADSm, STFrmapWADSmWTSel, STFrmapWADSmWT, FrmapWADSmWTParams, FrmapWADSmWT
    from jguides_2024.firing_rate_map.jguidera_well_arrival_firing_rate_map import FrmapWellArrivalParams, FrmapWellArrivalSel, FrmapWellArrival, FrmapUniqueWellArrival, FrmapWellArrivalSmParams, FrmapWellArrivalSm, FrmapUniqueWellArrivalSm, STFrmapWellArrival, STFrmapWellArrivalSm
    from jguides_2024.glm.jguidera_basis_function import RaisedCosineBasisParams, RaisedCosineBasis
    from jguides_2024.glm.jguidera_el_net import ElNetParams, ElNetSel, ElNet
    from jguides_2024.glm.jguidera_measurements_interp_pool import InterceptSel, Intercept, XInterpPoolSel, XInterpPool, XInterpPoolCohortParamName, XInterpPoolCohortParams, XInterpPoolCohort, XInterpPoolCohortEpsCohortParams, XInterpPoolCohortEpsCohort
    from jguides_2024.firing_rate_vector.jguidera_multi_cov_firing_rate_vector_decode import DecodeMultiCovFRVecParams
    from jguides_2024.firing_rate_vector.jguidera_well_event_firing_rate_vector_decode import DecodeTimeRelWAFRVecParams, DecodeTimeRelWAFRVecSel, DecodeTimeRelWAFRVec, DecodeTimeRelWAFRVecSummParams, DecodeTimeRelWAFRVecSummSel, DecodeTimeRelWAFRVecSumm
    from jguides_2024.firing_rate_vector.jguidera_firing_rate_difference_vector_similarity import FRDiffVecCosSimSel, FRDiffVecCosSim
    from jguides_2024.firing_rate_vector.jguidera_firing_rate_vector_euclidean_distance import FRVecEucDistSel, FRVecEucDist
    from jguides_2024.firing_rate_vector.jguidera_path_firing_rate_vector import PathFRVecParams, PathFRVecSel, PathFRVec, PathFRVecSTAveParams, PathFRVecSTAveSel, PathFRVecSTAve, PathAveFRVecParams, PathAveFRVecSel, PathAveFRVec, PathFRVecSTAveSummParams, PathFRVecSTAveSummSel, PathFRVecSTAveSumm, PathAveFRVecSummParams, PathAveFRVecSummSel, PathAveFRVecSumm
    from jguides_2024.firing_rate_vector.jguidera_multi_cov_firing_rate_vector import MultiCovFRVecParams, MultiCovFRVecSel, MultiCovFRVec, MultiCovAveFRVecParams, MultiCovAveFRVecSel, MultiCovAveFRVec, MultiCovFRVecSTAveParams, MultiCovFRVecSTAveSel, MultiCovFRVecSTAve, MultiCovFRVecSTAveSummParams, MultiCovFRVecSTAveSummSel, MultiCovFRVecSTAveSumm, MultiCovAveFRVecSummParams, MultiCovAveFRVecSummSel, MultiCovAveFRVecSumm
    from jguides_2024.firing_rate_vector.jguidera_firing_rate_vector import FRVecSel, FRVec
    from jguides_2024.firing_rate_vector.jguidera_path_firing_rate_vector_decode import DecodePathFRVecParams, DecodePathFRVecSel, DecodePathFRVec, DecodePathFRVecSummParams, DecodePathFRVecSummSel, DecodePathFRVecSumm
    from jguides_2024.firing_rate_vector.jguidera_post_delay_firing_rate_vector import RelPostDelFRVecParams, RelPostDelFRVecSel, RelPostDelFRVec, RelPostDelAveFRVecParams, RelPostDelAveFRVecSel, RelPostDelAveFRVec
    from jguides_2024.firing_rate_vector.jguidera_firing_rate_difference_vector_similarity_ave import FRDiffVecCosSimPptNnAveParams, FRDiffVecCosSimPptNnAveSel, FRDiffVecCosSimPptNnAve, FRDiffVecCosSimWANnAveParams, FRDiffVecCosSimWANnAveSel, FRDiffVecCosSimWANnAve, FRDiffVecCosSimWANnAveSummParams, FRDiffVecCosSimWANnAveSummSel, FRDiffVecCosSimWANnAveSumm, FRDiffVecCosSimPptNnAveSummParams, FRDiffVecCosSimPptNnAveSummSel, FRDiffVecCosSimPptNnAveSumm
    from jguides_2024.firing_rate_vector.jguidera_firing_rate_difference_vector import FRDiffVecParams, FRDiffVecSel, FRDiffVec
    from jguides_2024.firing_rate_vector.jguidera_well_event_firing_rate_vector import TimeRelWAFRVecParams, TimeRelWAFRVecSel, TimeRelWAFRVec, TimeRelWAFRVecSTAveParams, TimeRelWAFRVecSTAveSel, TimeRelWAFRVecSTAve, TimeRelWAAveFRVecParams, TimeRelWAAveFRVecSel, TimeRelWAAveFRVec, TimeRelWAFRVecSTAveSummParams, TimeRelWAFRVecSTAveSummSel, TimeRelWAFRVecSTAveSumm, TimeRelWAAveFRVecSummParams, TimeRelWAAveFRVecSummSel, TimeRelWAAveFRVecSumm
    from jguides_2024.firing_rate_vector.jguidera_firing_rate_vector_embedding import FRVecEmbParams, FRVecEmbSel, FRVecEmb
    from jguides_2024.spikes.jguidera_unit import EpsUnitsParams, EpsUnitsSel, EpsUnits, BrainRegionUnitsParams, BrainRegionUnitsSel, BrainRegionUnitsFail, BrainRegionUnits, BrainRegionUnitsCohortType
    from jguides_2024.spikes.jguidera_res_spikes import ResEpochSpikeTimesSel, ResEpochSpikeTimes, ResEpochSpikeCountsSel, ResEpochSpikeCounts, ResEpochSpikesSmParams, ResEpochSpikesSmSel, ResEpochSpikesSm, ResEpochSpikesSmDsParams, ResEpochSpikesSmDs
    from jguides_2024.spikes.jguidera_spikes import EpochSpikeTimes, EpochSpikeTimesRelabelParams, EpochSpikeTimesRelabel, EpochMeanFiringRate
    from jguides_2024.task_event.jguidera_dio_trials import DioWellTrials, DioWellDDTrialsParams, DioWellDDTrials, DioWellDATrialsParams, DioWellDATrials, DioWellADTrialsParams, DioWellADTrials, DioWellArrivalTrialsParams, DioWellArrivalTrials, DioWellArrivalTrialsSubParams, DioWellArrivalTrialsSubSel, DioWellArrivalTrialsSub, DioWellDepartureTrialsParams, DioWellDepartureTrials
    from jguides_2024.task_event.jguidera_task_value import TrialExpecValParams, TrialExpecValSel, TrialExpecVal, TimeExpecValSel, TimeExpecVal
    from jguides_2024.task_event.jguidera_dio_event import DioEvents, ProcessedDioEvents, PumpDiosComplete
    from jguides_2024.task_event.jguidera_task_performance import AlternationTaskWellIdentities, AlternationTaskRule, AlternationTaskPerformance, PerformanceOutcomeColors, AlternationTaskPerformanceStatistics, ContingencyActiveContingenciesMap
    from jguides_2024.task_event.jguidera_task_event import EventNamesMapDioStatescript, PumpTimes, ContingencyEnvironmentColor
    from jguides_2024.task_event.jguidera_statescript_event import StatescriptEvents, ProcessedStatescriptEventsDioMismatch, ProcessedStatescriptEvents, StatescriptEventInt
    from jguides_2024.edeno_decoder.jguidera_edeno_decoder_helpers import StackedEdgeTrackGraph, EDPathGroups, TrackGraphSourceSortedSpikesClassifierParams
    from jguides_2024.edeno_decoder.jguidera_edeno_decoder_error import EdenoDecodeErrParams, EdenoDecodeErrSel, EdenoDecodeErr, EdenoDecodeErrSummBinParams, EdenoDecodeErrSummSecKeyParams, EdenoDecodeErrSummSel, EdenoDecodeErrSumm
    from jguides_2024.edeno_decoder.jguidera_edeno_decoder_run import EDDecodeVariableParams, EDCrossValidationParams, EDAlgorithmParams, EDComputeParams, EDStorageParams, EdenoDecodeParams, EdenoDecodeSel, EdenoDecode, EdenoDecodeMAPSel, EdenoDecodeMAPSel, EdenoDecodeMAP
    # Return table
    return eval(table_name)
