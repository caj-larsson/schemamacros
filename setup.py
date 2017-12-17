"""
Schema Macros
----------------

Jinja2 enhanced SQL

"""

from setuptools import setup, find_packages


setup(
    name='schemamacros',
    version='0.0.1',
    url='http://',
    license='MIT',
    author='Caj Larsson',
    author_email='contact@caj.me',
    description='Template SQL',
    long_description=__doc__,
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'attrs',
        'jinja2',
        'pyaml'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
