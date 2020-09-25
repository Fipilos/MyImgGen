from entities.physical_entity import PhysicalEntity
from entities.oval import Oval
from relative_position import RelativePosition
from entity_parameters import EntityParameters as EP
from hierarchy.supertypes import get_supertypes
from part import Part


class Eye(PhysicalEntity):
    STANDARD_SHAPE = 'standard'
    ASPECT_RATIO = {'human': 5/3}

    def __init__(self, parameters):
        super().__init__(parameters)
        self.SUPPORTED_TYPES = {'human'}
        self._set_default_type_if_needed('human')
        chosen_type = self._get_chosen_type()

        if chosen_type == 'human':
            self.parts.append(Part(entity=Oval({EP.ASPECT_RATIO: Eye.ASPECT_RATIO['human']}),
                              relative_position=RelativePosition(left=0, top=0, right=1, bottom=1)))
            self.parts.append(Part(entity=Oval({EP.ASPECT_RATIO: 1.0}),
                              relative_position=RelativePosition(top=0, bottom=1, left=0.25, right=0.75)))
