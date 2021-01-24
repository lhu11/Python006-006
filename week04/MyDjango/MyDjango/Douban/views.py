from django.shortcuts import render
from django.db.models import  Avg
from .models import T1
# Create your views here.
def books_short(request):
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "
    # 情感倾向
    sent_avg = f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte': 0.5}
    plus = queryset.filter(**condtions).count()

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt': 0.5}
    minus = queryset.filter(**condtions).count()

    # return render(request, 'douban.html', locals())
    return render(request, 'result.html', locals())


def books_short_star(request):
    shorts = T1.objects.all()
    counter = T1.objects.all().count()
    star_value = T1.objects.values('n_star')
    conditions = {'n_star__gt': 3}
    short_list = T1.objects.filter(**conditions)
    return render(request, 'result1.html', locals())

def books_search(request):
    if request.POST:
        text=request.POST.get('text',None)
        shorts = T1.objects.all()
        conditions = {"short__icontains":text}
        short_list = T1.objects.filter(**conditions)
        return render(request, 'result2.html', locals())

    else:
        shorts = T1.objects.all()
        return render(request, 'result.html', locals())