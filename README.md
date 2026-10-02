# Metaheuristic Optimisation Algorithms (ILS)

Academic implementation of Iterated Local Search (ILS) for a small Euclidean Travelling Salesperson Problem example.

## Implementation

- Euclidean tour-length calculation with return to the starting city.
- 2-opt-style local search.
- Random swap perturbation with configurable strength.
- Simulated-annealing-inspired acceptance criterion and cooling.
- Best-tour and convergence plots for a seven-city example.

The project report records a final route length of `14.54` for the seven-city example.

## Project files

The ILS implementation is available in `notebooks/ils_original.ipynb` and `src/ils_tsp.py`.

## Author

Adam El Akkaoui

## Academic artefacts

- [French academic report (PDF)](docs/academic-report-fr.pdf).

## Results, complexity and limitations

The report applies Iterated Local Search to a seven-city TSP example and shows a clear reduction of the total route distance compared with the initial solution.

The theoretical complexity reported for the implementation is:

- **Time:** `O(iterations_max × n²)`, dominated by the 2-opt local search.
- **Space:** `O(n)`.

For the example with `n = 7` and `iterations_max = 1000`, the report estimates about `49,000` operations and notes that the observed execution time is consistent with this order of complexity for a small instance.

The limitations identified in the report are sensitivity to parameter choices, the possibility of remaining trapped in local minima, and reduced scalability for large TSP instances because of the quadratic local-search cost. Suggested improvements include adaptive parameters, stronger local-search neighborhoods such as 3-opt, hybridization with other metaheuristics, and parallel execution for larger problems.
