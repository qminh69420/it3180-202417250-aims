MAX_NUMBERS_ORDERED = 20


class Cart:
    def __init__(self):
        self.items = []

    def add_digital_video_disc(self, dvd):
        if len(self.items) > MAX_NUMBERS_ORDERED:
            return False
        self.items.append(dvd)
        print("The disc has been added")
        return True

    def remove_digital_video_disc(self, dvd):
        if dvd not in self.items:
            return False
        self.items.remove(dvd)
        return True

    def total_cost(self):
        return round(sum(dvd.cost for dvd in self.items), 2)
