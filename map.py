from random import randint
from tile import Tile, plains, forest, pines, mountain, water


class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.init_map_data: list[list[str]]
        self.full_map_data: list[[str]]
        self.map_data: list[list[Tile]]
        self.exporation_process: [player]

        self.generate_map()
        self.generate_patch(forest, 2, 5, 7)
        self.generate_patch(pines, 2, 2, 5)
        self.generate_patch(mountain, 3, 5, 7)
        self.generate_patch(water, 1, 10, 12)
        self.generate_patch(town, 3, 3, 3)

        self.movement_options = {...}

        self.explored_tiles = [player]

    def generate_map(self) -> None:
        self.init_map_data = [[plains.colored_symbol for _ in range(self.width)] for _ in range(self.height)]
        self.map_data = deepcopy(self.init_map_data)
        self.exploration_process =[[0 for _ in range (self.width)] for _ in range(self.height)]

    def update_map(self, pos: list[int], marker: Tile) -> None:
        x, y = pos
        self.map_data = deepcopy(self.init_map_data)
        self.map_data[y][x] = marker.colored_symbol

    def generate_patch(
            self,
            tile: Tile,
            num_patches: int,
            min_size: int,
            max_size: int,
            irregular: bool = True
    ) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)

            if irregular:
                init_start_x = randint(3, self.width - max_size)

            for i in range(height):
                if irregular:
                    width = randint(int(0.7 * max_size), max_size)
                    start_x = init_start_x - randint(1, 2)
                for j in range(width):
                    self.map_data[start_y + i][start_x + j] = tile

    def display_map(self) -> None:
        frame = "x" + self.width * "=" + "x"
        print(frame)

        for y_index, (row, explored_row) in enumerate(zip(self.map_data, self.exploration_process)):

            if y_index in range(len(self.explored_tiles)):
                legend = self.explored_tiles[y_index].colored_legend
            else
                legend = ""

            print(
                "|" + "".join(
                    [
                        tile.colored_symbol if is_explored else " "
                        for tile, is_explored in zip(row, explored_row)
                    ]
                ) + "|" + legend
            )
        print(frame)

    def reveal_map(self, pos: list[int]) -> None:
        x, y = pos
        sight_range = range(-2, 3)
        fov = [
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],

        ]
        for y_index in sight_range:
            tile_y = y + y_index
            if 0 <= tile_y < self.height:
                for x_index in sight_range:
                    tile_x = x + x_index
                    if 0 <= tile_x < self.width and fov[y_index + 2][x_index + 2]:
                        self.exploration_process[tile_y][tile_x] = 1
                        revealed_tile = self.init_map_data[tile_y][tile_x]
                        if revealed_tile not in self.explored_tiles:
                            self.explored_tiles.append(revealed_tile)

    def display(self) -> None:
        self.screen.fill("black")

        for i, row in enumerate(self.game_map.map_data):
            for j, tile in enumerate(row):
                if self.game_map.exploration_process[i][j]:
                    self.canvas.blit(tile, image, (j * self.tile_size, i * self.tile_size))
        self.screen.blit(self.map_background, (0, 0))
        self.screen.blit(pygame.transform.scale2x(self.canvas),(self.tile_size, self.tile_size))
     
    def draw_text(self, text: str, pos: list[int], alignment=None) -> None:
        font = pygame.font.Font("fint.ttf" 30)

        text_surface = font.render(text, True, (255, 255, 255)).convert_alpha()
        text_rect = text_surface.get_rect(center = pos)

        if alignment == "left":
            text_rect.midleft = pos
        elif alignment == "right":
            text_rect.midright = pos
        self.screen.blit(text_surface, text_rect)