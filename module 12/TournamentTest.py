import runner
import unittest


class TournamentTest(unittest.TestCase):
    is_frothen = True
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usain = runner.Runner("Усэйн", 10)
        self.Andrey = runner.Runner("Андрей", 9)
        self.Nick = runner.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        print("<= Result Tournament =>")
        for result in cls.all_results.values():
            results = {place: str(runer) for place, runer in result.items()}
            print(results)

    def test_usain_and_nick(self):
        tournament = runner.Tournament(90, self.Usain, self.Nick)
        self.all_results[1] = tournament.start()
        self.assertTrue(self.all_results[1][max(self.all_results[1].keys())] == "Ник")

    @unittest.skipIf(is_frothen, "Тесты в этом кейсе заморожены")
    def test_andrey_and_nick(self):
        tournament = runner.Tournament(90, self.Andrey, self.Nick)
        self.all_results[2] = tournament.start()
        self.assertTrue(self.all_results[2][max(self.all_results[2].keys())] == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = runner.Tournament(90, self.Usain, self.Andrey, self.Nick)
        self.all_results[3] = tournament.start()
        self.assertTrue(self.all_results[3][max(self.all_results[3].keys())] == "Ник")

    def test_usain_overtakes_andrei(self):
        """Проверяем, что Усэйн обгоняет Андрея на дистанции 45"""
        tournament = runner.Tournament(45, self.Usain, self.Andrey)
        results = tournament.start()
        self.assertTrue(results[1] == "Усэйн")

    def test_nick_overtakes_andrei(self):
        """Проверяем, что Ник обгоняет Андрея на дистанции 15"""
        tournament = runner.Tournament(15, self.Andrey, self.Nick)
        results = tournament.start()
        self.assertTrue(results[1] == "Андрей")


if __name__ == "__main__":
    unittest.main()
