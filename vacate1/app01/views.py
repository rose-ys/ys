from app01 import models
from django.shortcuts import render, redirect, reverse
from app01.forms import QingJiaForm
from utils.pagination import Pagination


def index(request):
    return render(request, 'index.html')


# 新增请假申请
def qingjia(request):
    form_obj = QingJiaForm()

    if request.method == 'POST':
        form_obj = QingJiaForm(request.POST)

        if form_obj.is_valid():
            # 校验成功
            form_obj.save()  # 存入数据库
            return render(request, 'ok.html')

    return render(request, 'qingjia.html', {'form_obj': form_obj})


# 审批请假申请
def shenpi(request):
    all_notpass = models.Application.objects.all()
    if request.method == 'POST':
        obj = request.POST.get('action')
        # print('obj=',obj)
        pk = request.POST.get('pk')
        # print('pk=',pk)

        if obj and pk:

            if obj == 'del':
                models.Application.objects.filter(pk=pk).delete()
            elif obj == 'ok':
                models.Application.objects.filter(pk=pk).update(case=True)

    page = Pagination(request.GET.get('page', 1), all_notpass.count(), request.GET.copy(), 10)

    return render(request, 'shenpi.html',
                  {'all_notpass': all_notpass[page.start:page.end], 'page_html': page.page_html})
