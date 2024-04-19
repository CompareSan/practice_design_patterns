from typing import Any, Protocol


class ITarget(Protocol):
    def request(self) -> None: ...


class Target:
    def request(self) -> None:
        print("Compatible Interface")


class Adaptee:
    def specific_request(self) -> None:
        print("Incompatible Interface")


class Adapter:
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> None:
        self.adaptee.specific_request()
        print("Now is compatible Interface")


def client_code(target: ITarget):
    target.request()


if __name__ == "__main__":
    compatible_target = Target()
    client_code(compatible_target)

    try:
        incompatible_target = Adaptee()
        client_code(incompatible_target)

    except AttributeError:
        make_compatible_target = Adapter(incompatible_target)
        client_code(make_compatible_target)
