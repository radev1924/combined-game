def run(self):
    while True:
        self.Clear()

        if enemy is self.spawn_enemy(self.player.pos):
            self.combat(enemy)

        if self.player.health <= 0:
            input("Game Over")
            break
        
        self.player.calculate_movement_options(self.map_w, self.map_h)

        self.game_map_update_map(self.player.pos, self.player.marker)

        self.game_map.display_map()
        self.game_map.display_movement_options(self.player_movement_options)

        self.player.get_movement_input() 


def spawn_enemy(self, pos: list [i nt]) —> Enemy I None:
x, Y = pos
chance
= randint(l, 100)
tile =
sel f. game_map. i ni t_map_data [y] [x]
if chance < SPAWN_CHANCE and tile. name != "water":
return deepcopy(choi ce (enemi es))

def spawn_enemy(self, pos:list [int]) -> Enemy : None

    x, y = pos
    chance =randint(1,100)
    tile = self.game_map.init_map_data[x][y]
    if chance < SPAWN_CHANCE and tile.name != "water"
        return deepCopy(choice_enemies)
