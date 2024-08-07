def wall(self, screen):
    # Background
    pygame.draw.rect(screen, PLAYING_FIELD, (self.wall_x_pos, self.wall_y_pos, self.wall_width, self.wall_hight), 10)

    # Brickwork
    stone_size_x = 4
    stone_size_y = stone_size_x / 2
    half_stone_size_x = stone_size_x / 2
    half_stone_size_y = stone_size_y

    # Brick loop
    for row in range(int(self.wall_width / (stone_size_x + 1))):
        for column in range(int(self.wall_hight / (stone_size_y + 1))):
            if row % 2 == 0:
                x = self.wall_x_pos + column * (stone_size_x + 2)
            else:
                x = self.wall_x_pos + column * (half_stone_size_x + 2)
            y = self.wall_y_pos + row * (stone_size_y + 2)
            pygame.draw.rect(screen, STONES, (x, y, stone_size_x, stone_size_y))
