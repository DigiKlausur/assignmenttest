from .variables import VariableTest
from .functions import FunctionTest
from .utils import grade_report
from .classes import ClassTest
from .deprecated import deprecation_warning

deprecation_warning()

__all__ = ["ClassTest", "grade_report", "FunctionTest", "VariableTest"]
