from entities.physical_entity import PhysicalEntity
from entities.oval import Oval
from relative_position import RelativePosition
from part import Part


class Ear(PhysicalEntity):
    def __init__(self, parameters):
        super().__init__(parameters)

        self.parts.append(Part(entity=Oval(parameters),
                          relative_position=RelativePosition(left=0, top=0, right=1, bottom=1)))
