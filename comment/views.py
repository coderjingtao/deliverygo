from django.shortcuts import render
from comment.models import City, Suburb, CityRisk
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator

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

# def make_comment(request, id):
#     ctx = {'code':200}
#     try:
#         suburb = Suburb.objects.get(pk=id)
#         if request.path.startswith('/good'):
#             suburb.good_count +=1
#             ctx['result'] = f'Good({suburb.good_count})'
#         else:
#             suburb.bad_count +=1
#             ctx['result'] = f'Bad({suburb.bad_count})'
#         suburb.save()
#     except suburb.DoesNotExist:
#         ctx['code'] = 404
#     return JsonResponse(ctx)

def roadblock(request):
    return render(request, 'road_block.html')

def safetyVote(request):
    id = request.GET.get('id')
    score = request.GET.get('score')
    ctx = {'code':200}
    try:
        suburb = Suburb.objects.get(pk=id)
        suburb.star_count +=1
        suburb.star_total +=float(score)
        ctx['result'] = suburb.rating
        suburb.save()
    except suburb.DoesNotExist:
        ctx['code'] = 404
    return JsonResponse(ctx)

def starry(request): # the most romantic method
    # if request.path.startswith('/showstar'):
        #suburbs = Suburb.objects.filter(city__id=1)
        # suburbs = Suburb.objects.all() 
        # limit = 10
        # paginator = Paginator(suburbs,limit)
        # page = request.GET.get('page','1')  #默认从第一页开始
        # result = paginator.page(page)
        # resp = { 'city_list': City.objects.all(), 'suburb_list':result }

    suburb_name = request.GET.get('suburb') #根据表单的name属性，不是id
    pcode = request.GET.get('postcode')
    city_id = request.GET.get('city')
    if city_id is None and suburb_name is None and pcode is None:
        suburbs = Suburb.objects.all() 
    elif city_id is not None and city_id!='':
        suburbs = Suburb.objects.filter(city__id=city_id,name__icontains=suburb_name,postcode__contains=pcode) #大小写不敏感
    else:
        suburbs = Suburb.objects.filter(name__icontains=suburb_name,postcode__contains=pcode)
        
    limit = 10
    paginator = Paginator(suburbs,limit)
    page = request.GET.get('page','1')  #从页面中获得page参数，没有则默认从第一页开始
    result = paginator.page(page)
    resp = { 'city_list': City.objects.all(), 'suburb_list':result }
    return render(request,'vote.html', {'resp':resp} )

def about(request):
    return render(request, 'aboutus.html')

def team(request):
    return render(request, 'teaminfo.html')

def d3_bar(request):
    return render(request, 'd3_barchart.html')

def d3_bubble(request):
    return render(request, 'd3_bubble.html')

def weather(request):
    return render(request, 'weather.html')

# def d3(request):
#     cities = CityRisk.objects.all()
#     cities_serilized =  serializers.serialize('json', cities)
#     return JsonResponse(cities_serilized,safe=False)

def page_not_found(request):
    return render(request,'404.html')