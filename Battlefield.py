import random
import pygame.key
from Tetriminos import *


class Battlefield():

    # Spielfeld initialisieren (20x10)
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

        # Alle verfügbaren Spielsteine
        self.pieces = [orange_ricky, blue_ricky,cleveland,rhode_island, hero, teewee, smashboy]


        # Zufällig einen Stein auswählen
        self.selected_piece = random.choice(self.pieces)

        self.selected_piece_index_rotation = 0

        # Index des ausgewählten Steines finden
        self.selected_piece_index = self.pieces.index(self.selected_piece)

        self.selected_piece_start = self.selected_piece[self.selected_piece_index_rotation]

        # Ausgabe des ausgewählten Steins und seines Indexes
        print(f"Das zufällig ausgewählte Stück ist '{self.selected_piece_start}' und hat den Index {self.selected_piece_index}.")


    def start_position(self):

        # Anzahl der Spalten des ausgewählten Spielsteins
        num_columns = int(len(self.selected_piece_start))

        # Berechnung der Startposition in der Mitte des Spielfelds
        start_position_column = int((10 - num_columns) / 2)

        # Setze die Startposition des Spielsteins (x, y)
        self.active_current_position = [start_position_column, 0]
        print (self.active_current_position)

        return self.active_current_position

    def set_piece(self):
        start_row = self.active_current_position[1]
        start_col = self.active_current_position[0]

        # Iteriere über die Zeilen und Spalten des Spielsteins
        for y in range(len(self.selected_piece_start)):
            for x in range(len(self.selected_piece_start[y])):
                # Setze den Wert des Spielsteins auf das Spielfeld, falls der Stein dort existiert
                if self.selected_piece_start[y][x] != 0:  # Nur nicht-leere Zellen setzen
                    self.state[start_row + y][start_col + x] = self.selected_piece_start[y][x]

        print (self.state)


    def down(self):
        self.active_current_position[1] += 1


#Todo def down_move, clear_screen funktioniert nicht, Stein setz in der mitte des Spielfeldes an
    def down_move(self):                       # automatische Spielablauf, der Stein bewegt sich nach unten
        self.active_current_position[1] += 1

    def left(self):
        self.active_current_position[0] -= 1

    def right(self):
        self.active_current_position[0] += 1

    def rotate(self):
        print("Aktuelles Stück:", self.selected_piece_start)

        current_rotation_index = self.selected_piece_index_rotation # bestimmt den aktuellen Index der Rotation
        print('aktueller Rotation Index', self.selected_piece_index_rotation)

        numbers_possible_rotation = len(self.pieces[self.selected_piece_index]) # Anzahl der Rotationsvarianten
        print('mögliche Rotationen', numbers_possible_rotation)

        new_rotation_index = (current_rotation_index + 1) % numbers_possible_rotation
        self.selected_piece_index_rotation = new_rotation_index
        self.selected_piece_start = self.pieces[self.selected_piece_index][self.selected_piece_index_rotation]
        print("Neuer Rotation Index:", self.selected_piece_index_rotation)
        print("Aktuelles Stück:", self.selected_piece_start)
        return self.selected_piece_start


#ToDo Fehler in def Clear_screen - Bei Rotation bleibt wird die alte Reihe nicht gelöscht
    def clear_screen(self):
        # Die aktuelle Position des aktiven Steins (Kolonne, Reihe)
        start_col, start_row = self.active_current_position

        # Iteriere über die Zeilen und Spalten des aktuellen Steins
        for y in range(len(self.selected_piece_start)):
            for x in range(len(self.selected_piece_start[y])):
                # Wenn das aktuelle Feld des Steins nicht leer ist
                if self.selected_piece_start[y][x] != 0:
                    # Berechne die tatsächliche Position auf dem Spielfeld
                    actual_row = start_row + y
                    actual_col = start_col + x

                    # Setze den Wert auf dem Spielfeld auf 0, um den alten Stein zu löschen
                    if 0 <= actual_row < len(self.state) and 0 <= actual_col < len(self.state[0]):
                        self.state[actual_row][actual_col] = 0

        # Ausgabe des aktualisierten Spielfelds
        print(self.state)





