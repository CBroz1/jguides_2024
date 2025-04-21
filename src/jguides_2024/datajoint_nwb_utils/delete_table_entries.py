# Delete entries from downstream tables to avoid error when deleting from upstream tables

from spyglass.spikesorting.v0.spikesorting_artifact import (
    ArtifactDetectionSelection,
)
from spyglass.spikesorting.v0.spikesorting_curation import Curation
from spyglass.spikesorting.v0.spikesorting_recording import (
    SpikeSortingRecordingSelection,
)
from spyglass.spikesorting.v0.spikesorting_sorting import SpikeSortingSelection

from jguides_2024.firing_rate_vector.jguidera_firing_rate_vector_embedding import (
    FRVecEmb,
)
from jguides_2024.metadata.jguidera_brain_region import BrainRegionSortGroup
from jguides_2024.metadata.jguidera_epoch import EpochCohort
from jguides_2024.position_and_maze.jguidera_position import (
    IntervalLinearizedPositionRelabel,
)
from jguides_2024.position_and_maze.jguidera_ppt import Ppt
from jguides_2024.spike_sorting_curation.jguidera_spikesorting import (
    SpikeSortingRecordingCohortParams,
)
from jguides_2024.spikes.jguidera_spikes import EpochSpikeTimes
from jguides_2024.time_and_trials.jguidera_trials_pool import TrialsPool


def delete_table_entries(key):
    (FRVecEmb & key).delete()
    (TrialsPool & key).delete_(key=key)
    (Ppt & key).delete()
    (IntervalLinearizedPositionRelabel & key).delete()
    delete_spikesorting_table_entries(key)
    (BrainRegionSortGroup & key).delete()
    (EpochCohort & key).delete()


def delete_curation_table_entries(key, safemode=True):
    """
    Delete entries in curation table
    :param key: dictionary with key to query tables
    """

    # Check inputs
    if "nwb_file_name" not in key:
        raise Exception(
            "nwb_file_name must be passed in key in order to delete entries from SpikeSortingRecordingCohortParams"
        )
    (EpochSpikeTimes & key).delete_(key=key, safemode=safemode)
    (Curation & key).delete(safemode=safemode)


def delete_spikesorting_table_entries(key):
    """
    Delete entries in spikesorting tables, up through the most upstream table: SpikeSortingRecordingSelection
    :param key: dictionary with key to query tables
    """

    delete_curation_table_entries(key)
    (SpikeSortingSelection & key).delete()
    (ArtifactDetectionSelection & key).delete()
    (SpikeSortingRecordingCohortParams & key).delete()
    (SpikeSortingRecordingSelection & key).delete()
