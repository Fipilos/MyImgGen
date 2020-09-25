from copy import deepcopy

from create_entity import create_entities
from position.positioning import Positioning
from position.positions_from_words import get_rel_pos_dict
from position.position import Position
from entity_parameters import EntityParameters as EP


class LogicalWorld(object):
    def __init__(self, grammatical_world):
        self.entities = []
        self.positioning = None
        self._create_entities(grammatical_world)
        self._create_positioning(grammatical_world)
        self.current_group = None
        self._resize_entities()
        self._create_parts_of_entities()

    def __repr__(self):
        return str(self.__dict__)

    def _resize_entities(self):
        self._adapt_to_largest()

        for e in self.entities:
            e.resize()

    def _adapt_to_largest(self):
        divide_by_largest = dict()

        for c in ['x', 'y']:
            largest = max([e.size_multiplier['multiplier'][c] for e in self.entities])
            divide_by_largest[c] = 1 / largest

        for e in self.entities:
            e.multiply(multiplier=divide_by_largest)

    def print_positioned_entities(self):
        for e in self.entities:
            print(str(type(e)), e.parameters[EP.POSITION])

    def _create_entities(self, grammatical_world):
        for obj in grammatical_world.objects + grammatical_world.subjects:
            entities_group = create_entities(obj)
            if entities_group is not None:
                self.entities.append(entities_group)

    def _unzip_entities(self):
        entities = []

        for group in self.entities:
            entities.extend(group)

        self.entities = entities

    def _give_entities_their_positions(self, place_dict):
        for group in self.entities:
            self.current_group = group
            id_ = group[0].parameters[EP.ID]
            id_ = place_dict[id_]
            group_place = id_
            self._give_each_entity_from_group_its_position(group_place)

        self._unzip_entities()

    def _give_each_entity_from_group_its_position(self, place):
        #  todo use two dimensions
        positions = place.get_equal_parts(len(self.current_group))
        # print(f'positions from positioning: {positions}')

        for e_idx, p in enumerate(positions):
            self.current_group[e_idx].parameters[EP.POSITION] = p

    def _create_positioning(self, grammatical_world):
        subjects = grammatical_world.subjects
        attributes = grammatical_world.attributes
        rel_pos_dict = get_rel_pos_dict(subjects, attributes, grammatical_world.objects_pairs)
        objects = [e[0] for e in self.entities]
        self.positioning = Positioning(objects, rel_pos_dict)
        self.positioning.parse_positioning()
        place_dict = self.positioning.get_place_dict()
        self._give_entities_their_positions(place_dict)

    def _reset_dimensions_and_create_parts_of_single_entity(self, entity):
        width = entity.parameters[EP.POSITION].right - entity.parameters[EP.POSITION].left
        height = entity.parameters[EP.POSITION].bottom - entity.parameters[EP.POSITION].top

        if entity.parameters[EP.ASPECT_RATIO] not in {'fit', 'default'}:
            width, height = entity.get_dimensions_keeping_aspect_ratio(width, height)

        self.entities.append(entity)

        for p_idx, p in enumerate(deepcopy(entity.parts)):
            # print('!'*10, 'BEFORE PROCESS', type(entity), type(p.entity), self.entities)

            # print('processing', type(p.entity))
            new_entity = p.entity

            # print(f'new entity before: {new_entity}')

            left = entity.parameters[EP.POSITION].left + p.relative_position.left * width
            right = entity.parameters[EP.POSITION].left + p.relative_position.right * width
            top = entity.parameters[EP.POSITION].top + p.relative_position.top * height
            bottom = entity.parameters[EP.POSITION].top + p.relative_position.bottom * height

            # print('!'*10, 'POST PROCESS BEFORE POS', type(entity), type(p.entity), self.entities)

            # print('BEFORE!', p.entity)
            p.entity.parameters[EP.POSITION] = Position(left, top, right, bottom)
            # print('AFTER!', p.entity)

            # print('!'*10, 'POST PROCESS AFTER POS', type(entity), type(p.entity), self.entities)

            # print(f'entity of type {type(new_entity)} position {new_entity.parameters[EP.POSITION]}')
            # print('!'*10, 'POST PROCESS BEFORE APPEND', type(entity), type(p.entity), self.entities)

            # print('!'*10, 'POST PROCESS AFTER APPEND', type(entity), type(p.entity), self.entities)
            # print('sub', type(new_entity), new_entity.parameters[EP.COLOR])
            # print('sub (the same)', type(p.entity), p.entity.parameters[EP.COLOR])
            self._reset_dimensions_and_create_parts_of_single_entity(new_entity)

            # print('!'*10, type(entity), type(new_entity), self.entities)

    def _create_parts_of_entities(self):
        base_entities = deepcopy(self.entities)
        self.entities = []
        for e in base_entities:
            self._reset_dimensions_and_create_parts_of_single_entity(e)

    def _remove_all_parts_of_entities(self):
        for e in self.entities:
            e.parts = []
