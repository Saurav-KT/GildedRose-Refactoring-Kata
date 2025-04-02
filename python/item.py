class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        self.update_sell_in()
        self.update_item_quality()

    def update_item_quality(self):
        pass

    def update_sell_in(self):
        self.sell_in -= 1

class BackstagePass(Item):
    def update_item_quality(self):
        if self.quality < 50:
            self.quality += 1
        if self.sell_in < 11 and self.quality < 50:
            self.quality += 1
        if self.sell_in < 6 and self.quality < 50:
            self.quality += 1
        if self.sell_in < 1:
            self.quality = 0

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, days_left={self.sell_in}, quality={self.quality})"

class AgedBrie(Item):
    def update_item_quality(self):
        if self.quality < 50:
            self.quality += 1
        if self.sell_in < 1 and self.quality < 50:
            self.quality += 1

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, days_left={self.sell_in}, quality={self.quality})"

class Sulfuras(Item):
    def update_item_quality(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, days_left={self.sell_in}, quality={self.quality})"

class RegularItem(Item):
    def update_item_quality(self):
        if self.quality > 0:
            self.quality -= 1
        if self.sell_in < 1 and self.quality > 0:
            self.quality -= 1

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, days_left={self.sell_in}, quality={self.quality})"
