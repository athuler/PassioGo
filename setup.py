from setuptools import setup, find_packages
from passiogo import __version__

with open("README.md", 'r') as f:
	long_description = f.read()

with open("requirements.txt", "r") as fh:
    requires = [line for line in fh.read().splitlines() if line != ""]

setup(
	name='PassioGo',
	version=__version__,
	description="Tracking the Performance of UChicago's Shuttle Network",
	long_description=long_description,
	author='Andrei Thuler',
	author_email='info@andreithuler.com',
	url="https://github.com/athuler/PassioGo",
	packages=find_packages(),
	py_modules=find_packages(),
	install_requires=requires,
	project_urls = {
		'Documentation': 'https://passiogo.readthedocs.io/',
		'GitHub': 'https://github.com/athuler/PassioGo'
	},
)