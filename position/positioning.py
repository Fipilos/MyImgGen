import config as cfg
from location import Location
from position.position_connected_puzzle import PositionConnectedPuzzle
from position.position import Position
from entity_parameters import EntityParameters as EP


class Canvas(Position):
    def get_sub_canvas_from_location_enum(self, enum):
        if enum == Location.BOTTOM:
            sub_canvas = self.get_sub_canvas_from_location_bottom()
        elif enum == Location.TOP:
            sub_canvas = self.get_sub_canvas_from_location_top()

        return sub_canvas

    def get_sub_canvas_from_location_bottom(self):
        sub_self = Canvas(left=self.left, right=self.right, bottom=self.bottom,
                               top=(self.bottom + self.top) // 2)
        return sub_self

    def get_sub_canvas_from_location_top(self):
        sub_self = Canvas(left=self.left, right=self.right,
                               bottom=(self.bottom + self.top) // 2, top=self.top)
        return sub_self

    def get_equal_parts(self, cnt):
        """Use for plurals"""
        parts = []
        width = self.right - self.left

        for i in range(cnt):
            parts.append(Canvas(
                left=self.left + int(round(i/cnt * width)),
                right=self.left + int(round((i+1)/cnt * width)),
                top=self.top,
                bottom=self.bottom
            ))

        # print('parts', parts, self.right, self.left)
        return parts


class Positioning(object):
    def __init__(self, objects, rel_pos_dict, canvas=Canvas(0, 0, cfg.CANVAS_WIDTH, cfg.CANVAS_HEIGHT)):
        self.objects = objects
        self.canvas = canvas
        self.sub_positionings = []
        self.positions = dict()
        self.rel_pos_dict = rel_pos_dict
        self.place_dict = None
        self.pos_dict = None

    def __eq__(self, another):
        return self.canvas == another.canvas

    def __repr__(self):
        return str(self.__dict__)

    def _find_sub_positioning(self, sub_positioning):
        for i in self.sub_positionings:
            if sub_positioning == i:
                return i

        return None
        
    def _move_objects_to_sub_positionings(self):
        for obj in self.objects:
            if obj.location_list:
                location = obj.location_list.pop()
                sub_canvas = self.canvas.get_sub_canvas_from_location_enum(location)
                sub_positioning = Positioning([obj], self.rel_pos_dict, sub_canvas)  # todo only part of rel_pos_dict should be taken
                found_positioning = self._find_sub_positioning(sub_positioning)

                if found_positioning is None:
                    self.sub_positionings.append(sub_positioning)
                else:
                    found_positioning.objects.append(obj)

    def _create_place_dict(self):
        if len(self.objects) > 1:
            place_dict = dict()
            x_cnt = max(i.x for i in self.pos_dict.values()) + 1
            y_cnt = max(i.y for i in self.pos_dict.values()) + 1
            x_size = self.canvas.right - self.canvas.left
            y_size = self.canvas.bottom - self.canvas.top
            place_width = x_size // x_cnt
            place_height = y_size // y_cnt

            # todo handle places of different sizes
            for i in self.pos_dict:
                place_dict[i] = Canvas(
                    left=self.pos_dict[i].x * place_width,
                    right=(self.pos_dict[i].x + 1) * place_width,
                    top=self.pos_dict[i].y * place_height,
                    bottom=(self.pos_dict[i].y+1) * place_height)
        elif len(self.objects) == 1:
                    place_dict = {self.objects[0].parameters[EP.ID]: self.canvas}
        else:
                    place_dict = dict()

        self.place_dict = place_dict

    def parse_positioning(self):
        self._move_objects_to_sub_positionings()

        if self.rel_pos_dict:
            pos_puzzle = PositionConnectedPuzzle(rel_pos_dict=self.rel_pos_dict)
            self.pos_dict = pos_puzzle.get_positions()

        self._create_place_dict()

        for sp in self.sub_positionings:
            sp.parse_positioning()

    def get_place_dict(self):
        return self.place_dict
