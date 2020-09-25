"""
Based on https://thevirtualinstructor.com/facialproportions.html
"""

import math

from entities.physical_entity import PhysicalEntity
from entities.oval import Oval
from entities.eye import Eye
from entities.nose import Nose
from entities.mouth import Mouth
from entities.ear import Ear
from part import Part
from relative_position import RelativePosition
from entity_parameters import EntityParameters as EP


class Face(PhysicalEntity):
    ASPECT_RATIO = {'human': 2*math.sqrt(2)/(2+math.sqrt(2)),
                    'cat': 0.66}

    def __init__(self, parameters):
        super().__init__(parameters)
        self.SUPPORTED_TYPES = {'human', 'cat'}
        self._set_default_type_if_needed('human')
        chosen_type = self._get_chosen_type()
        self._change_default_aspect_ratio_to_value(Face.ASPECT_RATIO[chosen_type])

        if chosen_type is None:
            print('{} face not implemented'.format(self.parameters[EP.TYPE]))
        elif chosen_type in ['human', 'cat']:  # TODO move 'cat' into separate branch
            self.parameters[EP.TYPE] = 'human'
            brow_line = (math.sqrt(2))/(2+math.sqrt(2))
            nose_line = (1+math.sqrt(2))/(2+math.sqrt(2))
            eyes_bottom_line = brow_line + 0.2 / Eye.ASPECT_RATIO[self.parameters[EP.TYPE]]
            mouth_height = 0.12
            mouth_center_height = (1.5+math.sqrt(2))/(2+math.sqrt(2))
            self.parts.append(Part(entity=Oval({EP.ASPECT_RATIO: 'fit'}),
                                   relative_position=RelativePosition(
                left=0.1, top=0, right=0.9, bottom=1
            )))
            self.parts.append(Part(entity=Eye({EP.SHAPE: Eye.STANDARD_SHAPE, EP.TYPE: self.parameters[EP.TYPE]}), relative_position=RelativePosition(
                left=0.2, top=brow_line, right=0.4,
                bottom=eyes_bottom_line
            )))
            self.parts.append(Part(entity=Eye({EP.SHAPE: Eye.STANDARD_SHAPE, EP.TYPE: self.parameters[EP.TYPE]}), relative_position=RelativePosition(
                left=0.6, top=brow_line, right=0.8,
                bottom=eyes_bottom_line
            )))
            self.parts.append(Part(entity=Nose({EP.TYPE: self.parameters[EP.TYPE]}), relative_position=RelativePosition(
                left=0.4, right=0.6, top=eyes_bottom_line, bottom=nose_line
            )))
            self.parts.append(Part(entity=Mouth({EP.TYPE: self.parameters[EP.TYPE]}), relative_position=RelativePosition(
                left=0.32, right=0.68, top=mouth_center_height-mouth_height/2, bottom=mouth_center_height+mouth_height/2
            )))
            self.parts.append(Part(entity=Ear({EP.TYPE: self.parameters[EP.TYPE]}), relative_position=RelativePosition(
                left=0, right=0.1, top=brow_line, bottom=nose_line
            )))
            self.parts.append(Part(entity=Ear({EP.TYPE: self.parameters[EP.TYPE]}), relative_position=RelativePosition(
                left=0.9, right=1.0, top=brow_line, bottom=nose_line
            )))
