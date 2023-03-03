import arcade
from game.modules.bullet import Bullet


class Tank(arcade.Sprite):
    def __init__(self, img_path, scale, x, direction=1):
        super().__init__(img_path, scale)
        self.center_x = x
        self.direction = direction
        self.bullets_list = arcade.SpriteList()

    def fire(self, delta_time: float = 0.0):
        bullet = Bullet(self.center_x, self.top, self.direction)
        self.bullets_list.append(bullet)

    def draw(self):
        super().draw()
        # ? Drawing bullets here does not work
        # self.bullets_list.draw()

    def update(self):
        super().update()
        self.bullets_list.update()
