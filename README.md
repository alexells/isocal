# isocal

Simple python script to check the max available date for MIQ bookings and generate an alert when it changes.

## Local installation

- you will first need to install the [Poetry package manager](https://python-poetry.org/docs/#installation) and Python 3.9 on your system
- `git clone` this repo and `cd` into project directory.
- install the poetry environment:
    - to use the exact same dependency versions, install from the lockfile with `poetry install`
    - to rebuild the dependency graph using the latest versions available for your system use `poetry build && poetry install`

## Run the script

`python main.py`

This will check that the max available date is equal to the date defined in the script. If the dates are not equal, an error will be thrown so that Github Actions CI breaks and an alert is sent.

## To do

- take a date arg
