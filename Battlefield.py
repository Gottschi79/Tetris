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

        self.current_row = 0
        self.current_column = 4  # Beginnt in der Mitte des Spielfelds

    def make_move(self):

        # Stück bewegt sich standardmäßig nach unten
        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN]:
            self.current_row += 5
        else:
            self.current_row += 1

        if keys[pygame.K_LEFT]:
            self.current_column -= 5
        elif keys[pygame.K_RIGHT]:
            self.current_column += 5

        # Überprüfen, ob das Stück den unteren Rand des Spielfelds erreicht hat
        if self.current_row >= len(self.state):
            self.current_row = len(self.state) - 1

        # Überprüfen, ob das Stück den linken oder rechten Rand des Spielfelds erreicht hat
        if self.current_column < 0:
            self.current_column = 0
        elif self.current_column >= len(self.state[0]):
            self.current_column = len(self.state[0]) - 1

        # Setze den ausgewählten Stein in das Spielfeld
        self.state[self.current_row][self.current_column] = self.selected_piece









