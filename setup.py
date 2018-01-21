"""
Schema Macros
----------------

Jinja2 enhanced SQL

"""

from setuptools import setup, find_packages


setup(
    name='schemamacros',
    version='0.2.0',
    url='https://github.com/caj-larsson/schemamacros',
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
        'Click',
        'attrs',
        'jinja2',
        'pyaml'
    ],
    entry_points='''
        [console_scripts]
        sm-compile=schemamacros.cli:compile_schema
    ''',
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
