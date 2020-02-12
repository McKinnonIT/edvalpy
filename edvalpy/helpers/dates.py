import datetime


def get_sync_dates(days=14):
    """
    Returns formatted dates in a format required for the Edval.run_sync() function,
    optionally the days parameter can be used to chose how far inthe future timetable data is returned.
    Default is 14 days
    """
    data_from = datetime.datetime.now().strftime("%Y-%m-%d")
    data_to = (datetime.datetime.now() + datetime.timedelta(days=days)).strftime(
        "%Y-%m-%d"
    )
    return {"from": data_from, "to": data_to}
