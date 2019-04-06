from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Company, Company_Field

# Create your views here.

def index(request):
      return HttpResponse("Hello, world")

def detail(request, company_id):
    return HttpResponse("You're looking at company %s." % company_id)

@csrf_exempt
def recommend(request):
      json_data = json.loads(request.body)
      fields = Company_Field.objects.filter(field_name=json_data['AOI']).filter(field_minimum_score__lte=json_data['Score'])
      companies = []
      for field in fields:
            companies.append(get_object_or_404(Company, id=field.company_id).company_name)

      # return HttpResponse(companies)
      responseData = {
        'recommended_companies' : companies
      }
      return JsonResponse(responseData)
