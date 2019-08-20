from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .utils import view_fns
from django.contrib.auth import get_user
from .forms import PostForm
from .models import Log
# Create your views here.



@login_required
def all_logs(request):
	if request.method == 'GET':
		user_logs = view_fns.get_user_logs(request)
		log_dates = { (log.date.date()) for log in user_logs }
		form = PostForm(initial={'date': str(datetime.now())})
		context = {'logs': user_logs, 'log_dates': log_dates, 'form': form}
		return render(request, 'logs/all.html', context)

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			Log.objects.create(user=request.user, date=form.cleaned_data['date'], log=form.cleaned_data['log'])
			return redirect('logs:all_logs')
		else:
			print('errors', form.errors)
			return redirect('logs:all_logs')
		



@login_required
def day_logs(request, day):
    logs = view_fns.logs_of_the_day(request=request, day=day)

    # read
    if request.method == 'GET':
        return render(request, 'logs/daylogs.html', {'logs': logs})





