class Counter:
    def __init__(self, x, y, n1, n2, n3):
        """Initialises counters."""
        self.x = x
        self.y = y
        self.num_1 = n1
        self.num_2 = n2
        self.num_3 = n3

    def increment(self):
        """Increments the total number of the counter."""
        if self.num_3 < 9:
            self.num_3 += 1
        elif self.num_2 < 9:
            self.num_2 += 1
            self.num_3 = 0
        else:
            self.num_1 += 1
            self.num_2 = 0
            self.num_3 = 0

    def decrement(self):
        """Decrements the total number of the counter."""
        if self.num_3 > 0:
            self.num_3 -= 1
        elif self.num_2 > 0:
            self.num_2 -= 1
            self.num_3 = 9
        else:
            self.num_1 -= 1
            self.num_2 = 9
            self.num_3 = 9

    def get_val(self):
        """Returns the value of the counter."""
        total_val = self.num_1 * 100
        total_val += self.num_2 * 10
        total_val += self.num_3
        return total_val

    def set_val(self, aim):
        """Sets the value of the counter"""
        while aim > self.get_val():
            self.increment()
        while self.get_val() > aim:
            self.decrement()
