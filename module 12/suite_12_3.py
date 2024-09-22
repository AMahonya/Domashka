import runner_test
import unittest
import TournamentTest


runDZ = unittest.TestSuite()
runDZ.addTest(unittest.TestLoader().loadTestsFromTestCase(runner_test.TestRunner))
runDZ.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runDZ)
