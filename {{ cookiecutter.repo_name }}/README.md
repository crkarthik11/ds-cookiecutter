# {{ cookiecutter.repo_name }}

{{ cookiecutter.description }}

## Project Organization

```
├── README.md          <- The top-level README for developers using this project.
├── pyproject.toml     <- Project configuration file.
├── setup.py           <- Makes project pip-installable (pip install -e .) so project code can be imported.
├── setup.cfg          <- Configuration file for setup.py.
├── .flake8            <- flake8 configuration file.
├── .gitattributes     <- git-attributes configuration file.
├── .gitignore         <- git-ignore configuration file.
│
├── analysis           <- Analysis scripts and notebooks. Naming convention is a number (for
│                         ordering) and a short description with `_` separators, e.g.
│                         `1_0_initial_data_exploration`. Add directories to organise and
│                         separate purposes, as appropriate.
│
├── binder             <- Contains requirements.txt to instruct Binder and docker/Dockerfile
│                         how to create an image.
│
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modelling.
│   └── raw            <- The original, immutable data dump.
│
├── docker             <- Contains the Dockerfile.
│   └── scripts        <- Helper scripts for a Docker container e.g. launch scripts.
│
├── docs               <- Support documents for project code.
│
├── examples           <- Examples using project code. Add directories to organise, if appropriate.
│
├── models             <- Trained and serialized models, model predictions, or model summaries.
│
├── src                <- Source code for use in this project.
│   ├── {{cookiecutter.module_name}}
│   │   ├── __init__.py    <- Makes a Python module
│   │   ├── ...
│
├── tasks              <- Module with task definitions for invoke. See `invoke --list`.
|
├── tests              <- Unit tests for the project source code.
```

## Prerequisites

- [Docker][docker] or [Docker for windows][docker4windows]

- [invoke][invoke]:
  Used for task execution.

- [pre-commit][pre-commit]:
  Used for automating tasks on version control.
  Code is formatted using [Black][black] on commit.

## Set-up

1. Obtain the code: either a git clone or an export
2. Download the [data](#data)
3. [Create or pull Docker image](#tasks)
4. Run `pre-commit install`

Additional optional set-up steps:

- VSCode:
  - Configure Python environment location
  - Enable flake8 code checking
  - Enable pylint code checking

## Tasks

Many tasks, especially set-up ones, are automated using [invoke][invoke].
These are defined in the [`tasks` module](tasks).
See `invoke -l` for descriptions and `tasks` for definitions.
The main tasks are listed below.


<table>
<thead>
<th>Task</th>
<th>Command</th>
<th>Comments</th>
</thead>

<tr>
<td>Pull Docker image</td>
<td><code>invoke docker.pull image_name</code></td>
<td><code>image_name</code> is image's name, e.g. <code>jupyter/scipy-notebook:latest</code></td>
</tr>

<tr>
<td>Build image</td>
<td><code>invoke docker.build-image</code></td>
<td></td>
</tr>

<tr>
<td>Run container</td>
<td><code>invoke docker.run</code></td>
<td>Enters bash shell. <b>Currently does not work</b></td>
</tr>

<tr>
<td>Run jupyter notebook</td>
<td><code>invoke docker.run image_name</code></td>
<td><b>Currently does not work</b></td>
</tr>

<tr>
<td>Run python interpreter</td>
<td><code>invoke docker.run-python</code></td>
<td><b>Currently does not work</b></td>
</tr>

</table>

## Binder

TODO

## Data

Data files are shared via the project drive, which is:

```bash
<project drive>
```

### Original data

The original data files received from the client are stored in:

```bash
<project drive>/FROZEN/data_received/<datestamp>
```

_etc._

--------

<small>
This project was generated using Thinkingstack Sygmoid project generator
<small>