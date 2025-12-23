from setuptools import find_packages,setup
from typing import List

hypen_e_dot = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    this function will return the list of requirements
    """
    requiremnts = []
    with open(file_path) as file_obj:
        requiremnts = file_obj.readlines()
        requiremnts = [req.replace('\n','') for req in requiremnts]

        if hypen_e_dot in requiremnts:
            requiremnts.remove(hypen_e_dot)
     
    return requiremnts


setup(
    name = 'ML_Project',
    version= '0.0.1',
    author= 'Emon Howlader',
    author_email= 'emonhowlader280@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('required.txt')
   
)