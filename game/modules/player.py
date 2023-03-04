import arcade
from game.modules.tank import Tank
from game.settings import HEIGHT, WIDTH


class Player(Tank):
    def __init__(self, img_path, scale, x, health=100):
        super().__init__(img_path, scale, x, flip_y=True)
        self.center_y = self.height
        self.health = health
        self.max_health = health

    def draw(self):
        super().draw()
        # radius = 2
        # for i in range(10):
        #     print(i)
        #     arcade.draw_circle_filled(
        #         self.left + i * radius, self.bottom + 2*radius, radius=radius, color=arcade.color.CAPRI)

    def update(self):
        super().update()
        if self.right > WIDTH:
            self.right = WIDTH
        if self.left < 0:
            self.left = 0
        if self.top > HEIGHT:
            self.top = HEIGHT
        if self.bottom < 0:
            self.bottom = 0
