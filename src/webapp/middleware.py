from django.middleware.common import CommonMiddleware
import re
from django.shortcuts import render
from django.conf import settings


class AdminLoginMiddleware(CommonMiddleware):

    def process_request(self, request):
        if re.search('^/admin', request.path) and request.META.get('REMOTE_ADDR', '') not in settings.ADMIN_IPS:
            return render(request, '401.html', status=401)
