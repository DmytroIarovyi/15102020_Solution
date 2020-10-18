import datetime


@property
def current_date(self):
    return datetime.datetime.today().strftime('%Y-%m-%d')
