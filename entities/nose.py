from entities.physical_entity import PhysicalEntity
from entities.triangle import Triangle
from entity_parameters import EntityParameters as EP
from part import Part
from relative_position import RelativePosition


class Nose(PhysicalEntity):
    def __init__(self, params):
        super().__init__(params)
        self.SUPPORTED_TYPES = {'human'}
        self._set_default_type_if_needed('human')
        chosen_type = self._get_chosen_type()

        if chosen_type == 'human':
            self.parts.append(Part(
                Triangle({EP.TYPE: 'human_nose', EP.ASPECT_RATIO: self.parameters[EP.ASPECT_RATIO]}),
                RelativePosition()))
        else:
            'TODO'
