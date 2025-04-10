# -*- coding: utf-8 -*-
from item import AgedBrie,BackstagePass,Sulfuras,RegularItem
from product_list import ProductList
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    @classmethod
    def create_item(cls, name, sell_in, quality):
        if name == ProductList.AGED_BRIE:
            return AgedBrie(name, sell_in, quality)
        elif name == ProductList.BACK_STAGE_PASSES:
            return BackstagePass(name, sell_in, quality)
        elif name == ProductList.SULFURAS:
            return Sulfuras(name, sell_in, quality)
        else:
            return RegularItem(name, sell_in, quality)

    def update_quality(self):
        for item in self.items:
            print(item)
            item.update_quality()


# items = [
#         GildedRose.create_item("Regular Item", 10, 20),
#         GildedRose.create_item("Aged Brie", 5, 10),
#         GildedRose.create_item("Backstage passes to a TAFKAL80ETC concert", 12, 20),
#         GildedRose.create_item("Sulfuras, Hand of Ragnaros", 0, 80)
#     ]
#
# gilded_rose = GildedRose(items)
# gilded_rose.update_quality()












