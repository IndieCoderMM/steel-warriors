import random
import arcade
from game.modules.player import Player
from game.modules.enemy import Enemy
from game.modules.explosion import Expolsion
from game.modules.map import Map
from game.settings import WIDTH, HEIGHT, TITLE, SCALE, PLAYER_SPEED


class Game(arcade.Window):
    def __init__(self, width: int, height: int, title: str):
        super().__init__(width, height, title)
        self.enemies_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.explosion_sprites = arcade.SpriteList()
        self.score_text = arcade.Text(
            'Score: ', 10, height - 50, color=arcade.color.AZURE, font_size=30, bold=True)
        self.game_over_text = arcade.Text(
            'Game Over!', width/2, height/2, font_size=50, color=arcade.color.AUBURN, bold=True, anchor_x="center", anchor_y="center")
        self.setup()
        self.map = Map()

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
        tanks = ['red', 'dark', 'sand', ]
        huge_tanks = ['darkLarge', 'huge', 'bigRed']
        if self.score > 0 and self.score % 3 == 0:
            tank = huge_tanks[random.randrange(
                0, len(huge_tanks))]
            hp = 30
            reload_time = 1
        else:
            tank = tanks[random.randrange(
                0, len(tanks))]
            hp = 10
            reload_time = 1.5

        x = random.randint(50, self.width - 50)
        enemy = Enemy(tank, x, self.height + 100, reload_time, hp)
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
        elif symbol == arcade.key.UP:
            self.player.change_y = PLAYER_SPEED / 2
        elif symbol == arcade.key.DOWN:
            self.player.change_y = -PLAYER_SPEED / 2
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = PLAYER_SPEED
        elif symbol == arcade.key.SPACE:
            self.player.fire()
        elif symbol == arcade.key.G:
            self.map.generate_new_map()

    def on_key_release(self, symbol: int, modifiers: int):
        if (symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT):
            self.player.change_x = 0
        elif (symbol == arcade.key.UP or symbol == arcade.key.DOWN):
            self.player.change_y = 0

    def on_update(self, delta_time: float):
        if self.paused:
            return

        self.all_sprites.update()

        for bullet in self.player.bullets_list:
            for enemy in self.enemies_list:
                if bullet.collides_with_sprite(enemy):
                    bullet.remove_from_sprite_lists()
                    enemy.hitpoint -= 10
                if enemy.hitpoint <= 0:
                    explosion = Expolsion(
                        'game/assets/explosion3.png', enemy.center_x, enemy.center_y, lifetime=0.25)
                    self.all_sprites.append(explosion)
                    enemy.remove_from_sprite_lists()
                    self.score += 1

        for enemy in self.enemies_list:
            if enemy.top < 0:
                self.game_over = True
                self.paused = True
            for bullet in enemy.bullets_list:
                if bullet.collides_with_sprite(self.player):
                    bullet.remove_from_sprite_lists()
                    self.player.health -= 20

        if self.player.collides_with_list(self.enemies_list) or self.player.health <= 0:
            explosion = Expolsion(
                'game/assets/explosion3.png', self.player.center_x, self.player.center_y, lifetime=0.25)
            self.all_sprites.append(explosion)
            self.game_over = True
            self.paused = True

        self.score_text.text = "Score: " + str(self.score)

    def on_draw(self):
        arcade.start_render()
        self.map.draw()
        self.player.bullets_list.draw()
        for enemy in self.enemies_list:
            enemy.bullets_list.draw()
        self.all_sprites.draw()
        self.explosion_sprites.draw()
        radius = 4
        hp = 0
        i = 0
        while (hp < self.player.health):
            hp += 20
            arcade.draw_circle_filled(
                self.player.left + i * (2*radius + radius), self.player.bottom - 2 * radius, radius=radius, color=arcade.color.BARBIE_PINK)
            i += 1

        self.score_text.draw()
        if self.game_over:
            self.game_over_text.draw()


def run():
    game = Game(WIDTH, HEIGHT, TITLE)
    game.run()
