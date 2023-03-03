from game.modules.tank import Tank
from game.settings import WIDTH


class Player(Tank):
    def __init__(self, img_path, scale, x):
        super().__init__(img_path, scale, x, flip_y=True)
        self.center_y = self.height

    def update(self):
        super().update()
        if self.right > WIDTH:
            self.right = WIDTH
        if self.left < 0:
            self.left = 0
