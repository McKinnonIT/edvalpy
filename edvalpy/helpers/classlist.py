import csv

def format_classlist_csv(csv):
    """Converts an Edval exported ischolaris classlist.csv to a more workable format
    Returns JSON: {"Class code", "Teacher", "Students"}
    """
    class_list = json.load(open(classlist))
    class_members = json.load(open(classmember))
    class_codes = set([c.get('EdvalClassCode', 'Unknown') for c in class_list])
    class_names = {c.get('EdvalClassCode', 'Unknown'): c.get('DefaultTeacher', '') for c in class_list}
    classroom_sync = []

    for c in class_codes:
        classroom_sync.append(
            (c, c, class_names[c], ",".join(m['StudentId']
                for m in class_members if m['EdvalClassCode'] == c))
            )
