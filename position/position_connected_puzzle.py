"""
Assume rel pos dict gives, for each object id's pair, their relative position
e.g. {(0,1):MoveVector(x=1,y=-1)}
"""
import random

from position.move_vector import MoveVector
from position.positions_from_words import get_relative_position_for_pos_phrase


class PositionConnectedPuzzle(object):
    def __init__(self, rel_pos_dict):
        """
        values of both dictionaries are MoveVector instances
        """
        self.rel_pos_dict = rel_pos_dict  # pairs of id's
        self.position_dict = dict()  # id's

    def get_positions(self):
        self._position_with_negative_values()
        self._reset()

        return self.position_dict

    def _reset(self):
        min_x = min(v.x for v in self.position_dict.values())
        min_y = min(v.y for v in self.position_dict.values())

        for id_ in self.position_dict:
            self.position_dict[id_] += MoveVector(-min_x, -min_y)

    def _position_single_id(self, id_):
        difficult_pairs = []

        for pair in self.rel_pos_dict:
            if pair[0] == id_ or pair[1] == id_:
                if type(self.rel_pos_dict[pair]) == MoveVector:
                    self._position_simple_pair(pair)
                else:
                    difficult_pairs.append(pair)

        for pair in difficult_pairs:
            self._position_ambiguous_pair(pair)

    def _position_simple_pair(self, pair):
        if pair[0] in self.position_dict and pair[1] in self.position_dict:
            pass  # already done
        elif pair[0] in self.position_dict and pair[1] not in self.position_dict:
            self.position_dict[pair[1]] = self.position_dict[pair[0]] + self.rel_pos_dict[pair]
            self._position_single_id(pair[1])
        elif pair[1] in self.position_dict and pair[0] not in self.position_dict:
            self.position_dict[pair[0]] = self.position_dict[pair[1]] + self.rel_pos_dict[pair]
            self._position_single_id(pair[0])
        else:
            raise AssertionError('should not have happened!')

    def _position_ambiguous_pair(self, pair):
        move_list = get_relative_position_for_pos_phrase(self.rel_pos_dict[pair])
        move_vector = random.choice(move_list)
        self.rel_pos_dict[pair] = move_vector
        self._position_simple_pair(pair)

    def _position_with_negative_values(self):
        """
        Assuming there are no contradictions...
        """
        start_id = list(self.rel_pos_dict.keys())[0][0]
        self.position_dict[start_id] = MoveVector(0, 0)
        self._position_single_id(start_id)


