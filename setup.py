#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="django-auth-kerberos",
    version="1.2.1",
    description="Kerberos authentication backend for Django",
    long_description="Kerberos authentication backend for Django",
    url="https://github.com/02strich/django-auth-kerberos",
    author="Stefan Richter",
    author_email="stefan@02strich.de",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["django", "kerberos", "authentication", "auth"],
    packages=find_packages(exclude='tests'),
    install_requires=[
        'Django>=1.6',
        'kerberos==1.1.1',
    ],
)
