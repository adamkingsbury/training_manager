# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import re, ast

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in training_manager/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('training_manager/__init__.py', 'rb') as f:
	version = str(ast.literal_eval(_version_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	name='training_manager',
	version=version,
	description='An frappe framework app to manage training courses, training events and participant registrations.',
	author='LogiKal',
	author_email='info@logikalprojects.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
