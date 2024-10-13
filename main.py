import pygame,sys
from game import Game
from colors import Colors
from Screen import *

pygame.init()

# initalize the scoreboard
title_font = pygame.font.Font(None, 40)
scoreboard1 = Scoreboard(200, 60, 350, 10)
scoreboard2 = Scoreboard(250, 60, 325, 80)
scoreboard_Level = Scoreboard(200, 100, 350, 170)
score_surface_box = Scoreboard(200, 100, 350, 280)
score_surface = title_font.render("Score", True, Colors.TEXT_COLOR)
scoreboard_next_surface = Scoreboard(150, 150, 400, 410)
next_surface = title_font.render("Next", True, Colors.TEXT_COLOR)
game_over_surface = title_font.render("GAME OVER", True, Colors.ROT)

# initalize the wall
wall_background_left = Wall(20, playing_field_height,(playing_field_x_pos - 20), playing_field_y_pos )
wall_background_right = Wall(20, playing_field_height,(playing_field_x_pos + playing_field_width), playing_field_y_pos )

score_rect = pygame.Rect(350, 80, 60, 60)
next_rect = pygame.Rect(430, 500, 170, 180)

screen = pygame.display.set_mode((600, 620))
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 300)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if game.game_over == True:
				game.game_over = False
				game.reset()
			if event.key == pygame.K_LEFT and game.game_over == False:
				game.move_left()
			if event.key == pygame.K_RIGHT and game.game_over == False:
				game.move_right()
			if event.key == pygame.K_DOWN and game.game_over == False:
				game.move_down()
				game.update_score(0, 1)
			if event.key == pygame.K_UP and game.game_over == False:
				game.rotate()
		if event.type == GAME_UPDATE and game.game_over == False:
			game.move_down()

	#Drawing
	score_value_surface = title_font.render(str(game.score), True, Colors.TEXT_COLOR)

	screen.fill(Colors.HINTERGRUND)
	scoreboard1.scoreboard(screen)
	scoreboard2.scoreboard(screen)
	scoreboard_Level.scoreboard(screen)
	score_surface_box.scoreboard(screen)
	screen.blit(score_surface, (365, 20, 350, 280))
	scoreboard_next_surface.scoreboard(screen)
	screen.blit(next_surface, (420, 420, 400, 410))



	if game.game_over == True:
		screen.blit(game_over_surface, (100, 100, 50, 50))

	screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
		centery = score_rect.centery))
	game.draw(screen)

	wall_background_left.wall(screen)
	wall_background_right.wall(screen)
	wall_background_left.brick(screen, (playing_field_x_pos - 19))
	wall_background_right.brick(screen, (playing_field_x_pos + playing_field_width))

	pygame.display.update()
	clock.tick(60)