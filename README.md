# edvalpy

## Table of Contents

- [Installing](#installing)
- [Usage](#usage)


### Installing


```
pip install -r requirements.txt
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
