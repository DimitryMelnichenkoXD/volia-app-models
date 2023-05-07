from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='volia_app_models',
    version='0.1',
    author='Dmitry Melnichenko',
    description='Base models for volia app',
    packages=find_packages(),
    install_requires=requirements
)
