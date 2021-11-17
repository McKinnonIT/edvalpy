# edvalpy

- [Prerequisites](#prerequisites)
- [Installing](#installing)
- [Usage](#usage)

## Prerequisites
Before you can export a csv, you'll need to add the "iScholaris" sync config.
1. Log into https://my.edval.education
2. From the top-left, click **Daily** then **Synchronise**
3. On the right, click **Add sync system** 
4. From the **System** dropdown, select **iScholaris Flat file** and click **Save**

## Installing

```
pip install -r requirements.txt
```

## Usage <a name = "usage"></a>

```python
In [23]: from edvalpy import Edval
In [24]: edval = Edval("YOUR_EDVAL_WEB_TOKEN")
In [25]: edval.configs
Out[25]: [ischolaris (1), compass (2)]
In [26]: edval.ischolaris.files()
Out[26]: 
['everyone.csv',  
 'teachers.csv',  
 'classlists.csv',
 'classlessons.csv',
 'DailyTimetable.csv',
 'EventMembership.csv']

In [27]: edval.ischolaris.save_file("classlists.csv")

❯ head -n5 classlists.csv
Student,Class,Subject,Teacher
AAA0001,10PHY-6,10 Physics,01234567
BBB0001,10PHY-6,10 Physics,01234567
CCC0001,10PHY-6,10 Physics,01234567
DDD0001,10PHY-6,10 Physics,01234567
```
