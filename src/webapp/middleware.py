from django.middleware.common import CommonMiddleware
import re
from django.shortcuts import render

class AdminLoginMiddleware(CommonMiddleware):

    def process_request(self, request):
        if re.search('^/admin', request.path) and request.META.get('REMOTE_ADDR','') != '127.0.0.1' :
            return render(request, '401.html', status=401)
