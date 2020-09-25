from entities.face import Face
from entities.hair import Hair
from entities.physical_entity import PhysicalEntity
from part import Part
from relative_position import RelativePosition
from entity_parameters import EntityParameters as EP


class Head(PhysicalEntity):

    def __init__(self, parameters):
        super().__init__(parameters)
        self.SUPPORTED_TYPES = {'man', 'woman', 'cat'}
        self._set_default_type_if_needed('human')
        chosen_type = self._get_chosen_type()

        face_params = self.parameters
        face_params[EP.ASPECT_RATIO] = 'fit'

        if chosen_type is None:
            print('{} head type not implemented!'.format(self.parameters[EP.TYPE]))
        elif chosen_type == 'man':
            self.parts.append(Part(entity=Face(face_params),
                                   relative_position=RelativePosition(top=0.05)))
            self.parts.append(Part(entity=Hair(self.parameters),
                                   relative_position=RelativePosition(top=0.0, bottom=0.35, left=0.1, right=0.9)))
        elif chosen_type == 'woman':
            self.parts.append(Part(entity=Face(face_params),
                                   relative_position=RelativePosition(top=0.05, bottom=0.9)))
            self.parts.append(Part(entity=Hair(self.parameters),
                                   relative_position=RelativePosition()))
        elif chosen_type == 'cat':
            self.parts.append(Part(entity=Face(face_params)))
