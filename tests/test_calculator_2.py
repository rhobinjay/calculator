import pytest
import calculator


def test_operation_add_int():
    result = calculator.add(1, 2)
    assert result == 3


def test_operation_add_float():
    result = calculator.add(1.5, 2.2)
    assert result == 3.7


@pytest.mark.parametrize('x,y,expected_result',
[
    # WHEN addends are integer
    (1, 2, 3),
    # WHEN addends are float
    (1.5, 2.2, 3.7)
])
def test_operation_add(x, y, expected_result):
    result = calculator.add(x, y)
    assert result == expected_result



def case(given, when, then):
    parametrize_values = given + [then]
    return pytest.param(
        *parametrize_values,
        id=when,
    )


@pytest.mark.parametrize('x,y,expected_result',
[
    # (1, 2, 3),
    case(
        given=[1, 2],
        when="addends are integer",
        then=3
    ),
    # WHEN addends are float
    (1.5, 2.2, 3.7)
])
def test_operation_add_in_test_models(x, y, expected_result):
    result = calculator.add(x, y)
    assert result == expected_result


###################
###################
from .models import Cases

def test_foo():
    c1 = Cases(
        [
            case(
                given=[1, 2], # given={'x': 1, 'y': 2},
                when="addends are integer",
                then=3
            ),
        ]
    )
    assert True

# def cases(mycases):

#     pass

# @pytest.mark.parametrize(
#     Cases(
#         [
#             case(
#                 given={'x': 1, 'y': 2},
#                 when="addends are integer",
#                 then=3
#             ),
#         ]
#     ).args
# )
# def test_operation_add_in_test_models(x, y, expected_result):
#     result = calculator.add(x, y)
#     assert result == expected_result