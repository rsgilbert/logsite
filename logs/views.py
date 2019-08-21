from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .utils import view_fns
from .forms import PostForm
from . import forms
from .models import Log



@login_required
def all_logs(request):
	if request.method == 'GET':
		user_logs = view_fns.get_user_logs(request)
		log_dates = {(log.date.date()) for log in user_logs}
		form = PostForm(initial={'date': str(datetime.now())})
		context = {'logs': user_logs, 'log_dates': log_dates, 'form': form}
		return render(request, 'logs/all.html', context)

	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			Log.objects.create(
				user=request.user, date=form.cleaned_data['date'], log=form.cleaned_data['log'])
			return redirect('logs:all_logs')
		else:
			print('errors', form.errors)
			return redirect('logs:all_logs')


@login_required
def day_logs(request, day):
	if request.method == 'POST':
		form = forms.DayPostForm(request.POST)
		if form.is_valid():
			Log.objects.create(user=request.user, date=view_fns.get_datetime(day), log=form.cleaned_data['log'])
			return redirect('logs:day_logs', day=day)

		elif request.POST['delete']:
			log = get_object_or_404(Log, id=request.POST['delete'])
			log.delete()
			return redirect('logs:day_logs', day=day)


	logs = view_fns.logs_of_the_day(request=request, day=day)
	form = forms.DayPostForm()
	return render(request, 'logs/daylogs.html', {'logs': logs, 'form': form, 'day': day})
