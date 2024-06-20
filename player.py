class Player:
    def __init__(self) -> None:
        self.pos = [0,0]
        self.marker = player
    def move(self, x: int, y: int):
        self.pos[0] += x
        self.pos[1] += y
    def calculate_movement_options(self, width, height) -> dict[str, bool]:
        return{
            "up": self.pos[1] > 0,
            "down": self.pos[1] < height,
            "left": self.pos[0] > 0,
            "right": self.pos[0] < width,
        }