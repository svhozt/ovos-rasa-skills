#!/usr/bin/env python3
import os

from setuptools import setup
from os import walk, path


URL = "https://github.com/ravindukathri/ovos-rasa-skill"
SKILL_CLAZZ = "OVOSRasaSkill"  # needs to match __init__.py class name
PYPI_NAME = "ovos-skill-rasa"  # pip install PYPI_NAME  ##Changed from ovos_rasa_skill

# below derived from github url to ensure standard skill_id
SKILL_AUTHOR, SKILL_NAME = URL.split(".com/")[-1].split("/")
SKILL_PKG = SKILL_NAME.lower().replace('-', '_')
PLUGIN_ENTRY_POINT = f'{SKILL_NAME.lower()}.{SKILL_AUTHOR.lower()}={SKILL_PKG}:{SKILL_CLAZZ}'
BASEDIR = os.path.abspath(os.path.dirname(__file__))

def required(requirements_file):
    """Read requirements file and remove comments and empty lines."""
    with open(os.path.join(BASEDIR, requirements_file), 'r') as f:
        requirements = f.read().splitlines()
        return [pkg for pkg in requirements if pkg.strip() and not pkg.startswith("#")]


with open("README.md", "r") as f:
    long_description = f.read()

def get_version():
    """Find the version of the package"""
    # Define the version of your skill here
    return "0.1.0"

setup(
    name=PYPI_NAME,
    version=get_version(),
    description='OVOS Skill for Rasa Integration',
    url=URL,  # Replace with your repository URL
    package_dir={SKILL_PKG: ""},
    packages=[SKILL_PKG],
    package_data={SKILL_PKG: required()},
    author='Your Name',
    author_email='your.email@example.com',
    license='Apache-2.0',
    zip_safe=True, #
    include_package_data=True,
    install_requires=required("requirements.txt"),
    long_description="An OVOS skill for integrating with Rasa using Socket.IO",
    long_description_content_type='text/markdown',
    keywords='ovos skill plugin',
    entry_points={'ovos.plugin.skill': PLUGIN_ENTRY_POINT}
)

