import arcade
from game.settings import BULLET_SPEED, HEIGHT


class Bullet(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("game/assets/bulletBlue1_outline.png", 2)
        self.center_x = x
        self.center_y = y
        self.velocity = (0, BULLET_SPEED)

    def update(self):
        super().update()
        if self.top > HEIGHT:
            self.remove_from_sprite_lists()
