import cv2

from figures.figure import Figure


class Ellipse(Figure):
    def draw(self, img):
        cv2.ellipse(img,
                    self.params['center'],
                    (int(round(0.5*self.params['width'])),
                          int(round(0.5*self.params['height']))),
                    0,
                    0,
                    360,
                    self.params['color'],
                    self.params['thickness']
                    )
