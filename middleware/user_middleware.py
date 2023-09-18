# import threading

# class UserMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Store the user information in a thread-local variable
#         #threading.local().user = "salman"
#         my_thread_local = threading.local()

# # Set the 'user' attribute
#         my_thread_local.user = request.employee.email

# # Access the 'user' attribute
#         user = my_thread_local.user

#         print(user)  # This will print "salman"
#         print(request)
#         response = self.get_response(request)
#         return response
from threading import current_thread

from django.utils.deprecation import MiddlewareMixin


_requests = {}


def current_request():
    return _requests.get(current_thread().ident, None)


class RequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        _requests[current_thread().ident] = request

    def process_response(self, request, response):
        # when response is ready, request should be flushed
        _requests.pop(current_thread().ident, None)
        return response


    def process_exception(self, request, exception):
        # if an exception has happened, request should be flushed too
         _requests.pop(current_thread().ident, None)