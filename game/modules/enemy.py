import arcade
from game.modules.tank import Tank
from game.settings import SCALE, ENEMY_SPEED


class Enemy(Tank):
    def __init__(self, color, x, y):
        img_path = ':resources:/images/topdown_tanks/tank_' + color + '.png'
        super().__init__(img_path, SCALE, x, -1)
        self.top = y
        self.velocity = (0, -ENEMY_SPEED)
        arcade.schedule(self.fire, .5)
