django-settings-context-processor
---------------------------------


What does it do?
---------------
Makes specified django settings visible in template rendering context.


How does it do it?
------------------
It takes the setting variable TEMPLATE_VISIBLE_SETTINGS, which should
be an iterable of strings, and looks for a settings of that name.  If it
finds one, it places it in the template rendering context.


Can I see an example?
---------------------
Yup, here's the key parts of a settings.py:

TODO: fill me in.

