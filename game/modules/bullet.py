import arcade
from game.settings import BULLET_SPEED, HEIGHT


class Bullet(arcade.Sprite):
    def __init__(self, x, y, direction):
        img_path = "game/assets/shotLarge.png"
        super().__init__(img_path, 1, flipped_vertically=direction == -1)
        self.center_x = x
        self.top = y
        self.direction = direction
        self.velocity = (0, BULLET_SPEED * self.direction)

    def update(self):
        super().update()
        if self.direction > 0 and self.top > HEIGHT:
            self.remove_from_sprite_lists()
        elif self.direction < 0 and self.bottom < 0:
            self.remove_from_sprite_lists()
