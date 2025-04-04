import datajoint as dj
import pandas as pd
from spyglass.common import AnalysisNwbfile

from jguides_2024.datajoint_nwb_utils.datajoint_table_base import (
    ComputedBase,
)
from jguides_2024.datajoint_nwb_utils.datajoint_table_helpers import (
    get_schema_table_names_from_file,
    insert_analysis_table_entry,
    populate_insert,
)
from jguides_2024.datajoint_nwb_utils.nwbf_helpers import get_nwb_file
from jguides_2024.datajoint_nwb_utils.unpack_nwbf import (
    get_epoch_timestamps_nwbf,
)
from jguides_2024.metadata.jguidera_metadata import TaskIdentification

schema = dj.schema("jguidera_timestamps")


@schema
class EpochTimestamps(ComputedBase):
    definition = """
    # Timestamps within epoch
    -> TaskIdentification
    ---
    -> AnalysisNwbfile
    epoch_timestamps_object_id : varchar(40)
    """

    def make(self, key):
        # Hard code parameters for getting epoch timestamps
        num_samples_estimation = 10000000
        expected_sampling_rates = [30000]
        error_tolerance_expected_vs_estimated_fs = 0.5
        tolerance_distance_to_epoch_bounds = 0.005

        # Get sample times during epoch (in PTP and Trodes time)
        nwbf = get_nwb_file(key["nwb_file_name"])
        epoch_sample_times_df = pd.DataFrame.from_dict(
            get_epoch_timestamps_nwbf(
                nwbf=nwbf,
                epoch=key["epoch"],
                num_samples_estimation=num_samples_estimation,
                expected_sampling_rates=expected_sampling_rates,
                error_tolerance_expected_vs_estimated_fs=error_tolerance_expected_vs_estimated_fs,
                tolerance_distance_to_epoch_bounds=tolerance_distance_to_epoch_bounds,
            )
        )
        insert_analysis_table_entry(
            self, [epoch_sample_times_df], key, ["epoch_timestamps_object_id"]
        )


def populate_jguidera_timestamps(key=None, tolerate_error=False):
    schema_name = "jguidera_timestamps"
    for table_name in get_schema_table_names_from_file(schema_name):
        table = eval(table_name)
        populate_insert(table, key=key, tolerate_error=tolerate_error)


def drop_jguidera_timestamps():
    schema.drop()
