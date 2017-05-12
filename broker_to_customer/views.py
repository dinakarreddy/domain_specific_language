from django.shortcuts import render
import sys
import json
import requests
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist
from django.http.response import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import debug, defaults
from django.conf import settings
from functools import wraps

from broker_to_customer import models
from broker_to_customer import tasks
import traceback
# Create your views here.


def standardize_response(orig_func):

    @wraps(orig_func)
    def wrapper(request, *args, **kwargs):
        try:
            response = orig_func(request, *args, **kwargs)

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
    return wrapper


@csrf_exempt
@standardize_response
def store_user_token(request):
    data = json.loads(request.body)
    user_id = data.get('user_id')
    device_id = data.get('device_id')
    if not user_id or not device_id:
        return HttpResponseBadRequest('user_id and device_id required')
    row = models.User_Devices(user_id=user_id, device_id=device_id)
    row.save()
    return 'stored user token'

@csrf_exempt
@standardize_response
def store_user_requirement(request):
    data = json.loads(request.body)
    user_id = data.get('user_id')
    requirements = data.get('requirements')
    requirement_id = data.get('requirement_id')
    if not user_id or not requirement_id:
        return HttpResponseBadRequest('user_id and requirement_id required')
    row = models.User_Requirements(user_id=user_id, requirements=requirements, requirement_id=requirement_id)
    row.save()
    tasks.broadcast_brokers.delay(requirement_id)
    return 'stored user requirement'

@csrf_exempt
@standardize_response
def get_brokers(request):
	return {'brokers': ['1', '2']}

@csrf_exempt
@standardize_response
def get_flats(request):
	response = requests.get('https://search.housing.com/api/v0/rent/get_bulk_rent_details?rent_ids=1547572')
	return response.json()

