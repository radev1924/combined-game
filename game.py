from abc import abstractmethod



class Game(ABV):
    def __init__(self, map_w: int, map_h: int) -> None:
    
        self.map_w = map_w
        self.map_h = map_h
        self.game_map = Map(map_w, map_h)
        self.player = Player()
    
    def decorate(self, before=False, afterr=False) -> None:
        newline = "\n"
        print(f"{newline if before else ''}-{'-' * self.map_w}{newline if after else ''}")

    @abstractmethod
    def run (self) -> None:
        ... 
    
    @staticmethod
    def clear() -> None:
        os.system("cls||clear")
    
    def spawn_enemy(self, pos:list [int]) -> Enemy : None

    x, y = pos
    chance =randint(1,100)
    tile = self.game_map.init_map_data[x][y]
    if chance < SPAWN_CHANCE and tile.name != "water"
        return deepCopy(choice_enemies)

class Pygamemode(Game)
    def __init__(self, map_w: int = 30, map_h: int = 15) -> None:
        super().__init__(map_h, map_w)

        pygame.init()

        self.tile_size = 10
        self.hud_height = 140
        self.screen_width = self.tile_size * map_w * 2 + self.tile_size * 2
        self.screen_height = self.tile_size * map_h * 2 + self.hud_height + self.tile_size

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.canvas = pygame.Surface((self.map_w * self.tile_size, self.map_h * self.tile_size)).convert
        self.map_background = pygame.Surface(( self.screen_width, self.screen_height -  self.hud_height)).convert_alpha()
        self.map_background.fill("brown")

        self.game.map.load_images()
        self.player.marker.load_image()

        self.enemy_in_combat = None

    def load_image(self):
        self.image =pygame.image.load(
            os.path.join("images" , f{self.name}.png)
        ).convert_alpha()

    def load_images(self) -> None:
        for row in self.init.map_data:
            for tile in row:
                tile.load.image()

    def display_ui(self) -> None:
        self.draw_text(self.player.name, (self.screen_width / 2, self.screen_height - 110))
        self.draw_health_bar(self.player.health, self.player.health_max, (40, 200, 40), self.screen_height - 95)

        if self.enemy_in_combat:
            self.draw_text("[ENTER] - ATTACK", (self.screen_width - 40, self.screen_height - 105), "right")
            self.draw_text(self.enemy_in_combat.name, (self.screen_width / 2, self.screen_height - 55))
            self.draw_health_bar(self.enemy_in_combat.health, self.enemy_in_combat.health_max, (200, 40, 40), self.screen_height - 40)
        else:
            for index, (direction, value) in enumerate(self.game_map.movement_options.items()):
                if self.player.movement_options.get(direction):
                    self.draw_text(value, (40, self.screen_height - 105 + index * 22), "left")

    def draw_health_bar(self, hp: int, max_hp: int, color list[int], y: int) -> None:
        lenght = 200
        widht = max(hp / max_hp * lenght, 1)
        bar =pygame.Surface((widht. 20))convert_alpha()
        bar.fill(color)
        self.screen.blit(bar, (self.screen.blit / 2 - lenght / 2), y)
        