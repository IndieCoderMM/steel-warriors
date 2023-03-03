import random


class Cell:
    def __init__(self, x, y, total_options) -> None:
        self.x = x
        self.y = y
        self.options = [i for i in range(total_options)]
        self.neighbors = []
        self.collapsed = False
        self.tile_index = None


class WaveFunction:
    def __init__(self, cols, rows, tiles):
        self.rows = rows + 1
        self.cols = cols + 1
        self.tiles = tiles
        self.grid: list[list[Cell]] = []

    def setup_grid(self):
        self.grid = []
        for r in range(self.rows):
            row = []
            for c in range(self.cols):
                cell = Cell(c, r, len(self.tiles))
                row.append(cell)
            self.grid.append(row)

    def get_open_cells(self):
        open = []
        for row in self.grid:
            for cell in row:
                if not cell.collapsed:
                    open.append(cell)
        return open

    def get_lowest_e_cell(self):
        open = self.get_open_cells()
        if len(open) == 0:
            return
        lowest_cell = open[0]
        for cell in open:
            if len(cell.options) < len(lowest_cell.options):
                lowest_cell = cell
        return lowest_cell

    def collapse(self, cell: Cell):
        cell.collapsed = True
        cell.tile_index = random.choice(cell.options)

    def validate(self, options, edge):
        valid_options = []
        for opt in options:
            if opt in edge:
                valid_options.append(opt)
        if len(valid_options) == 0:
            return options
        return valid_options

    def get_cell_at(self, x, y):
        if (x < 0 or x >= self.cols or y < 0 or y >= self.rows):
            return
        return self.grid[y][x]

    def propagate(self, cell):
        left = self.get_cell_at(cell.x - 1, cell.y)
        right = self.get_cell_at(cell.x + 1, cell.y)
        top = self.get_cell_at(cell.x, cell.y - 1)
        bottom = self.get_cell_at(cell.x, cell.y + 1)
        if left:
            left.options = self.validate(
                left.options, self.tiles[cell.tile_index].left_neighbors)
        if right:
            right.options = self.validate(
                right.options, self.tiles[cell.tile_index].right_neighbors)
        if top:
            top.options = self.validate(
                top.options, self.tiles[cell.tile_index].top_neighbors)
        if bottom:
            bottom.options = self.validate(
                bottom.options, self.tiles[cell.tile_index].bot_neighbors)

    def generate_new_grid(self):
        self.setup_grid()
        empty_cell = self.get_lowest_e_cell()
        while (empty_cell):
            self.collapse(empty_cell)
            self.propagate(empty_cell)
            empty_cell = self.get_lowest_e_cell()
