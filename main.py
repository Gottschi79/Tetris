import pygame
from Colors import *
from Screen import *
from Game_Painter import Game_Painter

# initalize the scoreboard
scoreboard1 = Scoreboard(200, 60, 350, 10)
scoreboard2 = Scoreboard(250, 60, 325, 80)
scoreboard_Level = Scoreboard(200, 100, 350, 170)
scoreboard_Lines = Scoreboard(200, 100, 350, 280)
scoreboard_Preview = Scoreboard(150, 150, 400, 410)

# initalize the wall
wall_background_left = Wall(20, playing_field_height,(playing_field_x_pos - 20), playing_field_y_pos )
wall_background_right = Wall(20, playing_field_height,(playing_field_x_pos + playing_field_width), playing_field_y_pos )

# initalize Game_Painter
game_painter = Game_Painter(playing_field_width, playing_field_x_pos, playing_field_y_pos)

#initalize Battelfield
battlefield = Battlefield()

battlefield.make_move(1,3)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

       
    # game_logik


    # fill the screen with a color to wipe away anything from last frame
    screen.fill(HINTERGRUND)

# RENDER YOUR GAME HERE

    # Check if a new piece is needed


    # Move the current piece down


    # Call up the wall
    wall_background_left.wall(screen)
    wall_background_right.wall(screen)
    wall_background_left.brick(screen,(playing_field_x_pos - 19))
    wall_background_right.brick(screen, (playing_field_x_pos + playing_field_width))

    #Call up the scoreboards
    scoreboard1.scoreboard(screen)
    scoreboard2.scoreboard(screen)
    scoreboard_Level.scoreboard(screen)
    scoreboard_Lines.scoreboard(screen)
    scoreboard_Preview.scoreboard(screen)

    scoreboard1.display_text(screen,'SCORE')
    scoreboard_Level.display_text(screen,'LEVEL')
    scoreboard_Lines.display_text(screen,'LINES')

    #Call up playing_field
    playing_field()

    #Call Battelfield_state
    game_painter.draw_battlefield_state(screen,battlefield.state)
    game_painter.draw_grid(screen)


# flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

