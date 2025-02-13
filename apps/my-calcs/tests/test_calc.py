"""Hello unit test module."""

from apps_my_calcs.calc import calc


def test_calc():
    """Test the calc function."""
    assert calc(1,2) == 3
