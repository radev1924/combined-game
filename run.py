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