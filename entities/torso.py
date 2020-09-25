from entities.physical_entity import PhysicalEntity
from entities.trapezoid import Trapezoid
from entities.oval import Oval
from relative_position import RelativePosition
from entity_parameters import EntityParameters as EP
from part import Part


class Torso(PhysicalEntity):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.SUPPORTED_TYPES = {'man', 'woman', 'cat'}
        self._set_default_type_if_needed('human')
        chosen_type = self._get_chosen_type()

        if chosen_type is None:
            print('Torso of type {} not implemented!'.format(self.parameters[EP.TYPE]))
        elif chosen_type == 'man':
            self.parts.append(Part(Trapezoid(self.parameters, trapezoid_type='horizontal', top_to_bottom=1.3),
                                   RelativePosition()))
        elif chosen_type == 'woman':
            self.parts.append(Part(Trapezoid(self.parameters, trapezoid_type='horizontal', top_to_bottom=0.7),
                              RelativePosition()))
        elif chosen_type == 'cat':
            self.parts.append(Part(Oval(self.parameters)))