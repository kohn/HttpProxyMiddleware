# -*- coding: utf-8 -*-
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from threading import Timer
import logging

logger = logging.getLogger("IPBanTest")

ip_count = {}

def clear_ip():
    logger.info("clear ip_count")
    ip_count.clear()
    Timer(10*60, clear_ip, ()).start() # clear evert 10min

Timer(10, clear_ip, ()).start()

@cache_page(0)
def index(request):
    ip = request.META.get("REMOTE_ADDR")
    if ip in ip_count.keys():
	ip_count[ip] += 1
    else:
	ip_count[ip] = 0
        
    message = {}
    if ip_count[ip] > 5:
	return HttpResponseForbidden("banned")
    else:
	message["ip"] = ip
	message["count"] = ip_count[ip]
	return JsonResponse(message)
