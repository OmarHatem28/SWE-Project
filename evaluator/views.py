from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Company, Company_Field, User, User_Field
from django.core import serializers

# Create your views here.

def index(request):
      return HttpResponse("Hello, world")

def detail(request, company_id):
    return HttpResponse("You're looking at company %s." % company_id)

@csrf_exempt
def recommend(request):
      json_data = json.loads(request.body)
      fields = Company_Field.objects.filter(field_name=json_data['FOI']).filter(field_minimum_score__lte=json_data['Score'])
      companies = []
      rec = []
      co=0
      for field in fields:
            companies.append(get_object_or_404(Company, id=field.company_id))
            rec.append(
                  {
                        'company_id' : companies[co].pk,
                        'company_name' : companies[co].company_name,
                        'field' : field.field_name
                  }
            )
            print(companies[co].pk)
            co+= 1

      responseData = {
        'recommended_companies' : rec
      }
      return JsonResponse(responseData)


@csrf_exempt
def recommendUsers(request):
      json_data = json.loads(request.body)
      fields = User_Field.objects.filter(field_name=json_data['Open_field']).filter(field_test_score__gte=json_data['min_score'])
      users = []
      rec = []
      co=0
      for field in fields:
            users.append(get_object_or_404(User, id=field.user_id))
            rec.append(
                  {
                        'user_id' : users[co].pk,
                        'user_name' : users[co].user_name,
                        'user_score' : field.field_test_score
                  }
            )
            co+= 1

      responseData = {
        'recommended_users' : rec
      }
      return JsonResponse(responseData)

