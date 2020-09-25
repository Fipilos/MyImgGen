from entities.physical_entity import PhysicalEntity
from entities.oval import Oval
from part import Part
from relative_position import RelativePosition
from entity_parameters import EntityParameters as EP


class Hair(PhysicalEntity):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.SUPPORTED_TYPES = {'man', 'woman'}
        self._set_default_type_if_needed('human')
        chosen_type = self._get_chosen_type()

        if chosen_type is None:
            print('{} hair type not implemented!'.format(self.parameters[EP.TYPE]))
        elif chosen_type == 'man':
            self.parts.append(Part(entity=Oval({EP.LINE_THICKNESS: -1, EP.COLOR: self.parameters[EP.COLOR]}),
                              relative_position=RelativePosition(left=0.0, right=1.0, top=0.0, bottom=0.8)))
            self.parts.append(Part(entity=Oval({EP.LINE_THICKNESS: -1, EP.COLOR: self.parameters[EP.COLOR]}),
                              relative_position=RelativePosition(left=0.0, right=0.1, top=0.0, bottom=1.0)))
            self.parts.append(Part(entity=Oval({EP.LINE_THICKNESS: -1, EP.COLOR: self.parameters[EP.COLOR]}),
                              relative_position=RelativePosition(left=0.9, right=1.0, top=0.0, bottom=1.0)))
        elif chosen_type == 'woman':
            self.parts.append(Part(entity=Oval({EP.LINE_THICKNESS: -1, EP.COLOR: self.parameters[EP.COLOR]}),
                              relative_position=RelativePosition(left=0.0, right=1.0, top=0.0, bottom=0.2)))
            self.parts.append(Part(entity=Oval({EP.LINE_THICKNESS: -1, EP.COLOR: self.parameters[EP.COLOR]}),
                              relative_position=RelativePosition(left=0.0, right=0.1, top=0.0, bottom=1.0)))
            self.parts.append(Part(entity=Oval({EP.LINE_THICKNESS: -1, EP.COLOR: self.parameters[EP.COLOR]}),
                              relative_position=RelativePosition(left=0.9, right=1.0, top=0.0, bottom=1.0)))
