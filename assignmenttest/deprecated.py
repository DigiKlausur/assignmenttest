import warnings

def deprecation_warning():
    previous_warning_filters = warnings.filters[:]
    warnings.filterwarnings("always", category=DeprecationWarning, module="assignmenttest")
    warnings.warn("The package assignmenttest is deprecated. Use e2xgradingtools instead.", DeprecationWarning)
    warnings.filters = previous_warning_filters

def deprecated_decorator(func):
    def wrapper(*args, **kwargs):
        previous_warning_filters = warnings.filters[:]
        warnings.filterwarnings("always", category=DeprecationWarning, module="assignmenttest")
        old_import_string = f"{func.__module__}.{func.__name__}"
        new_import_string = old_import_string.replace("assignmenttest", "e2xgradingtools")
        message = f"{old_import_string} is deprecated. Use {new_import_string} instead."
        warnings.warn(message, DeprecationWarning)
        warnings.filters = previous_warning_filters
        return func(*args, **kwargs)
    return wrapper

def deprecated_class_decorator(cls):
    previous_warning_filters = warnings.filters[:]
    warnings.filterwarnings("always", category=DeprecationWarning, module="assignmenttest")
    old_import_string = f"{cls.__module__}.{cls.__name__}"
    new_import_string = old_import_string.replace("assignmenttest", "e2xgradingtools")
    message = f"{old_import_string} is deprecated. Use {new_import_string} instead."
    warnings.warn(message, DeprecationWarning)
    warnings.filters = previous_warning_filters

    return cls