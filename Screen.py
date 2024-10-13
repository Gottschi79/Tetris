import pygame
from colors import *

# pygame setup
pygame.init()

# pygame front
pygame.font.init ()

# main screen
screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TETRIS')
clock = pygame.time.Clock()
running = True

# playing_feld
playing_field_x_pos = 9
playing_field_y_pos = 10
playing_field_width = 303
playing_field_height = 600

def playing_field():
    pygame.draw.rect(screen,Colors.PLAYING_FIELD, (playing_field_x_pos,playing_field_y_pos,playing_field_width,playing_field_height),0,0,0,0,0)

# scoreboard

class Scoreboard():

    def __init__(self, scoreboard_width, scoreboard_height , scoreboard_x_pos, scoreboard_y_pos):
        self.scoreboard_width = scoreboard_width
        self.scoreboard_height = scoreboard_height
        self.scoreboard_x_pos = scoreboard_x_pos
        self.scoreboard_y_pos = scoreboard_y_pos

    def scoreboard(self,screen):
        pygame.draw.rect(screen, Colors.PLAYING_FIELD,
                         (self.scoreboard_x_pos, self.scoreboard_y_pos, self.scoreboard_width, self.scoreboard_height), 0, 0, 0,
                         0, 0)
        pygame.draw.rect(screen, Colors.HINTERGRUND,
                         ((self.scoreboard_x_pos+5), (self.scoreboard_y_pos+5), (self.scoreboard_width-10), (self.scoreboard_height-10)), 5, 0, 0,
                         0, 0)

    def display_text(self,screen,text):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text_surface = font.render(text, True, Colors.TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(self.scoreboard_x_pos + self.scoreboard_width // 2,
                                                  self.scoreboard_y_pos + self.scoreboard_height // 2))
        screen.blit(text_surface, text_rect)


class Wall():

    def __init__(self, wall_width, wall_hight,wall_x_pos, wall_y_pos):
        self.wall_width = wall_width
        self.wall_hight = wall_hight
        self.wall_x_pos = wall_x_pos
        self.wall_y_pos = wall_y_pos

    def wall(self, screen):
        # Background
        pygame.draw.rect(screen, Colors.PLAYING_FIELD,(self.wall_x_pos, self.wall_y_pos, self.wall_width, self.wall_hight), 10 )

        # Brickwork
        stone_size_x = 6
        stone_size_y = 3


    def brick(self,screen, x_pos): # Brick loop
        # Brickwork
        stone_size_x = 6
        stone_size_y = 3

        for row in range(200):
            for column in range(3):
                if row % 2 == 0:
                    x =  column * (stone_size_x + 1)+ x_pos + 1
                else:
                    x = (column) * (stone_size_x + 1)+ x_pos -2
                y = row * (stone_size_y + 1) + playing_field_y_pos
                pygame.draw.rect(screen, Colors.STONES, (x, y, stone_size_x, stone_size_y))




