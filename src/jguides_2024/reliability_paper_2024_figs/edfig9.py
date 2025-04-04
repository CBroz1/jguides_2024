import os

# Import custom datajoint tables
from jguides_2024.reliability_paper_2024_figs.population_reliability_plot_helpers import (
    _add_medium_long_sized_plot_params,
    _add_medium_sized_plot_params,
    _add_outbound_path_x_params,
    fr_vec_plot,
)

analysis_dir = "/home/jguidera/Src/jguides_2024"
# Single trial, same outbound path different outbound path, correct trials, single rats

# Parameters
plot_type = "same_different_outbound_path_correct"
boot_set_name = "default"
rat_cohort = False
brain_regions_separate = True
median = False
single_epochs_plot = False
dmPFC_OFC_only = True
# Table names and accompanying params
table_names = ["PathFRVecSTAveSumm"]
label_names = ["path"]
relationship_vals_list = [
    [
        "outbound_correct_correct_trials",
        "same_path_outbound_correct_correct_trials",
    ]
]
# Processing/saving
populate_tables = False
make_plot = True
save_fig = False

metric_names = ["cosine_similarity", "euclidean_distance"]
vector_types = ["diff_vec", "vec"]
params = {
    "populate_tables": populate_tables,
    "save_fig": save_fig,
    "path_fr_vec_param_name": "correct_incorrect_trials",
}
params = _add_medium_sized_plot_params(params, extra_gaps=True)
params = _add_outbound_path_x_params(params)

params.update(
    {"yticklabels": None}
)  # causes y tick labels to be placed on all plots

if make_plot:
    for metric_name, vector_type in zip(metric_names, vector_types):
        fr_vec_plot(
            plot_type,
            boot_set_name,
            rat_cohort,
            brain_regions_separate,
            median,
            single_epochs_plot,
            dmPFC_OFC_only,
            metric_name,
            vector_type,
            table_names,
            label_names,
            relationship_vals_list,
            params,
        )


# Single trial, stay leave, single rats

# Parameters
plot_type = "single_trial_stay_leave"
boot_set_name = "default"
rat_cohort = False
brain_regions_separate = True
median = False
single_epochs_plot = False
dmPFC_OFC_only = True
# Table names and accompanying params
table_names = ["TimeRelWAFRVecSTAveSumm"]
label_names = ["path"]
relationship_vals_list = [
    ["same_path_stay_leave_trials", "same_path_stay_stay_trials"]
]
# Processing/saving
populate_tables = True
make_plot = True
save_fig = False

metric_names = ["cosine_similarity", "euclidean_distance"]
vector_types = ["diff_vec", "vec"]
ylims = [[-0.15, 0.7], [-0.15, 0.45]]
yticks = [0, 0.2, 0.4, 0.6]

params = {
    "populate_tables": populate_tables,
    "save_fig": save_fig,
    "yticks": yticks,
}
params = _add_medium_sized_plot_params(params)

params.update(
    {"yticklabels": None}
)  # causes y tick labels to be placed on all plots

for metric_name, vector_type, ylim in zip(metric_names, vector_types, ylims):
    params.update(
        {
            "ylim": ylim,
        }
    )
    fr_vec_plot(
        plot_type,
        boot_set_name,
        rat_cohort,
        brain_regions_separate,
        median,
        single_epochs_plot,
        dmPFC_OFC_only,
        metric_name,
        vector_type,
        table_names,
        label_names,
        relationship_vals_list,
        params,
    )


# Extra:

# Path traversal

# Single trial, same outbound path different outbound path difference, correct trials,
# single rats

# Parameters
plot_type = "same_different_outbound_path_correct"
boot_set_name = "same_different_outbound_path_correct_diff"
rat_cohort = False
brain_regions_separate = True
median = False
single_epochs_plot = False
dmPFC_OFC_only = True
# Table names and accompanying params
table_names = ["PathFRVecSTAveSumm"]
label_names = ["path"]
relationship_vals_list = [
    [
        "outbound_correct_correct_trials_same_path_outbound_correct_correct_trials"
    ]
]
# Processing/saving
populate_tables = False
make_plot = False
save_fig = False

metric_names = ["cosine_similarity", "euclidean_distance"]
vector_types = ["diff_vec", "vec"]
params = {
    "populate_tables": populate_tables,
    "save_fig": save_fig,
    "path_fr_vec_param_name": "correct_incorrect_trials",
    "ylim": [-0.1, 0.5],
}
params = _add_medium_sized_plot_params(params, extra_gaps=True)
params = _add_outbound_path_x_params(params)

params.update(
    {"yticklabels": None}
)  # causes y tick labels to be placed on all plots

# wspace = .25
# yticklabels = None  # causes y tick labels to be placed on all plots
# params = {"populate_tables": populate_tables, "save_fig": save_fig, "wspace": wspace, "yticklabels": yticklabels}

if make_plot:
    for metric_name, vector_type in zip(metric_names, vector_types):
        fr_vec_plot(
            plot_type,
            boot_set_name,
            rat_cohort,
            brain_regions_separate,
            median,
            single_epochs_plot,
            dmPFC_OFC_only,
            metric_name,
            vector_type,
            table_names,
            label_names,
            relationship_vals_list,
            params,
        )


# Single trial, same outbound path vs. different outbound path, correct trials, brain region difference, single rats

# Parameters
plot_type = "same_different_outbound_path_correct_diff"
boot_set_name = "same_different_outbound_path_correct_diff_brain_region_diff"
rat_cohort = False
brain_regions_separate = False
median = False
single_epochs_plot = False
dmPFC_OFC_only = True
# Table names and accompanying params
table_names = ["PathFRVecSTAveSumm"]
label_names = ["path"]
relationship_vals_list = [
    [
        "outbound_correct_correct_trials_same_path_outbound_correct_correct_trials"
    ]
]
# Processing/saving
populate_tables = False
make_plot = False
save_fig = False

params = {
    "populate_tables": populate_tables,
    "save_fig": save_fig,
    "path_fr_vec_param_name": "correct_incorrect_trials",
    "xlim": [0, 0.5],
    "ylim": [-0.1, 0.3],
    "yticks": [0, 0.3],
}
params = _add_medium_long_sized_plot_params(params)
params = _add_outbound_path_x_params(params)

params.update(
    {"yticklabels": None}
)  # causes y tick labels to be placed on all plots

if make_plot:
    for metric_name, vector_type in zip(metric_names, vector_types):
        fr_vec_plot(
            plot_type,
            boot_set_name,
            rat_cohort,
            brain_regions_separate,
            median,
            single_epochs_plot,
            dmPFC_OFC_only,
            metric_name,
            vector_type,
            table_names,
            label_names,
            relationship_vals_list,
            params,
        )


# Delay period


# Single trial, stay leave difference, single rats

# Parameters
plot_type = "single_trial_stay_leave"
boot_set_name = "stay_leave_diff"
rat_cohort = False
brain_regions_separate = True
median = False
single_epochs_plot = False
dmPFC_OFC_only = True
# Table names and accompanying params
table_names = ["TimeRelWAFRVecSTAveSumm"]
label_names = ["path"]
relationship_vals_list = [
    ["same_path_stay_leave_trials_same_path_stay_stay_trials"]
]
# Processing/saving
populate_tables = True
make_plot = False
save_fig = False

ylim = [-0.15, 0.35]
yticks = [0, 0.2]

params = {
    "populate_tables": populate_tables,
    "save_fig": save_fig,
    "ylim": ylim,
    "yticks": yticks,
}
params = _add_medium_sized_plot_params(params, extra_gaps=True)

params.update(
    {"yticklabels": None}
)  # causes y tick labels to be placed on all plots

if make_plot:
    for metric_name, vector_type in zip(metric_names, vector_types):
        fr_vec_plot(
            plot_type,
            boot_set_name,
            rat_cohort,
            brain_regions_separate,
            median,
            single_epochs_plot,
            dmPFC_OFC_only,
            metric_name,
            vector_type,
            table_names,
            label_names,
            relationship_vals_list,
            params,
        )


# Single trial, stay leave difference, brain region difference, single rats

# Parameters
plot_type = "single_trial_stay_leave_brain_region_diff"
boot_set_name = "stay_leave_diff_brain_region_diff"
rat_cohort = False
brain_regions_separate = False
median = False
single_epochs_plot = False
dmPFC_OFC_only = True
# Table names and accompanying params
table_names = ["TimeRelWAFRVecSTAveSumm"]
label_names = ["path"]
relationship_vals_list = [
    ["same_path_stay_leave_trials_same_path_stay_stay_trials"]
]
# Processing/saving
populate_tables = False
make_plot = False
save_fig = False

ylim = [-0.35, 0.15]
yticks = [-0.2, 0]
params = {
    "populate_tables": populate_tables,
    "save_fig": save_fig,
    "ylim": ylim,
    "yticks": yticks,
    "xticklabels": [],
}
params = _add_medium_long_sized_plot_params(params)

if make_plot:
    for metric_name, vector_type in zip(metric_names, vector_types):
        fr_vec_plot(
            plot_type,
            boot_set_name,
            rat_cohort,
            brain_regions_separate,
            median,
            single_epochs_plot,
            dmPFC_OFC_only,
            metric_name,
            vector_type,
            table_names,
            label_names,
            relationship_vals_list,
            params,
        )
