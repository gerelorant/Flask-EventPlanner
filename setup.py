from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Flask-EventPlanner',
    version='0.1',
    packages=['flask_eventplanner'],
    url='https://github.com/gerelorant/Flask-EventPlanner',
    license='MIT',
    author='Gere Lóránt',
    author_email='gerelorant@gmail.com',
    description='Event planner extension for Flask',
    install_requires=['Flask', 'Flask-SQLAlchemy'],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown'
)
