from django.shortcuts import render
from .models import Plane, Flight, Passenger, Ticket, User_Info 
from django.views.generic import TemplateView, ListView
from django.db.models import Q


class HomePageView(TemplateView):
    template_name = 'travel/home.html'

class SearchResultView(ListView):
	model = Flight 
	template_name = 'travel/flight_list.html'

	def get_queryset(self):
		departure  = self.request.GET.get('departure')
		arrival  = self.request.GET.get('arrival')
		departure_date  = self.request.GET.get('departure_date')
		object_list = Flight.objects.filter(
				Q(from_city__exact=departure) 
				& Q(to_city__exact=arrival) 
				& Q(from_time__contains=departure_date) 
			)
		return object_list












	# if request.method == 'POST':
	# 	filled_form = FlightForm(request.POST)
	# 	if filled_form.is_valid():
	# 		context =  {'flight_form':filled_form}
	# 		return render(request, 'travel/fligh_list.html',context)
	# else:

	# 	flight_form = FlightForm()
	# 	return render(request, 'travel/home.html', {'flight_form':flight_form})


