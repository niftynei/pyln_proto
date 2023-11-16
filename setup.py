# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyln.proto', 'pyln.proto.message']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyln-proto',
    'version': '23.5.2',
    'description': 'Protocol Library for the Lightning Network',
    'author': 'Christian Decker',
    'author_email': 'decker.christian@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
