import arcade
from game.settings import SCALE, HEIGHT, ENEMY_SPEED


class Enemy(arcade.Sprite):
    def __init__(self, color, x, y):
        img_path = ':resources:/images/topdown_tanks/tank_' + color + '.png'
        super().__init__(img_path, SCALE)
        self.center_x = x
        self.top = y
        self.velocity = (0, -ENEMY_SPEED)
