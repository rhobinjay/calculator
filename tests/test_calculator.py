import pytest
import calculator

# def test_operation_add_int():
#     result = calculator.add(1, 2)
#     assert result == 3

# def test_operation_add_float():
#     result = calculator.add(1.3, 2.5)
#     assert result == 3.8

def case(given, when, then):
    return pytest.param(*given, then, id=when)


@pytest.mark.parametrize('x,y,expected', [
    case(
        given=[1, 2],
        when='where int',
        then=3
    ),
    case(
        given=[1.3, 2.5],
        when='where float',
        then=3.8
    ),
])
def test_operation_add(x,y,expected):
    result = calculator.add(x,y)
    assert result == expected


# @pytest.mark.parametrize('x,y,expected', [
#     case(
#         given=[1, 2],
#         when='where int',
#         then=3
#     ),
#     case(
#         given=[1.3, 2.5],
#         when='where float',
#         then=3.8
#     ),
# ])
# def test_operation_add2(input,expected):
#     input['x']
#     input['y']
#     result = calculator.add(x,y)
#     assert result == expected



# @pytest.mark.parametrize('x,y,expected', [
#     pytest.param(1, 2, 3, id='where_int'),
#     pytest.param(1.3, 2.5, 3.8, id='where_float')
# ])
# def test_operation_add(x,y,expected):
#     result = calculator.add(x,y)
#     assert result == expected
