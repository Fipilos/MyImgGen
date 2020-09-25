from entities.physical_entity import PhysicalEntity
from entities.oval import Oval


class Mouth(PhysicalEntity):
    def __init__(self, parameters):
        super().__init__(parameters)

        self.add_part(Oval)
