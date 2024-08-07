import pygame
from Colors import *
from Screen import *

# initalize the scoreboard
scoreboard1 = Scoreboard(200, 60, 350, 10)
scoreboard2 = Scoreboard(250, 60, 325, 80)
scoreboard_Level = Scoreboard(200, 100, 350, 170)
scoreboard_Lines = Scoreboard(200, 100, 350, 280)
scoreboard_Preview = Scoreboard(150, 150, 400, 410)

# initalize the wall
wall_background_left = Wall(20, playing_field_height,(playing_field_x_pos - 10), playing_field_y_pos )
wall_background_right = Wall(20, playing_field_height,(playing_field_x_pos + playing_field_width), playing_field_y_pos )

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(HINTERGRUND)

# RENDER YOUR GAME HERE

    #Call up playing field
    playing_field()

    # Call up the wall
    wall_background_left.wall(screen)
    wall_background_right.wall((screen))

    #Call up the scoreboards
    scoreboard1.scoreboard(screen)
    scoreboard2.scoreboard(screen)
    scoreboard_Level.scoreboard(screen)
    scoreboard_Lines.scoreboard(screen)
    scoreboard_Preview.scoreboard(screen)

    scoreboard1.display_text(screen,'SCORE')
    scoreboard_Level.display_text(screen,'LEVEL')
    scoreboard_Lines.display_text(screen,'LINES')



# flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

