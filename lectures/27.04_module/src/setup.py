# License MIT
from setuptools import setup, find_packages
import os

DISTRO_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def extract_requirements(file):
    """
    Extract dependencies from files
    :param file: path to requirements file
    :type file: str -- list of requirements
    :return: list(str)
    """

    with open(file, 'r') as file:
        return file.read().splitlines()

setup(
    name='supertool-distro',
    version='0.1',
    description='Super super tool',
    author='FAG',
    author_email='fag@mail.com',
    license='MIT',
    classifiers=[
        'Topic :: Education',
        'Programming Language :: Python :: 3.6'
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATH, 'requirements', 'base.txt')),
    test_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATH, 'requirements', 'test.txt')),
    test_suite='nose.collector',
    bin=[os.path.join('bin', 'similar_files')],
    zip_safe=False

)
