def run(self):
    
    self.player.calculate_movement_options(self.map_w, self.map_h)
    self.clear

    self.game_map.display_map()
    self.decorate()
    self.player.health_bar.draw()
    self.decorate(True)
    self.game_map.display_movement_options(self.player_movement_options)

    self.player.get_movement_input() 


    while True:
        self.Clear()

        if enemy is self.spawn_enemy(self.player.pos):
            self.combat(enemy)

        if self.player.health <= 0:
            input("Game Over")
            break
        
       


def run (self) -> None:
    while True:
        self.check_events()

        if self.player.health <= 0:
            break

        self.player.calculate_movement_options(self.map_w, self.map_h)
        self.game_map.pdate_map(self.player.pos, self.player.marker)
        self.display()
        self.display_ui()
        pygame.display.update()

def next_turn (self) -> None:
    self.player.attack(self.enemy_in_combat)
    self.enemy_in_combat.attack(self.player)

    if self.player.health <= 0 or self.enemy_in_combat.health <= 0:
        self.enemy_in_combat None

def check_events(self) -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and self.player.movement_options_get("up"):
                self.player.pos[1] -= 1
                self.enemy_in_combat = self.spawn_enemy(self.player.pos)
            elif event.key == pygame.K_s and self.player.movement_options_get("down"):
                self.player.pos[1] += 1
                self.enemy_in_combat = self.spawn_enemy(self.player.pos)
            elif event.key == pygame.K_a and self.player.movement_options_get("left"):
                self.player.pos[0] -= 1
                self.enemy_in_combat = self.spawn_enemy(self.player.pos)
            elif event.key == pygame.K_d and self.player.movement_options_get("right"):
                self.player.pos[0] += 1
                self.enemy_in_combat = self.spawn_enemy(self.player.pos)

            if self.enemy_in_combat:
                if event.key == pygame.K_RETURN:
                    self.next_turn()
            elif:
                self.check_movement_inputs(event)
        