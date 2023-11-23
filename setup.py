#!/usr/bin/env python3
import os

from setuptools import setup

BASEDIR = os.path.abspath(os.path.dirname(__file__))

def required(requirements_file):
    """Read requirements file and remove comments and empty lines."""
    with open(os.path.join(BASEDIR, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        return [pkg for pkg in requirements if pkg.strip() and not pkg.startswith("#")]

def get_version():
    """Find the version of the package"""
    # Define the version of your skill here
    return "0.1.0"

setup(
    name='rasa-skill',
    version=get_version(),
    description='OVOS Skill for Rasa Integration',
    url='https://github.com/YourGitHub/rasa-skill',  # Replace with your repository URL
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    packages=['rasa_skill'],  # Replace with the name of your skill's Python package
    zip_safe=True,
    install_requires=required("requirements.txt"),
    long_description="An OVOS skill for integrating with Rasa using Socket.IO",
    long_description_content_type='text/markdown',
    entry_points={}
)

