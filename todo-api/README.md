# todo-api

Todo API built with FastAPI.

## Requirements

- Rye 0.39.0

## Setup

Install project dependencies:

```sh
rye sync
```

This will create a new virtual environment in the `.venv` directory.

If using Visual Studio Code, select the Python interpreter in the `.venv/bin`
directory to get the project dependencies recognized.

Install `pre-commit` hooks:

```sh
rye run pre-commit install
```

## Usage

Start API locally, running Alembic first to make sure that the database is
up-to-date:

```sh
./scripts/start_api.sh
```

To start the API in debug mode using Visual Studio Code, the following launch configuration is required:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python Debugger: Current File",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "cwd": "${workspaceFolder}/todo-api",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/todo-api"
      }
    }
  ]
}
```

Then, launch the Python Debugger using the `launch.json` configuration with the
file `todo-api/app/main.py`.

## Tests

To run the tests:

```sh
rye run pytest
```

To configure Visual Studio Code to discover the tests, add this snippet to the
user or workspace `settings.json` file:

```js
{
  ...
  "python.testing.cwd": "${workspaceFolder}/todo-api",
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  ...
}
```
