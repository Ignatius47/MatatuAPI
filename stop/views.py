from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import StopSerializer
from .models import Stop
import logging

logger = logging.getLogger('django')



class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer


def test_logging(request):
    logger.debug("This is a DEBUG message")
    logger.info("This is an INFO message")
    logger.warning("This is a WARNING message")
    logger.error("This is an ERROR message")
    logger.critical("This is a CRITICAL message")
    return HttpResponse("Check logs for all error levels.")



# Create your views here.
