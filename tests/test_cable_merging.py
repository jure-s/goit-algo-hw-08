from cable_merging import min_cable_cost

def test_min_cable_cost():
    assert min_cable_cost([8, 4, 6, 12]) == 58
    assert min_cable_cost([20, 4, 8, 2]) == 54
    assert min_cable_cost([1, 2, 3, 4, 5]) == 33
