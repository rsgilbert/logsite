from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .utils import view_fns
# Create your views here.


@login_required
def all_logs(request):
    pass


@login_required
def day_logs(request, day):
    logs = view_fns.logs_of_the_day(request=request, day=day)
    if request.method == 'GET':
        return render(request, 'logs/daylogs.html', {'logs': logs})


