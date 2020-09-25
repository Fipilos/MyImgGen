"""
Proportions based on https://www.thedrawingsource.com/figure-drawing-proportions.html
"""

from entities.physical_entity import PhysicalEntity
from part import Part
from relative_position import RelativePosition
from entities.head import Head
from entities.torso import Torso
from entities.leg import Leg
from entities.arm import Arm
from entity_parameters import EntityParameters as EP


class Woman(PhysicalEntity):
    def __init__(self, parameters):
        parameters[EP.TYPE] = 'woman'
        super().__init__(parameters)
        self._change_default_aspect_ratio_to_value(0.7)

        self.parts.append(Part(Head(self.parameters), relative_position=RelativePosition(bottom=1/7.5, left=0.38, right=0.62)))
        self.parts.append(Part(Torso(self.parameters), relative_position=RelativePosition(left=0.2, right=0.8, top=1/7.5, bottom=4/7.5)))
        self.add_part(Leg, left=0.38, right=0.43, top=4/7.5)
        self.add_part(Leg, left=0.58, right=0.63, top=4/7.5)
        self.add_part(Arm, left=0.4, right=0.41, top=1/7.5, bottom=4/7.5)
        self.add_part(Arm, left=0.57, right=0.6, top=1/7.5, bottom=4/7.5)
