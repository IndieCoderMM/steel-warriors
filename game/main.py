import arcade
from game.modules.player import Player

WIDTH = 800
HEIGHT = 600
TITLE = "STEEL WARRIORS"
SCALING = 1.5
PLAYER_SPEED = 100


class Game(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)
        self.enemies_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.paused = False
        self.game_over = False
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.player = Player('game/assets/tank_blue.png',
                             SCALING, self.width / 2)
        self.all_sprites.append(self.player)
        self.paused = False
        self.game_over = False

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.Q:
            arcade.close_window()
        elif symbol == arcade.key.R:
            if self.game_over:
                self.setup()
        elif symbol == arcade.key.P:
            self.paused = not self.paused
        elif symbol == arcade.key.LEFT:
            self.player.change_x = -PLAYER_SPEED
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
        elif symbol == arcade.key.SPACE:
            self.player.fire()

    def on_key_release(self, symbol: int, modifiers: int):
        if (symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT):
            self.player.change_x = 0

    def on_update(self, delta_time: float):
        if self.paused:
            return

        for sprite in self.all_sprites:
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )

        for bullet in self.player.bullets_list:
            bullet.center_y = int(
                bullet.center_y + bullet.change_y * delta_time)

        if self.player.collides_with_list(self.enemies_list):
            self.game_over = True
            self.paused = True

        if self.player.right > self.width:
            self.player.right = self.width
        if self.player.left < 0:
            self.player.left = 0

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()
        self.player.bullets_list.draw()


def run():
    game = Game(WIDTH, HEIGHT, TITLE)
    game.run()
