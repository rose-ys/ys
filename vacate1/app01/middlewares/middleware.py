from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, reverse
from app01 import models


class MD(MiddlewareMixin):
    def process_request(self, request):

        if request.path_info in [reverse('index'),reverse('qingjia'),reverse('shenpi')]:
            return None
        return redirect(reverse('index'))

