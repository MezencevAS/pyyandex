  
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = ['six', 'requests>2.4.0', 'future']

setup_requirements = ['six', 'requests>2.4.0', 'future']

test_requirements = ['six', 'requests>2.4.0', 'future']

setup(
    name='proxyyandexpy',
    version='1.0.1',
    author="Levent Duivel",
    include_package_data=True,
    packages=find_packages(),
    install_requires=requirements,
    setup_requires=setup_requirements,
    tests_require=test_requirements,
)
