import sys
from setuptools import find_packages, setup
from typing import List

# Default to creating build, dist, and wheel if no commands are passed
if len(sys.argv) <= 1:
    sys.argv += ['sdist', 'bdist_wheel']

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='DSProject',
version='0.0.1',
author='MrHamza',
author_email='hmzsattar99@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)