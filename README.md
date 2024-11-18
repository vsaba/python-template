# Python Project Template

This is a template for a Python project, designed to streamline development and enforce code quality standards using tools such as linters and type checkers.

## Getting Started

Before starting the project make sure to go through the following steps.

### 1. Set Up a Virtual Environment
Create and activate a virtual environment to isolate the project dependencies.

#### On Linux/MacOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### On Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install requirements
Install the packages defined in the requirements.txt file
```bash
pip install -r requirements.txt
```

### 3. install pre-commit hooks

This project uses pre-commit hooks to enforce code quality checks like linting and formatting. **The hooks must be installed before running the project.**

Ensure `pre-commit` is installed in your environment:
```bash
pip install pre-commit
```


### 4. Setup environemnt variables
Evnironemnt variable templates are defined in the `.env.example` file.
Create a `.env` file, copy the values from the `.env.example` and replace the placeholders with values


### 5. Run the project
The project code can be simply run with the following command:
```bash
python -m src
```