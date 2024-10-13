class Colors:
	PLAYING_FIELD = '#E3E3E3'  # Hellgrau
	HINTERGRUND = '#808080'  # Dunkelgrau
	TEXT_COLOR = '#808080'  # Dunkelgrau
	WALL_COLOR = '#BABABA'  # Mittelgrau
	OUTER_FRAME = '#E3E3E3'  # Hellgrau
	INNER_FRAME = '#808080'  # Dunkelgrau
	STONES = '#818049'  # grau
	BLAU = '#0023F5'
	ORANGE = '#FFC017'
	GRUEN = '#18F56F'
	LILA = '#EA3FF7'
	GELB = '#FFFD55'
	ROT = '#FC0A19'
	HELLBLAU = '#9FFCFD'

	@classmethod
	def get_cell_colors(cls):
		return [cls.PLAYING_FIELD, cls.GRUEN, cls.ROT, cls.ORANGE, cls.GELB, cls.LILA, cls.HELLBLAU, cls.BLAU]
