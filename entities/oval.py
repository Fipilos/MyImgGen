from entity import Entity
from figures.ellipse import Ellipse


class Oval(Entity):
    def get_figure(self):
        params = self._get_draw_parameters()
        figure = Ellipse(params)

        return figure
