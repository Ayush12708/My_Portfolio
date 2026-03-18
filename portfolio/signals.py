from django.contrib.auth.signals import user_logged_in
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
from django.dispatch import receiver
from django.utils import timezone


@receiver(user_logged_in)
def expire_previous_sessions(sender, request, user, **kwargs):
    """
    When a user logs in, delete ALL other active sessions for that user.
    This ensures only one device/browser can be logged into the admin at a time.
    """
    current_session_key = request.session.session_key

    # Walk through all non-expired sessions and delete ones belonging to this user
    active_sessions = Session.objects.filter(expire_date__gt=timezone.now())
    for session in active_sessions:
        if session.session_key == current_session_key:
            continue  # keep the just-created session
        try:
            data = session.get_decoded()
        except Exception:
            continue
        if str(data.get('_auth_user_id')) == str(user.pk):
            session.delete()
