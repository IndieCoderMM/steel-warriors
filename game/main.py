import random
import arcade
from game.modules.player import Player
from game.modules.enemy import Enemy
from game.settings import WIDTH, HEIGHT, TITLE, SCALE, PLAYER_SPEED


class Game(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)
        self.enemies_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.score_text = arcade.Text('Score: ', 10, height - 50, font_size=30)
        self.game_over_text = arcade.Text(
            'Game Over!', width/2, height/2, font_size=50, anchor_x="center", anchor_y="center")
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.AMAZON)
        self.enemies_list.clear()
        self.all_sprites.clear()
        self.player = Player('game/assets/tank_blue.png',
                             SCALE, self.width / 2)
        self.all_sprites.append(self.player)
        self.player.bullets_list.clear()
        self.score = 0
        self.paused = False
        self.game_over = False
        arcade.schedule(self.add_enemy, 2)

    def add_enemy(self, delta_time: float):
        colors = ['red', 'dark']
        x = random.randint(50, self.width - 50)
        enemy = Enemy(colors[random.randrange(
            0, len(colors))], x, self.height + 100)
        self.enemies_list.append(enemy)
        self.all_sprites.append(enemy)

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

        self.all_sprites.update()

        for bullet in self.player.bullets_list:
            for enemy in self.enemies_list:
                if bullet.collides_with_sprite(enemy):
                    bullet.remove_from_sprite_lists()
                    enemy.remove_from_sprite_lists()
                    self.score += 1

        for enemy in self.enemies_list:
            if enemy.top < 0:
                self.game_over = True
                self.paused = True

        if self.player.collides_with_list(self.enemies_list):
            self.game_over = True
            self.paused = True

        self.score_text.text = "Score: " + str(self.score)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites.draw()
        self.player.bullets_list.draw()
        self.score_text.draw()
        if self.game_over:
            self.game_over_text.draw()


def run():
    game = Game(WIDTH, HEIGHT, TITLE)
    game.run()
