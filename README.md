# daturai_project

1. Setup

# For Unix/macOS/WSL
curl -sSL https://install.python-poetry.org | python3 -

# For Windows PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

# Install dependencies
poetry install

# Initialize pre-commit hooks
poetry run pre-commit install

poetry run pre-commit run --all-files
or
poetry run pre-commit run --files  src/task_01.py --hook-stage manual


2. How to run
poetry run pytest
or
python -m unittest tests/test_task.py -v
or 
python -m unittest discover -s tests/ -p "test_*.py" -v


