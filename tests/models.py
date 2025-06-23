from dataclasses import dataclass, field
from typing import Any
import pytest


def case(given, when, then):
    parametrize_values = given + [then]
    return pytest.param(
        *parametrize_values,
        id=when,
    )

def foo(*args, **kwargs):
    print('asd')
    print('def')


@dataclass
class Cases:
    """A collection of test cases."""

    tests: list[case] = field(default_factory=foo)

    @property
    def arg_names(self):
        """Argument names"""
        return [p.values for p in self.tests]

    @property
    def args(self):
        """Argument values"""
        return self.arg_names, self.tests
