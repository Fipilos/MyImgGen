from entities.physical_entity import PhysicalEntity
from figures.polygon import Polygon
from entity_parameters import EntityParameters as EP


class Triangle(PhysicalEntity):
    def _get_draw_parameters(self):
        params = super()._get_draw_parameters()

        if self.parameters[EP.TYPE] == 'human_nose':
            params['vertices'] = [((params['draw_position'].left+params['draw_position'].right)/2, params['draw_position'].top),
                              (params['draw_position'].left, params['draw_position'].bottom),
                              (params['draw_position'].right, params['draw_position'].bottom)]

        return params

    def get_figure(self):
        params = self._get_draw_parameters()
        figure = Polygon(params=params)

        return figure
