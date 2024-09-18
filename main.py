import pygame

import Screen
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

# Timer für automatische Bewegung nach unten
pygame.time.set_timer(pygame.USEREVENT, 1000)  # Bewegt den Stein alle 1000ms nach unten

pressing_down = False
pressing_left = False
pressing_right = False
pressing_up = False

battlefield.start_position()

while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pressing_up = True
            if event.key == pygame.K_LEFT:
                pressing_left = True
            elif event.key == pygame.K_RIGHT:
                pressing_right = True
            elif event.key == pygame.K_DOWN:
                pressing_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                pressing_left = False
            elif event.key == pygame.K_RIGHT:
                pressing_right = False
            elif event.key == pygame.K_DOWN:
                pressing_down = False
            elif event.key == pygame.K_UP:
                pressing_up = False

        # aktuellen Spielstein löschen, wenn eine Taste gedrückt wird (Positionen ändern)
        if pressing_down or pressing_left or pressing_right:
            battlefield.clear_screen()

        if pressing_down:
            battlefield.down()
        if pressing_down == False:
            battlefield.down_move()
        if pressing_right:
            battlefield.right()
        if pressing_left:
            battlefield.left()
        if pressing_up:
            battlefield.rotate()



    # Fill the screen with a background color
    screen.fill(HINTERGRUND)

    # Game logic: Move the piece
    battlefield.clear_screen()
    battlefield.set_piece()
    #battlefield.move_piece()



    # Render the walls
    wall_background_left.wall(screen)
    wall_background_right.wall(screen)
    wall_background_left.brick(screen, (playing_field_x_pos - 19))
    wall_background_right.brick(screen, (playing_field_x_pos + playing_field_width))

    # Render the scoreboards
    scoreboard1.scoreboard(screen)
    scoreboard2.scoreboard(screen)
    scoreboard_Level.scoreboard(screen)
    scoreboard_Lines.scoreboard(screen)
    scoreboard_Preview.scoreboard(screen)

    scoreboard1.display_text(screen, 'SCORE')
    scoreboard_Level.display_text(screen, 'LEVEL')
    scoreboard_Lines.display_text(screen, 'LINES')

    # Draw the battlefield state and grid
    Screen.playing_field()
    game_painter.draw_grid(screen)
    game_painter.draw_battlefield_state(screen,battlefield.state)



    # Flip the display to put your work on screen
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(1)

# Quit pygame
pygame.quit()
