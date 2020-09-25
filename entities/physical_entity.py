from copy import deepcopy

from entity import Entity
from part import Part
from relative_position import RelativePosition
from entity_parameters import EntityParameters as EP


class PhysicalEntity(Entity):
    def add_part(self, part_type, top=0.0, bottom=1.0, left=0.0, right=1.0, aspect_ratio='default'):
        parameters = deepcopy(self.parameters)
        parameters[EP.ASPECT_RATIO] = aspect_ratio
        self.parts.append(Part(entity=part_type(parameters=parameters),
                               relative_position=RelativePosition(left=left, right=right, top=top, bottom=bottom)))
