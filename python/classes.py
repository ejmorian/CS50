
class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False

        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)
people = ["Hermione", "Ron", "Harry", "Gini"]

for people in people:
    success = flight.add_passenger(people)
    if success:
        print(f"{people} booked a flight")
    else:
        print(f"flight is full, cannot book flight for {people}")
