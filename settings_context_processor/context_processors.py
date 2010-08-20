"""
Adds the settings specified in settings.TEMPLATE_SETTIGNS to
the request context.

Documentation:
 - http://docs.djangoproject.com/en/dev/ref/templates/api/#writing-your-own-context-processors
 - http://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATE_CONTEXT_PROCESSORS
 - http://www.b-list.org/weblog/2006/jun/14/django-tips-template-context-processors/

Nothing like this in django core:
 - http://code.djangoproject.com/ticket/3818
 - http://code.djangoproject.com/ticket/1278

Similiar functionality:
 - http://sciyoshi.com/blog/2008/jul/10/dynamic-django-settings-context-processor/
   
"""

from django.conf import settings as django_settings
from django.core.exceptions import ImproperlyConfigured

def settings(request):
    """
    Adds the settings specified in settings.TEMPLATE_VISIBLE_SETTINGS to
    the request context.
    """
    new_settings = {}
    for attr in django_settings.TEMPLATE_VISIBLE_SETTINGS:
        try:
            new_settings[attr] = getattr(django_settings, attr)
        except AttributeError:
            m = "TEMPLATE_VISIBLE_SETTINGS: '{0}' does not exist".format(attr)
            raise ImproperlyConfigured(m);
    return new_settings

