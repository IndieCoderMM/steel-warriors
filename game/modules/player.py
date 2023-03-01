import arcade
from game.modules.bullet import Bullet


class Player(arcade.Sprite):
    def __init__(self, img_path, scale, x):
        super().__init__(img_path, scale)
        self.center_x = x - self.width / 2
        self.center_y = self.height
        self.bullets_list = arcade.SpriteList()

    def fire(self):
        bullet = Bullet(self.center_x, self.top)
        self.bullets_list.append(bullet)
