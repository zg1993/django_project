# coding: utf8
from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone
import pytz


class TimezoneMiddleware(MiddlewareMixin):
    # def process_request(self, request):
    #     # tzname = request.session.get('django_timezone')
    #     tzname = filter(lambda i: 'hang' in i, pytz.all_timezones)[0]
    #     print tzname
    #     if tzname:
    #         timezone.activate(pytz.timezone(tzname))
    #     else:
    #         timezone.deactivate()

    def process_response(self, request, response):
        tzname = filter(lambda i: 'hang' in i, pytz.all_timezones)[0]
        timezone.activate(pytz.timezone(tzname))
        return response