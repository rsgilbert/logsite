from django.shortcuts import render
from utils import view_fns
from django.contrib.auth.decorators import login_required
from datetime import date

# Create your views here.


@login_required
def dashboard (request):
    today_logs = view_fns.logs_of_the_day(request, date.today())
    return render(request, 'dashboard/dashboard.html', {"logs": today_logs})
