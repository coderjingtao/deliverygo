from django.shortcuts import render
from comment.models import City, Suburb, CityRisk
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def getNewsList(request):
    return render(request, 'news_list.html')

def getNewsDetail(request, no):
    return render(request, 'news_detail'+str(no) +'.html')

def analysis(request):
    return render(request, 'risk_level2.html')

def cityRiskAll(request):
    return render(request,'risk_level.html',{'city_list':CityRisk.objects.all()})

def cityRiskByName(request):
    cities = CityRisk.objects.filter(name__contains=request.GET['city'].upper())
    return render(request,'risk_level2.html',{'city_list':cities})
    #return JsonResponse(cities)

def show_allcity(request):
    return render(request,'city.html', { 'city_list': City.objects.all() })

def show_suburbs(request, id):
    suburbs = Suburb.objects.filter(city__id=id)
    return render(request,'suburb.html', {'suburb_list':suburbs})

def make_comment(request, id):
    ctx = {'code':200}
    try:
        suburb = Suburb.objects.get(pk=id)
        if request.path.startswith('/good'):
            suburb.good_count +=1
            ctx['result'] = f'Good({suburb.good_count})'
        else:
            suburb.bad_count +=1
            ctx['result'] = f'Bad({suburb.bad_count})'
        suburb.save()
    except suburb.DoesNotExist:
        ctx['code'] = 404
    return JsonResponse(ctx)