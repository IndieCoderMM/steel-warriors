from arcade import Sprite


class Tile(Sprite):
    def __init__(self, img_path, edges, weight=1, angle=0):
        super().__init__(img_path, angle=angle)
        self.img_path = img_path
        self.angle = angle
        self.edges = edges
        self.weight = weight
        self.top_neighbors = []
        self.right_neighbors = []
        self.bot_neighbors = []
        self.left_neighbors = []

    def analyze(self, tiles):
        for i in range(len(tiles)):
            tile = tiles[i]
            if self._is_match(self.edges[0], tile.edges[2]):
                self.top_neighbors.append(i)
            if self._is_match(self.edges[1], tile.edges[3]):
                self.right_neighbors.append(i)
            if self._is_match(self.edges[2], tile.edges[0]):
                self.bot_neighbors.append(i)
            if self._is_match(self.edges[3], tile.edges[1]):
                self.left_neighbors.append(i)

    @staticmethod
    def _is_match(a, b):
        return a == b[::-1]

    def rotate(self, n):
        new_edges = []
        angle = self.angle + 90 * n
        for i in range(len(self.edges)):
            edge = self.edges[(i - n + len(self.edges)) % len(self.edges)]
            new_edges.append(edge)
        # print(new_edges)
        return Tile(self.img_path, new_edges, angle=angle)
