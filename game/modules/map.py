from arcade import Sprite, SpriteList
from copy import deepcopy
from game.settings import WIDTH, HEIGHT, TILES_DATA
from game.modules.wave_func import WaveFunction
from game.modules.tile import Tile


class Map:
    def __init__(self):
        self.tiles: list[Tile] = []
        self.grid = []
        self.tilemap = SpriteList()
        self.initTiles()
        self.wfc = WaveFunction(
            int(WIDTH/self.tiles[0].width), int(HEIGHT/self.tiles[0].height), self.tiles)
        self.generate_new_map()

    def generate_new_map(self):
        tilesize = self.tiles[0].width
        total_rows = int(HEIGHT / tilesize)
        total_cols = int(WIDTH/tilesize)
        self.tilemap.clear()
        self.wfc.generate_new_grid()

        for r in range(total_rows+1):
            for c in range(total_cols+1):
                # * Get i from wave function
                i = self.wfc.get_cell_at(c, r).tile_index
                # i = 7
                tile = deepcopy(self.tiles[i])
                tile.bottom = r * tilesize
                tile.left = c * tilesize
                self.tilemap.append(tile)

    def draw(self):
        self.tilemap.draw()

    def initTiles(self):
        path = 'game/assets/map/'
        # Grass
        tile1 = Tile(path+"0.png", TILES_DATA[0])
        tile2 = Tile(path+"1.png", TILES_DATA[1])
        tile3 = Tile(path+"2.png", TILES_DATA[2])
        tile4 = Tile(path+"3.png", TILES_DATA[3])
        tile5 = tile2.rotate(1)
        tile6 = tile2.rotate(2)
        tile7 = tile2.rotate(3)
        tile8 = tile3.rotate(3)
        tile9 = tile1.rotate(1)
        # Sand
        tile10 = Tile(path+"4.png", TILES_DATA[4])
        tile11 = Tile(path+"5.png", TILES_DATA[5])
        tile12 = Tile(path+"6.png", TILES_DATA[6])
        tile13 = Tile(path+"7.png", TILES_DATA[7])
        tile14 = Tile(path+"8.png", TILES_DATA[8])
        tile15 = tile11.rotate(1)
        tile16 = tile11.rotate(2)
        tile17 = tile11.rotate(3)
        tile18 = tile12.rotate(3)
        tile19 = tile13.rotate(1)
        tile20 = tile13.rotate(2)
        tile21 = tile13.rotate(3)
        tile22 = Tile(path+'9.png', TILES_DATA[9])
        tile23 = tile22.rotate(1)
        tile24 = tile22.rotate(2)
        tile25 = tile22.rotate(3)
        self.tiles.append(tile1)
        self.tiles.append(tile2)
        self.tiles.append(tile3)
        self.tiles.append(tile4)
        self.tiles.append(tile5)
        self.tiles.append(tile6)
        self.tiles.append(tile7)
        self.tiles.append(tile8)
        self.tiles.append(tile9)
        self.tiles.append(tile10)
        self.tiles.append(tile11)
        self.tiles.append(tile12)
        self.tiles.append(tile13)
        self.tiles.append(tile14)
        self.tiles.append(tile15)
        self.tiles.append(tile16)
        self.tiles.append(tile17)
        self.tiles.append(tile18)
        self.tiles.append(tile19)
        self.tiles.append(tile20)
        self.tiles.append(tile21)
        self.tiles.append(tile22)
        self.tiles.append(tile23)
        self.tiles.append(tile24)
        self.tiles.append(tile25)

        for tile in self.tiles:
            tile.analyze(self.tiles)
