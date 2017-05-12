from django.shortcuts import render
import sys
import json
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http.response import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, HttpResponseBadRequest, HttpResponse
# Create your views here.


def standardize_response(response):
    try:
        if isinstance(response, HttpResponseBadRequest):
            return HttpResponseBadRequest(json.dumps({
                'status': 'fail',
                'data': response.content
            }), content_type='application/json')

        elif isinstance(response, HttpResponseNotFound):
            return HttpResponseNotFound(json.dumps({
                'status': 'error',
                'message': response.content
            }), content_type='application/json')

        elif isinstance(response, HttpResponseForbidden):
            return HttpResponseForbidden(json.dumps({
                'status': 'error',
                'message': 'You are not authorized'
            }), content_type='application/json')

        else:
            return HttpResponse(json.dumps({
                'status': 'success',
                'data': response
            }), content_type='application/json')

    except PermissionDenied:
        return HttpResponseForbidden(json.dumps({
            'status': 'error',
            'message': 'You are not authorized'
        }), content_type='application/json')

    except Exception as e:
        exc_info = sys.exc_info()
        if settings.DEBUG:
            return debug.technical_500_response(request, *exc_info)
        else:
            return HttpResponseServerError(json.dumps({
                'status': 'error',
                'message': 'A server error occurred'
            }), content_type='application/json')


def get_brokers(request):
	return standardize_response({'brokers': ['1', '2']})


def get_flats(request):
	return standardize_response([])

