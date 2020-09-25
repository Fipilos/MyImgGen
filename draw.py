import cv2
import numpy as np

import config as cfg


class Draw(object):
    def __init__(self, logical_world):
        self.img = np.ones((cfg.CANVAS_HEIGHT, cfg.CANVAS_WIDTH, 3), np.uint8)
        self.logical_world = logical_world

    def draw(self, save, display):
        self.img[:] = cfg.CANVAS_COLOR

        for entity in self.logical_world.entities:
            self._draw_entity(entity)

        if save:
            cv2.imwrite(cfg.OUTPUT_IMG_PATH, self.img)

        if display:
            WindowName = "Main View"

            cv2.imshow(WindowName, self.img)

            cv2.waitKey(0)
            cv2.destroyAllWindows

        return self.img

    def _draw_entity(self, entity):
        figure = entity.get_figure()
        # print(figure)

        if figure is not None:
            figure.draw(self.img)
