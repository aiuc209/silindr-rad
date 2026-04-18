import pytest
import math

def calculate_lateral_surface(radius_list, height_list):
    if len(radius_list) != len(height_list):
        raise ValueError("Radius and height lists must be of the same length")
    lateral_surfaces = []
    for radius, height in zip(radius_list, height_list):
        lateral_surface = 2 * math.pi * radius * height
        lateral_surfaces.append(lateral_surface)
    return lateral_surfaces

def test_calculate_lateral_surface():
    radius_list = [1, 2, 3]
    height_list = [4, 5, 6]
    expected_result = [2 * math.pi * r * h for r, h in zip(radius_list, height_list)]
    assert calculate_lateral_surface(radius_list, height_list) == pytest.approx(expected_result)

def test_calculate_lateral_surface_empty_lists():
    radius_list = []
    height_list = []
    expected_result = []
    assert calculate_lateral_surface(radius_list, height_list) == expected_result

def test_calculate_lateral_surface_lists_of_different_lengths():
    radius_list = [1, 2, 3]
    height_list = [4, 5]
    with pytest.raises(ValueError):
        calculate_lateral_surface(radius_list, height_list)
