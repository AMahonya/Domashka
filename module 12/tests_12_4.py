import logging
from runner import Runner
from runner_test import TestRunner

logging.basicConfig(level=logging.INFO,
                    filemode="w",
                    filename="test_runner.log",
                    encoding= 'utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')
if __name__ == '__main__':
    runner_test = TestRunner()
    runner_test.test_walk()
    runner_test.test_run()
    run = Runner
    print(run)
