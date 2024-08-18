import random
from Screen import *
from Colors import *
from Battlefield import Battlefield
from Tetriminos import *
class Game_Painter():

    def __init__(self, playing_field_width, playing_field_x_pos, playing_field_y_pos):
        self.SQUARE_SIZE = int(playing_field_width // 10)
        self.GRID_THICKNESS = int(playing_field_width // 300)
        self. playing_field_x_pos = playing_field_x_pos
        self.playing_field_y_pos = playing_field_y_pos

    # Gibt ein optisches Gitter im Spielfeld wieder
    def draw_grid (self,screen):
        for row in range(20):
            for column in range(10):
                x = column * self.SQUARE_SIZE + self.playing_field_x_pos
                y = row * self.SQUARE_SIZE + self.playing_field_y_pos
                pygame.draw.rect(screen, PLAYING_FIELD, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE),1)

    # Gibt den aktuellen Status des Spiels wieder
    def draw_battlefield_state(self, screen,  battlefield_state):
        square_size = self.SQUARE_SIZE
        for row in range(20):
            for column in range(10):
                piece = battlefield_state[row][column]
                x = (column * square_size) + self.playing_field_x_pos
                y = (row * square_size) + self.playing_field_y_pos
                if piece == Battlefield.Orange_Ricky:
                    ORANGE_RICKY(screen, x, y, square_size)
                elif piece == Battlefield.Blue_Ricky:
                    BLUE_RICKY(screen, x, y, square_size)
                elif piece == Battlefield.Cleveland_Z:
                    CLEVELAND_Z(screen, x, y, square_size)
                elif piece == Battlefield.Rhode_Island_Z:
                    RHODE_ISLAND_Z(screen, x, y, square_size)
                elif piece == Battlefield.Hero:
                    HERO(screen, x, y, square_size)
                elif piece == Battlefield.Smashboy:
                    SMASHBOY(screen, x, y, square_size)
                elif piece == Battlefield.Teewee:
                    TEEWEE(screen, x, y, square_size)



