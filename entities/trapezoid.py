from entities.physical_entity import PhysicalEntity
from figures.polygon import Polygon


class Trapezoid(PhysicalEntity):
    def __init__(self, parameters, trapezoid_type, top_to_bottom):
        super().__init__(parameters)
        self.type = trapezoid_type
        self.top_to_bottom = top_to_bottom

    def _get_draw_parameters(self):
        params = super()._get_draw_parameters()
        pos = params['draw_position']

        if self.type == 'horizontal':
            if self.top_to_bottom > 1:
                parallels_diff = params['width'] * (1 - 1/self.top_to_bottom)
                params['vertices'] = [(pos.left, pos.top), (pos.right, pos.top),
                                      (pos.right - parallels_diff, pos.bottom), (pos.left + parallels_diff, pos.bottom)]
            else:
                parallels_diff = params['width'] * (1-self.top_to_bottom)
                params['vertices'] = [(pos.left + parallels_diff, pos.top), (pos.right - parallels_diff, pos.top),
                                      (pos.right, pos.bottom), (pos.left, pos.bottom)]

        return params

    def get_figure(self):
        params = self._get_draw_parameters()
        figure = Polygon(params=params)

        return figure
