from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in qp_information_security/__init__.py
from qp_information_security import __version__ as version

setup(
	name='qp_information_security',
	version=version,
	description='Information Security',
	author='MENTUM Group',
	author_email='aryrosa.fuentes@MENTUM.group',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
