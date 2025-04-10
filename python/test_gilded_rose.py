# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from product_list import ProductList


class GildedRoseTest(unittest.TestCase):
    def test_normal_item_before_sell_date(self):
        items = [GildedRose.create_item(ProductList.REGULAR_PRODUCT, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(9, items[0].quality)

    def test_normal_item_after_sell_date(self):
        items = [GildedRose.create_item(ProductList.REGULAR_PRODUCT, 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_aged_brie_before_sell_date(self):
        items = [GildedRose.create_item(ProductList.AGED_BRIE, 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_aged_brie_after_sell_date(self):
        items = [GildedRose.create_item(ProductList.AGED_BRIE, 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(12, items[0].quality)

    def test_backstage_pass_long_before_sell_date(self):
        items = [GildedRose.create_item(ProductList.BACK_STAGE_PASSES, 15, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(11, items[0].quality)

    def test_backstage_pass_after_sell_date(self):
        items = [GildedRose.create_item(ProductList.BACK_STAGE_PASSES, 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_pass_quality_never_exceeds_50(self):
        items = [GildedRose.create_item(ProductList.BACK_STAGE_PASSES, 5, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, items[0].quality)



if __name__ == '__main__':
    unittest.main()
