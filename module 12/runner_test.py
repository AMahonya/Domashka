import logging
import traceback

from runner import Runner
import unittest


class TestRunner(unittest.TestCase):
    is_frothen = False

    @unittest.skipIf(is_frothen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            runner = Runner("John Doe", -5)
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info("'test_walk' выполнен успешно")
        except ValueError as e:
            logging.warning(f"Неверная скорость для Runner\n{e}")
            logging.warning(traceback.format_exc())

    def test_run(self):
        try:
            runner = Runner(113, 10)
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info("'test_run' выполнен успешно")
        except TypeError as e:
            logging.warning(f"Неверный тип данных для обьекта Runner\n{e}")
            logging.warning(traceback.format_exc())

    def test_challenge(self):
        runner1 = Runner("Alice")
        runner2 = Runner("Dasha")
        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)
        logging.info("'test_challenge' выполнен успешно")


if __name__ == "__main__":
    unittest.main()
