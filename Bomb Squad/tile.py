class Tile:
    def __init__(self, x, y):
        """Initialise tiles."""
        self.x = x
        self.y = y
        self.adj = 0
        self.covered = True
        self.flagged = False
        self.mine = False
        self.exploded = False
        # self.show = False
