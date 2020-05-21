from django.shortcuts import render
from core.forms import DataQueryForm
from core.models import SignsRegistration


# Create your views here.


def history_vital_sings(request):
	if request.method == "POST":
		form = DataQueryForm(request.POST)
		if form.is_valid():
			result = SignsRegistration.objects.filter(patient__idNumber=int(form['idNumber'].value()),
												patient__age=int(form['age'].value())).order_by('date')
			form = DataQueryForm()
			return render(
				request,
				"history.html",
				{'form': form, 'result': result}
			)

	form = DataQueryForm()
	return render(
		request,
		"history.html",
		{'form': form}
	)
