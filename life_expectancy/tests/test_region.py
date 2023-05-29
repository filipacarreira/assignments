"""Tests for the region enum"""

from typing import List
import numpy as np
from life_expectancy.region import Region

def test_regions_list(expected_countries: List[str]):
    """Test for the region listing function"""
    region_list = Region.list_all_countries()
    np.testing.assert_array_equal(region_list, expected_countries)
