from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
import datetime

from .models import Car

def index(request):
    cars_list = Car.objects.order_by('end_date')
    context = {'cars_list': cars_list}
    return render(request, 'odometr/index.html', context)
    
def car(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    total_mileage = sum([x.mileage for x in car.checkpoint_set.all()]) + car.initial_mileage
    target_mileage = int(car.initial_mileage + car.yearly_mileage/365.0 * (timezone.now() - car.start_date).days)
    context = {'car' : car, 'total_mileage' : total_mileage, 'target_mileage' : target_mileage}
    return render(request, 'odometr/car.html', context)
