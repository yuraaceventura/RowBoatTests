import pytest
from main import RowBoat, BoatFullException, InvalidDirectionException
from contextlib import nullcontext as does_not_raise

@pytest.mark.parametrize("capacity, passengers, exception", [
    (1, ["John"], does_not_raise()),
    (1, ["John", "Alice"], pytest.raises(BoatFullException)),
])
def test_load_passenger(capacity, passengers:list[str], exception):
    boat = RowBoat(capacity=capacity)
    with exception:
        for passenger in passengers:
            boat.load_passenger(passenger)
        assert passenger in boat.passengers


def test_rowing():
    boat = RowBoat()
    boat.start_rowing()
    assert boat.in_motion
    boat.stop_rowing()
    assert not boat.in_motion


@pytest.mark.parametrize("direction, exception", [
    ("влево", does_not_raise()),
    ("назад", pytest.raises(InvalidDirectionException)),
])
def test_set_direction(direction, exception):
    boat = RowBoat()
    with exception:
        boat.set_direction(direction)
    if exception == does_not_raise():
        assert boat.direction == direction

@pytest.mark.parametrize("capacity, passengers", [
    (2, ["John", "Alice"]),
])
def test_unload_passenger(capacity, passengers):
    boat = RowBoat(capacity)
    for passenger in passengers:
        boat.load_passenger(passenger)
        boat.unload_passenger(passenger)
        assert passenger not in boat.passengers
