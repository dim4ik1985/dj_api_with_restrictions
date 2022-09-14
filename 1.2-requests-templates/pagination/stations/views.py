from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open(BUS_STATION_CSV, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        content = [row for row in reader]
        paginator = Paginator(content, 10)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

        context = {
            'bus_stations': page,
            'page': page,
        }
        return render(request, 'stations/index.html', context)
