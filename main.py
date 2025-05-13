class BoatFullException(Exception):
    pass

class InvalidDirectionException(Exception):
    pass

class RowBoat:
    VALID_DIRECTIONS = {"прямо", "влево", "вправо"}

    def __init__(self, capacity=2):
        self.capacity = capacity
        self.passengers = []
        self.in_motion = False
        self.direction = "прямо"

    def load_passenger(self, name: str):
        if len(self.passengers) >= self.capacity:
            raise BoatFullException("Лодка переполнена")
        self.passengers.append(name)

    def unload_passenger(self, name: str):
        if name in self.passengers:
            self.passengers.remove(name)

    def start_rowing(self):
        self.in_motion = True

    def stop_rowing(self):
        self.in_motion = False

    def set_direction(self, direction: str):
        if direction not in self.VALID_DIRECTIONS:
            raise InvalidDirectionException(f"Неверное направление: {direction}")
        self.direction = direction

    def read_status(self):
        return {
            "in_motion": self.in_motion,
            "direction": self.direction,
            "passengers": self.passengers.copy(),
            "capacity": self.capacity
        }

boat = RowBoat(2)

print(boat.read_status())