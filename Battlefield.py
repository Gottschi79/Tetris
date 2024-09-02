import random
import pygame.key


class Battlefield():

    Orange_Ricky = 1
    Blue_Ricky = 2
    Cleveland_Z = 3
    Rhode_Island_Z = 4
    Hero = 5
    Teewee = 6
    Smashboy = 7

    def __init__(self):
                      #0,1,2,3,4,5,6,7,8,9
        self.state = [[0,0,0,0,0,0,0,0,0,0], #0
                      [0,0,0,0,0,0,0,0,0,0], #1
                      [0,0,0,0,0,0,0,0,0,0], #2
                      [0,0,0,0,0,0,0,0,0,0], #3
                      [0,0,0,0,0,0,0,0,0,0], #4
                      [0,0,0,0,0,0,0,0,0,0], #5
                      [0,0,0,0,0,0,0,0,0,0], #6
                      [0,0,0,0,0,0,0,0,0,0], #7
                      [0,0,0,0,0,0,0,0,0,0], #8
                      [0,0,0,0,0,0,0,0,0,0], #9
                      [0,0,0,0,0,0,0,0,0,0], #10
                      [0,0,0,0,0,0,0,0,0,0], #11
                      [0,0,0,0,0,0,0,0,0,0], #12
                      [0,0,0,0,0,0,0,0,0,0], #13
                      [0,0,0,0,0,0,0,0,0,0], #14
                      [0,0,0,0,0,0,0,0,0,0], #15
                      [0,0,0,0,0,0,0,0,0,0], #16
                      [0,0,0,0,0,0,0,0,0,0], #17
                      [0,0,0,0,0,0,0,0,0,0], #18
                      [0,0,0,0,0,0,0,0,0,0]] #19


        self.pieces = [Battlefield.Orange_Ricky,
                        Battlefield.Blue_Ricky,
                        Battlefield.Cleveland_Z,
                        Battlefield.Rhode_Island_Z,
                        Battlefield.Hero,
                        Battlefield.Teewee,
                        Battlefield.Smashboy]

        # Zufällig einen Stein auswählen
        self.selected_piece = random.choice(self.pieces)

        self.current_position = [4, 0]

    def clear_previous_position(self):
        """Setzt die aktuelle Position des Spielsteins im Spielfeld auf 0."""
        x, y = self.current_position
        self.state[y][x] = 0

    def make_move(self):
        # Zunächst die aktuelle Position löschen
        self.clear_previous_position()

        # Bewegung des Steins nach Benutzereingabe
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.current_position[1] += 3  # Nach unten bewegen
        else:
            self.current_position[1] += 1  # Nach unten bewegen
        if keys[pygame.K_LEFT]:
            self.current_position[0] -= 1  # Nach links bewegen
        elif keys[pygame.K_RIGHT]:
            self.current_position[0] += 1  # Nach rechts bewegen

        # Grenzen des Spielfelds überprüfen
        if self.current_position[1] >= len(self.state):
            self.current_position[1] = len(self.state) - 1
        if self.current_position[0] < 0:
            self.current_position[0] = 0
        elif self.current_position[0] >= len(self.state[0]):
            self.current_position[0] = len(self.state[0]) - 1

        # Setze die neue Position des Spielsteins
        x, y = self.current_position
        self.state[y][x] = self.selected_piece

        # Zum Debuggen: aktuellen Zustand des Spielfelds drucken
        for row in self.state:
            print(row)







