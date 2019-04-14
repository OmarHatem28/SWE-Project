from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Company, Company_Field
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

      # return HttpResponse(companies)
      responseData = {
        'recommended_companies' : rec
      }
      # response_data = {}
      # try:
      #       response_data['result'] = 'Success'
      #       response_data['recommended_companies'] = serializers.serialize('json', companies)
      # except:
      #       response_data['result'] = 'Ouch!'
      #       response_data['recommended_companies'] = 'Script has not ran correctly'
      return JsonResponse(responseData)
