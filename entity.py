from copy import deepcopy

import config as cfg
from modifiers import shape_config as shape_cfg
from position.position import Position
from entity_parameters import EntityParameters as EP
from hierarchy.supertypes import get_supertypes
from hierarchy.subtypes import get_subtype
from hierarchy.similarity import find_most_similar


class Entity(object):
    def __init__(self, parameters):
        self.color = None
        self.location_list = []
        self.parts = []
        self.parameters = deepcopy(parameters)
        self.size_multiplier = {'multiplier': {'x': 1.0, 'y': 1.0}, 'direction': {'x': 'left', 'y': 'bottom'}}

        self._set_defaults()

    def __repr__(self):
        return str(type(self)) + str(self.__dict__) # todo restore
        # return str(type(self)) + str(self.parameters[EP.POSITION] if EP.POSITION in self.parameters else 'no position') + str(self.parts)

    def _set_defaults(self):
        if EP.ASPECT_RATIO not in self.parameters:
            self.parameters[EP.ASPECT_RATIO] = 'default'  # 'default' (in contarty to 'fit') is weak i.e. it will be easily changed by e.g._change_default_aspect_ratio_to_value
        if EP.COLOR not in self.parameters:
            self.parameters[EP.COLOR] = cfg.LINE_COLOR

    def _set_default_type_if_needed(self, value):
        if EP.TYPE not in self.parameters:
            self.parameters[EP.TYPE] = value

    def _change_default_aspect_ratio_to_value(self, value):
        if self.parameters[EP.ASPECT_RATIO] == 'default':
            # print(f'changing {type(self)} aspect to {value}')
            self.parameters[EP.ASPECT_RATIO] = value

    def _get_chosen_type(self):
        chosen_type = get_subtype({self.parameters[EP.TYPE]}, self.SUPPORTED_TYPES)

        if chosen_type is None:
            chosen_type = get_supertypes(given_types={self.parameters[EP.TYPE]}, supported_types=self.SUPPORTED_TYPES)

        if chosen_type is not None:
            self.parameters[EP.TYPE] = chosen_type

        return chosen_type

    def get_dimensions_keeping_aspect_ratio(self, full_width, full_height):
        background_aspect_ratio = full_width / full_height

        if self.parameters[EP.ASPECT_RATIO] < background_aspect_ratio:
            height = full_height
            width = height * self.parameters[EP.ASPECT_RATIO]
            self.parameters[EP.POSITION].left += (full_width - width)/2
            self.parameters[EP.POSITION].right -= (full_width - width)/2
        else:
            width = full_width
            height = width / self.parameters[EP.ASPECT_RATIO]
            self.parameters[EP.POSITION].top += (full_height - height)/2
            self.parameters[EP.POSITION].bottom -= (full_height - height)/2

        return width, height

    def _get_center(self):
        center = (int(round((self.parameters[EP.POSITION].left + self.parameters[EP.POSITION].right) / 2)),
         int(round((self.parameters[EP.POSITION].top + self.parameters[EP.POSITION].bottom) / 2)))

        return center

    def _get_draw_parameters(self):
        params = dict()
        width = self.parameters[EP.POSITION].right - self.parameters[EP.POSITION].left
        height = self.parameters[EP.POSITION].bottom - self.parameters[EP.POSITION].top
        params['center'] = self._get_center()
        params['color'] = cfg.COLOR[self.parameters[EP.COLOR]if EP.COLOR in self.parameters else cfg.LINE_COLOR]
        params['thickness'] = self.parameters[EP.LINE_THICKNESS] if EP.LINE_THICKNESS in self.parameters else cfg.LINE_THICKNESS

        params['draw_position'] = Position(left=params['center'][0] - width/2, right=params['center'][0] + width/2,
                                      top=params['center'][1] - height/2, bottom=params['center'][1] + height/2)

        params['width'] = width
        params['height'] = height

        return params

    def get_figure(self):
        return None

    def apply_determiners(self, determiners):
        pass  # todo

    def apply_modifiers(self, modifiers):
        for modifier in modifiers:
            self.apply_modifier(modifier)

    def resize(self):
        for p in self.parts:
            p.relative_position.multiply(self.size_multiplier['multiplier'], self.size_multiplier['direction'])

    def apply_modifier(self, modifier):
        modifier = modifier.root.lemma_

        if modifier not in cfg.ALL_ADJ:
            modifier = find_most_similar(modifier, 'adj')

        modifier_type = self._get_modifier_type(modifier)

        if modifier_type == 'color':
            self.apply_color_modifier(modifier)
        elif modifier_type == 'size':
            self._apply_size_modifier(modifier)
        else:
            self.parameters[EP.ATTRIBUTES].add(modifier)

    def apply_color_modifier(self, modifier):
        self.parameters[EP.COLOR] = modifier

        for p in self.parts:
            p.entity.apply_color_modifier(modifier)

    def _apply_size_modifier(self, modifier):
        multiplier = shape_cfg.SIZE_MULTIPLIER[modifier]
        self.multiply(multiplier)

    def multiply(self, multiplier):
        self.size_multiplier['multiplier']['x'] *= multiplier['x']
        self.size_multiplier['multiplier']['y'] *= multiplier['y']

    @staticmethod
    def _get_modifier_type(modifier):
        for param_type in cfg.ADJ:
            if modifier in cfg.ADJ[param_type]:
                modifier_type = param_type
                break

        return modifier_type

    def apply_mod_verb(self, mod_verb):
        base_verb = mod_verb.verb.lemma_

        if base_verb == 'stand':
            self._apply_stand_mod_verb()
        elif base_verb in ['be', 'remain']:
            self._apply_be_mod_verb(mod_verb)
        else:
            print('Unknown action verb: {}'.format(mod_verb))

    def _apply_stand_mod_verb(self):
        'todo'

    def _apply_be_mod_verb(self, mod_verb):
        for adj_comp in mod_verb.adj_complements:
            self.apply_modifier(adj_comp)
