from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . models import Job
from . serializers import JobSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# 'POST' method requires csrf token
@csrf_exempt
def job_list(request):
    if request.method=='GET':
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True) 
        # convert and return json data
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        # convert srting (json) data to dicts
        data = JSONParser().parse(request)
        serializer = JobSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def job_detail(request, pk):
    try:
        job = Job.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer = JobSerializer(job)
        return JsonResponse(serializer.data)


    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = JobSerializer(job, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


    elif request.method=='DELETE':
        job.delete()
        return HttpResponse(status=204)




