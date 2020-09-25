from entities.physical_entity import PhysicalEntity
from entities.oval import Oval
from entity_parameters import EntityParameters as EP
from relative_position import RelativePosition
from part import Part


class Tail(PhysicalEntity):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.SUPPORTED_TYPES = {'cat'}
        self._set_default_type_if_needed('cat')
        chosen_type = self._get_chosen_type()

        if chosen_type is None:
            print('tails of {} not implemented!'.format(self.parameters[EP.TYPE]))
        elif chosen_type == 'cat':
            self.parts.append(Part(entity=Oval(self.parameters), relative_position=RelativePosition()))