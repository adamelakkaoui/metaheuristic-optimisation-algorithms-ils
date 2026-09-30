import importlib.util
import random
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).parents[1] / "src" / "ils_tsp.py"
SPEC = importlib.util.spec_from_file_location("ils_tsp", MODULE_PATH)
ils = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(ils)


class ILSTests(unittest.TestCase):
    def test_distance_closes_tour(self):
        cities = [(0, 0), (3, 0), (3, 4)]
        self.assertAlmostEqual(ils.distance_totale([0, 1, 2], cities), 12.0)

    def test_reported_best_never_worsens(self):
        random.seed(42)
        cities = [(0, 0), (1, 2), (2, 4), (3, 3), (5, 0), (4, 1), (2, 0)]
        tour, distance, history = ils.recherche_locale_iteree(cities, iterations_max=30)
        self.assertEqual(sorted(tour), list(range(len(cities))))
        self.assertAlmostEqual(distance, min(history))
        self.assertTrue(all(b <= a for a, b in zip(history, history[1:])))


if __name__ == "__main__":
    unittest.main()
