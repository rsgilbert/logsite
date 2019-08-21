from django.contrib.auth import get_user, decorators
from datetime import date, datetime


@decorators.login_required
def get_user_logs(request):
    user = get_user(request)
    return user.log_set.all()


@decorators.login_required
def logs_of_the_day(request, day):
    return get_user_logs(request).filter(date__date=get_date_as_str(day))

def get_datetime(day):
    return datetime.strptime(day, "%Y-%m-%d")

def get_date(day):
    return get_datetime(day).date()

def get_date_as_str(day):
    return str(get_date(day))