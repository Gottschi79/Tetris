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
    def draw_battlefield_state(self, screen, battlefield_state):
        for row in range(len(battlefield_state)):  # Gehe durch die Zeilen
            for column in range(len(battlefield_state[row])):  # Gehe durch die Spalten
                value = battlefield_state[row][column]  # Den Wert an der Position (row, column) holen

                if value != 0:  # Nur gezeichnet, wenn der Wert nicht 0 ist
                    x = column * self.SQUARE_SIZE + self.playing_field_x_pos
                    y = row * self.SQUARE_SIZE + self.playing_field_y_pos

                    # Farbe basierend auf dem Wert zuweisen
                    if value == 1:
                        pygame.draw.rect(screen, ORANGE, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                    elif value == 2:
                        pygame.draw.rect(screen, BLAU, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                    elif value == 3:
                        pygame.draw.rect(screen, ROT, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                    elif value == 4:
                        pygame.draw.rect(screen, GRUEN, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                    elif value == 5:
                        pygame.draw.rect(screen, HELLBLAU, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                    elif value == 6:
                        pygame.draw.rect(screen, GELB, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))
                    elif value == 7:
                        pygame.draw.rect(screen, LILA, (x, y, self.SQUARE_SIZE, self.SQUARE_SIZE))



