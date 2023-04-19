from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='PyDataOpsKit',
    version='1.0.1',
    packages=['PyDataOpsKit'],
    url='',
    license='',
    author='Oli Eugenio',
    author_email='',
    description='',
    install_requires=requirements,
)