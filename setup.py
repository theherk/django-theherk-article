import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-theherk-article',
    version='1.5',
    packages=find_packages(),
    include_package_data=True,
    license='see file LICENSE',
    description='django CMS plugin to post a simple article',
    long_description=read('README.md'),
    url='https://github.com/theherk/django-theherk-article',
    author='Adam Sherwood',
    author_email='theherk@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
