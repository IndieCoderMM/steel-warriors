import arcade
from game.modules.bullet import Bullet
from game.settings import WIDTH


class Player(arcade.Sprite):
    def __init__(self, img_path, scale, x):
        super().__init__(img_path, scale)
        self.center_x = x
        self.center_y = self.height
        self.bullets_list = arcade.SpriteList()

    def fire(self):
        bullet = Bullet(self.center_x, self.top)
        self.bullets_list.append(bullet)
        self.reloading = True

    def update(self):
        super().update()
        self.bullets_list.update()
        if self.right > WIDTH:
            self.right = WIDTH
        if self.left < 0:
            self.left = 0
