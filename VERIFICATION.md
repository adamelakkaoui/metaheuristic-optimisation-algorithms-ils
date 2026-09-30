# Verification

Test environment: Python 3.11 on Windows with a non-interactive plotting backend.

- `python -m unittest discover -s tests -v`: 2 tests passed, covering closed-tour distance and preservation of the global-best value.
- `src/ils_tsp.py` completed successfully and generated its ignored plot; the observed seven-city distance in this run was `14.54`.
- The cleaned original notebook passes Jupyter notebook-schema validation and contains no outputs or execution counts.

No exact-solver or TSPLIB benchmark was performed.
