from entities.physical_entity import PhysicalEntity
from part import Part
from relative_position import RelativePosition
from entities.head import Head
from entities.torso import Torso
from entities.leg import Leg
from entities.tail import Tail
from entity_parameters import EntityParameters as EP


class Cat(PhysicalEntity):
    def __init__(self, parameters):
        parameters[EP.TYPE] = 'cat'
        super().__init__(parameters)
        self._change_default_aspect_ratio_to_value(1.7)

        self.add_part(Head, bottom=0.41, left=0.73)
        self.add_part(Torso, left=0.2, right=0.8, top=0.17, bottom=0.65)
        self.add_part(Leg, left=0.2, right=0.3, top=0.5)
        self.add_part(Leg, left=0.4, right=0.5, top=0.5)
        self.add_part(Leg, left=0.6, right=0.7, top=0.5)
        self.add_part(Leg, left=0.72, right=0.82, top=0.5)
        self.add_part(Tail, right=0.3, top=0.17, bottom=0.35)