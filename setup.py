
from distutils.core import setup

setup(
    name='django-settings-context-processor',
    version='0.2',
    description='Makes specified django settings visible in template rendering context.',
    author='Mike Fogel',
    author_email='mike@fogel.ca',
    url='http://github.com/carbonXT/django-settings-context-processor',
    packages=['settings_context_processor'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
) 
