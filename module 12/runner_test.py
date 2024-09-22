from runner import Runner
import unittest


class TestRunner(unittest.TestCase):
    is_frothen = False

    @unittest.skipIf(is_frothen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("John Doe")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)



    def test_run(self):
        runner = Runner("Bob")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner1 = Runner("Alice")
        runner2 = Runner("Dasha")
        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()
