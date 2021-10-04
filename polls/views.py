from django.http import HttpResponse

import requests as rqt

url = "https://www.space-track.org/ajaxauth/login"
login = {'identity': 'crew288@innovaccion.mx', 'password': 'passNasHac!!21PrimTracksatel', 'query':'https://www.space-track.org/basicspacedata/query/class/tle_latest/orderby/ORDINAL%20asc/limit/100/emptyresult/show'}
response = rqt.post(url,data=login)


def index(request):
    return HttpResponse(response.json())