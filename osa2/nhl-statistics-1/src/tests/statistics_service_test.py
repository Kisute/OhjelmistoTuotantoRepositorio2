import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_pelaajaLoytyy(self):
        player = self.stats.search("Semenko")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(player.team, "EDM")

    def test_pelaajaaEiLoydy(self):
        player = self.stats.search("huuhaa")
        self.assertIsNone(player)

    def test_tiimi(self):
        tiimi = self.stats.team("EDM")
        self.assertEqual(len(tiimi), 3)
        self.assertEqual(tiimi[0].team, "EDM")
        self.assertEqual(tiimi[1].team, "EDM")
        self.assertEqual(tiimi[2].team, "EDM")

    def test_parhaatPelaajat(self):
        parhaat = self.stats.top(3)
        self.assertEqual(len(parhaat), 4)
        self.assertGreaterEqual(parhaat[0].points, parhaat[1].points)
        self.assertGreaterEqual(parhaat[1].points, parhaat[2].points)

    def test_pelaajienMäärä(self):
        maara = self.stats.top(4)
        self.assertEqual(len(maara), 5)