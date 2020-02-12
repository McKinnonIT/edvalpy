# edvalpy

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

rite about 1-2 paragraphs describing the purpose of your project.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

```
Give examples
```

### Installing


```
pip install .
or
pip install -e .
```

## Usage <a name = "usage"></a>

```
from edvalpy import Edval

edval = Edval("YOUR_EDVAL_TOKEN")
edval.configs
sync = edval.configs[2]
csv_file = sync.get_file("classlists.csv")
sync.save_file("classlists.csv", r"C:\Users\Sam\Downloads\classes.csv")
```