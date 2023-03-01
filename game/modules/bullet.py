import arcade


class Bullet(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__("game/assets/bulletBlue1_outline.png", 2)
        self.center_x = x - self.width / 2
        self.center_y = y - self.height / 2
        self.velocity = (0, 500)
