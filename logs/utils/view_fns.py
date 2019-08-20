from django.contrib.auth import get_user, decorators
from datetime import date


@decorators.login_required
def get_user_logs(request):
    user = get_user(request)
    return user.log_set.all()


@decorators.login_required
def logs_of_the_day(request, day):
    return get_user_logs(request).filter(date__date=date.today())