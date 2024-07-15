from setuptools import setup, find_packages

with open("README.md", 'r') as f:
	long_description = f.read()

with open("requirements.txt", "r") as fh:
    requires = [line for line in fh.read().splitlines() if line != ""]

setup(
	name='PassioGo',
	version="0.2.0",
	description="An unofficial API for Passio Go",
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='Andrei Thuler',
	author_email='info@andreithuler.com',
	url="https://github.com/athuler/PassioGo",
	packages=find_packages(),
	py_modules=find_packages(),
	install_requires=requires,
	project_urls = {
		'Documentation': 'https://passiogo.readthedocs.io/',
		'GitHub': 'https://github.com/athuler/PassioGo',
		'Support':'https://github.com/sponsors/athuler',
		'Changelog':'https://github.com/athuler/PassioGo/blob/main/CHANGELOG.md',
	},
)