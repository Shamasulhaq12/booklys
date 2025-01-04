import logging
from apps.core.models import LogEntry

# Helper function to get client IP
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class ActivityLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before processing the request
        response = self.get_response(request)

        # After processing the request, log activity
        self.log_activity(request)
        return response

    def log_activity(self, request):
        user = request.user if request.user.is_authenticated else None
        ip_address = get_client_ip(request)
        activity = f"Accessed {request.path} with method {request.method}"

        # Save log to database
        LogEntry.objects.create(
            user=user.username if user else "Anonymous",
            ip_address=ip_address,
            activity=activity,
            person=user.get_full_name() if user and hasattr(user, 'get_full_name') else None,
        )
