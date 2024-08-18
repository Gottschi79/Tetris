import random
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

    def make_move(self, row, column):
        # Liste der möglichen Steine
        pieces = [
            Battlefield.Orange_Ricky,
            Battlefield.Blue_Ricky,
            Battlefield.Cleveland_Z,
            Battlefield.Rhode_Island_Z,
            Battlefield.Hero,
            Battlefield.Teewee,
            Battlefield.Smashboy]

        # Zufällig einen Stein auswählen
        selected_piece = random.choice(pieces)

        # Setze den ausgewählten Stein in das Spielfeld
        self.state[row][column] = selected_piece


