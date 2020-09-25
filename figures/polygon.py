import cv2
import numpy as np

from figures.figure import Figure


class Polygon(Figure):
    def draw(self, img):
        vertices = np.array([v for v in self.params['vertices']], np.int32)
        vertices.reshape((-1, 1, 2))
        cv2.polylines(img, [vertices], True, self.params['color'])
