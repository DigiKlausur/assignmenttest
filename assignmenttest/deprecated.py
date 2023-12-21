import warnings


def deprecation_warning():
    previous_warning_filters = warnings.filters[:]
    warnings.filterwarnings(
        "always", category=DeprecationWarning, module="assignmenttest"
    )
    warnings.warn(
        "The package assignmenttest is deprecated. Use e2xgradingtools instead.",
        DeprecationWarning,
    )
    warnings.filters = previous_warning_filters
