import arcade
from game.modules.tank import Tank
from game.settings import SCALE, ENEMY_SPEED


class Enemy(Tank):
    def __init__(self, color, x, y, reload_time, hitpoint=10):
        img_path = 'game/assets/tank_' + color + '.png'
        super().__init__(img_path, SCALE, x, -1)
        self.top = y
        self.velocity = (0, -ENEMY_SPEED)
        self.reload_time = reload_time
        self.time_elapsed = 0.0
        self.hitpoint = hitpoint

    def update(self):
        super().update()
        self.time_elapsed += 1 / 60
        if self.time_elapsed > self.reload_time:
            self.fire()
            self.time_elapsed = 0.0
