"""Foundamentals of OOP"""

from dataclasses import dataclass


@dataclass
class Spaceship:
    """Class for modeling a fictional Spaceship"""

    # Class attribute
    tractor_beam = "off"

    # Instance variables
    name: str
    kind: str
    speed: float = 0.0

    # Instance method
    def warp(self, warp: float) -> None:
        """print warp status

        Parameters
        ----------
        warp : float
            by how much to warp the ship
        """
        self.speed = warp
        print(f"Warp {warp}, engage!d")

    def tractor(self):
        """print tractor status"""
        if self.tractor_beam == "off":
            self.tractor_beam = "on"
            print("Tractor beam on.")
        else:
            self.tractor_beam = "off"
            print("Tractor beam off")


# Create an instance of the Spaceship class (i.e. "instantiate")
ship = Spaceship("Mockingbird", "rescue frigate")
ship.tractor()
print(ship.tractor_beam)
