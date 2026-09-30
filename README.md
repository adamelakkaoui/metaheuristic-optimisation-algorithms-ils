# Metaheuristic Optimisation Algorithms (ILS)

Academic implementation of Iterated Local Search (ILS) for a small Euclidean Travelling Salesperson Problem example.

## Verified features

- Euclidean tour-length calculation with return to the starting city.
- 2-opt-style local search.
- Random swap perturbation with configurable strength.
- Simulated-annealing-inspired acceptance criterion and cooling.
- Best-tour and convergence plots for a seven-city example.

The submitted notebook recorded a tour length of `14.54` for its seven-city example. Because the implementation is stochastic and originally had no fixed seed, the precise route is not a stable benchmark and no claim of global optimality is made.

## Portfolio correction

The submitted loop overwrote the variable described as the global best whenever a worse candidate was probabilistically accepted, and applied local search before rather than after perturbing the candidate. `src/ils_tsp.py` now keeps current and global-best solutions separately and applies local search to each perturbed candidate. French pedagogical function names are preserved. The cleaned original notebook remains in `notebooks/` for provenance.

## Installation and use

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements.txt
python src/ils_tsp.py
python -m unittest discover -s tests -v
```

## Author

Adam El Akkaoui

## Academic artefacts

- [French academic report (PDF)](docs/academic-report-fr.pdf). No presentation or video was found.

## Testing and limitations

On Python 3.11, two tests passed for closed-tour distance and global-best preservation. The script completed and observed distance `14.54` on the seven-city example; the cleaned notebook validates. The portfolio copy corrects current/global-best separation and local-search placement. Only one small synthetic instance is supplied; no exact solver, TSPLIB benchmark, repeated-run distribution, scalability experiment or claim of global optimality is included. Runtime and solution quality depend on the seed and parameters.
