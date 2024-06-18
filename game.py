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


