from abc import ABC, abstractmethod


# Product
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


# All products must follow the same interface.
# Product Truck
class Truck(Transport):
    def deliver(self):
        return "Deliver with Truck"


# Product Truck
class Ship(Transport):
    def deliver(self):
        return "Deliver with Ship"


# Product Truck
class Airplane(Transport):
    def deliver(self):
        return "Deliver with Plane"


# Factory or Creator
class Logistic(ABC):
    @abstractmethod  # Factory Method
    def create_transport(self) -> Transport:
        pass

    def some_operation(self) -> str:
        transport = self.create_transport()
        result = f"Creator: The same creator's code has just worked with {transport.deliver()}"
        return result


# Concrete creator of Product Truck
class RoadLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Truck()


# Concrete creator of Product Ship
class SeaLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Ship()


class AirLogistic(Logistic):
    def create_transport(self) -> Transport:
        return Airplane()


def client_code(factory: Logistic) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(
        f"Client: I'm not aware of the creator's class, but it still works.\n"
        f"{factory.some_operation()}",
        end="",
    )


if __name__ == "__main__":
    print("App: Launched with the ConcreteCreator1.")
    client_code(RoadLogistic())
    print("\n")

    print("App: Launched with the ConcreteCreator2.")
    client_code(SeaLogistic())

    print("App: Launched with the ConcreteCreator3.")
    client_code(AirLogistic())
