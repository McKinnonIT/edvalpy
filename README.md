- [edvalpy](#edvalpy)
  - [Requirements](#requirements)
  - [Prerequisites](#prerequisites)
  - [Installing](#installing)
  - [Usage](#usage)
    - [:computer: Command-line tool](#computer-command-line-tool)
    - [:snake: In a Python program or script](#snake-in-a-python-program-or-script)

# edvalpy
A command-line tool used to export timetable data from [Edval](https://my.edval.education)

## Requirements
- :snake: [Python 3.8.5+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- An Edval WebCode for https://my.edval.education

## Prerequisites

Before you can export a csv, you'll need to add the **iScholaris** sync config.
1. Log into https://my.edval.education.
2. From the top-left, click **Daily** then **Synchronise**.
3. On the right, click **Add sync system**.
4. From the **System** dropdown, select **iScholaris Flat file** and click **Save**.

## Installing

```bash
git clone https://github.com/scv-m/edvalpy.git
cd edvalpy/
pip install -r requirements.txt
```

## Usage 

### :computer: Command-line tool

```bash
python edvalpy --token "DJF47SL" --path "C:\Users\sc-vm\Downloads"
```

```
python edvalpy --help
Usage: python -m edvalpy [OPTIONS]

Options:
  --token TEXT                    Your Edval WebCode
  --path TEXT                     Path where your Edval csvs will be saved
  --help                          Show this message and exit.
```

### :snake: In a Python program or script

```python
from edvalpy import Edval

edval = Edval("YOUR_EDVAL_WEB_TOKEN")
edval.ischolaris.save_file("classlists.csv")
```

```bash
❯ head -n5 classlists.csv
Student,Class,Subject,Teacher
AAA0001,10PHY-6,10 Physics,01234567
BBB0001,10PHY-6,10 Physics,01234567
CCC0001,10PHY-6,10 Physics,01234567
DDD0001,10PHY-6,10 Physics,01234567
```
