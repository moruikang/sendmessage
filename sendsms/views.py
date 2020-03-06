# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from .serializers import *
from .logs import logger
from send import send_mail
from tasks import send_email
from models import *

import json
# Create your views here.

def hello(request):
    return HttpResponse("Hello word.")

@csrf_exempt
@api_view(['POST'])
def sendsms(request):

    data = SmsSerializer(data=request.data)
    logger.info('here')
    if data.is_valid():

        body = dict()

        body['username'] = data.validated_data['username']
        body['phone'] = data.validated_data['phone']
        body['verify_code'] = data.validated_data['verify_code']
        body['content'] = data.validated_data['content']
    else:
        return HttpResponse(data.error_messages, status=400)
    return HttpResponse(json.dumps(body), content_type="application/json")

@csrf_exempt
@api_view(['POST'])
def sendemail(request):

    data = EmailSerializer(data=request.data)

    if data.is_valid():

        username = data.validated_data['username']
        email = data.validated_data['email']
        verify_code = data.validated_data['verify_code']
        content = data.validated_data['content']

    else:
        return HttpResponse(data.error_messages, status=400)

    mail_title = "测试验证码"
    mail_content = content + verify_code
    try:
        # send_mail(receiver=email, mail_title=mail_title,\
        # mail_content=mail_content )
        send_email.delay(receiver=email, mail_title=mail_title,\
        mail_content=mail_content )

        status = 'succeed'
    except Exception as e:
        status = 'failure'
        logger.info(e)

    email_status = Email(
        email = email,
        username = username,
        verify_code = verify_code,
        status = status
    )
    email_status.save()

    return HttpResponse(json.dumps({"status": status }), content_type="application/json")
