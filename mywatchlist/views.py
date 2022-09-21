from django.http import HttpResponse
from django.shortcuts import render
from mywatchlist.models import MyWatchlist
from django.core import serializers


# TODO: Create your views here.
def show_mywatchlist(request):

    data_watchlist = MyWatchlist.objects.all()

    watched=0
    not_watched=0

    for film in data_watchlist:
        if film.watched == True:
            watched+=1
        else:
            not_watched+=1

    # loop untuk validasi film yang ditonton
    if watched >= not_watched:
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        "watchlist": data_watchlist,
        "message": message,
        "judul": "My Watch List",
        "nama": 'Undissya Putri Maharani',
        "npm": "2106650935",
    }
    return render(request, "mywatchlist.html", context)

def show_mywatchlist_json(request):
    data_watchedlist = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize('json', data_watchedlist), content_type='application/json')

def show_mywatchlist_xml(request):
    data_watchedlist = MyWatchlist.objects.all()
    return HttpResponse(serializers.serialize('xml', data_watchedlist), content_type='application/xml')

def show_json_by_id(request, id):
    data_watchedlist = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data_watchedlist), content_type="application/json")

def show_xml_by_id(request, id):
    data_watchedlist = MyWatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data_watchedlist), content_type="application/xml")