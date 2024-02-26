from setuptools import find_packages,setup
from typing import List

Hyphen = '-e .'
def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if Hyphen in requirements:
            requirements.remove(Hyphen)
            
        return requirements
    
setup(
    name = "Flight_Fare",
    version = "0.0.1",
    author="Abhishek Singh",
    author_email = "a.singh.gla@gmail.com",
    packages = find_packages(),
    install_requirements = get_requirements('requirements.txt')
)