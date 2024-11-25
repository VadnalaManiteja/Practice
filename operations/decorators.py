from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.storage.fallback import FallbackStorage
from django.http import HttpResponseForbidden
from django.template.loader import render_to_string

def role_required(required_role):
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            # Check user role
            if hasattr(request.user, 'profile') and request.user.profile.role == required_role:
                return view_func(request, *args, **kwargs)
            # Redirect to a consistent page or display 403
            return HttpResponseForbidden(
                render_to_string('403.html', {"message": "You do not have access to view this page."})
            )
        return _wrapped_view
    return decorator