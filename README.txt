---------- django-settings-context-processor ----------
-------------------------------------------------------


What does it do?
---------------
Makes specified django settings visible in the template rendering context.


How does it do it?
------------------
django-settings-context-processor takes the settings variable
TEMPLATE_VISIBLE_SETTINGS, which should be an iterable of strings,
and looks for a settings of the name of each iterable.  The name-value
pair of this setting is then added to the template rendering context.


Can I see an example?
---------------------
Yes!  Assuming the root django-settings-context-processor is in your
PYTHON_PATH, this should work:

settings.py:

    INSTALLED_APPS = (
        ......
        'settings_context_processor',
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        # the first 5 here are the django 1.2.1 default context processors
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.contrib.messages.context_processors.messages',
        ......
        'settings_context_processor.context_processors.settings',
    )

    # define some settings we'd like to export
    CONTACT_PHONE='(555) 555-5555'
    CONTACT_EMAIL='contact@someplace.com
    CONTACT_ADDR_STREET='123 Anywhere Rd.'
    CONTACT_ADDR_CITYSTATE='Anyplace, AS 12345'

    # for settings_context_processor
    TEMPLATE_VISIBLE_SETTINGS = (
        'CONTACT_PHONE',
        'CONTACT_EMAIL',
        'CONTACT_ADDR_STREET',
        'CONTACT_ADDR_CITYSTATE',
    )


some_template.html:

    <ul class="contact">
        <li>{{ CONTACT_PHONE }}</li>
        <li><a href="mailto:{{ CONTACT_EMAIL }}">{{ CONTACT_EMAIL }}</a></li>
        <li>{{ CONTACT_ADDR_STREET }}</li>
        <li>{{ CONTACT_ADDR_CITYSTATE }}</li>
    </ul>




