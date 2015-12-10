import sys
import traceback

from django.conf import settings


class MyExceptionMiddleware(object):
    def process_exception(self, request, exception: Exception):
        if settings.DEBUG:
            sys.stderr.write(
                ''.join(traceback.format_exception(*sys.exc_info())))
            sys.stderr.write('\n')
            sys.stderr.flush()
