import pytest
from main import RowBoat, BoatFullException, InvalidDirectionException
from contextlib import nullcontext as does_not_raise


@pytest.mark.parametrize("capacity, passengers", [
    (1, ["John"]),
    (2, ["John", "Alice"]),
])
def test_boat(capacity, passengers:list[str]):
    boat = RowBoat(capacity)

    #Загружаем пассажиров
    for passenger in passengers:
        boat.load_passenger(passenger)
    assert boat.passengers == passengers

    #Начали плыть
    boat.start_rowing()
    assert boat.in_motion

    #Приплыли
    boat.stop_rowing()
    assert not boat.in_motion

    #Разгружаем пассажиров
    for passenger in passengers:
        boat.unload_passenger(passenger)
    assert boat.passengers == []

