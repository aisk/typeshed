"""Stub file for the 'cmath' module."""

import sys
from typing import Union, Tuple

e = ...  # type: float
pi = ...  # type: float

_C = Union[float, complex]

def acos(x:_C) -> complex: ...
def acosh(x:_C) -> complex: ...
def asin(x:_C) -> complex: ...
def asinh(x:_C) -> complex: ...
def atan(x:_C) -> complex: ...
def atanh(x:_C) -> complex: ...
def cos(x:_C) -> complex: ...
def cosh(x:_C) -> complex: ...
def exp(x:_C) -> complex: ...
def isinf(z:_C) -> bool: ...
def isnan(z:_C) -> bool: ...
def log(x:_C, base:_C = ...) -> complex: ...
def log10(x:_C) -> complex: ...
def phase(z:_C) -> float: ...
def polar(z:_C) -> Tuple[float, float]: ...
def rect(r:float, phi:float) -> complex: ...
def sin(x:_C) -> complex: ...
def sinh(x:_C) -> complex: ...
def sqrt(x:_C) -> complex: ...
def tan(x:_C) -> complex: ...
def tanh(x:_C) -> complex: ...

if sys.version_info[0] >= 3:
    def isfinite(z:_C) -> bool: ...
