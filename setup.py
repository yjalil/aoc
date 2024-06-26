from setuptools import setup, find_packages

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(
    name = 'aoc',
    description= 'My solutions to aoc challenges',
    packages = find_packages(['api']),
    install_requires=requirements
)
