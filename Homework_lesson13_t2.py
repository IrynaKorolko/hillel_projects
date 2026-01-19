class Counter:

    def __init__(self, current=1, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_value):
        self.max_value = max_value

    def set_min(self, min_value):
        self.min_value = min_value

    def step_up(self):
        if self.current < self.max_value:
            self.current += 1
        else:
            raise ValueError("Value cannot exceed max value.")

    def step_down(self):
        if self.current > self.min_value:
            self.current -= 1
        else:
            raise ValueError("Value cannot go below min value.")

    def get_current(self):
        return self.current