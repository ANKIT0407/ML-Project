from importlib.metadata import version
from setuptools import setup,find_packages
from typing import List
hypen_e = "-e ."

def get_requires(file_path:str) -> List[str]:
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if(hypen_e in requirements):
            requirements.remove(hypen_e)
    
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Ankit',
    author_email = 'aveekrrishu@gmail.com',
    packages = find_packages(),
    install_requires = get_requires('requirements.txt') 
)