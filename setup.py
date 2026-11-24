from setuptools import setup, find_packages
from typing import List


def get_requirements(file_path: str) -> List[str]:
    """Read requirements from a file and return them as a list."""
    requirements_list::List[str] = []

    try:
        #Open and read the requirements.txt file
        with open("requirements.txt", 'r') as file:
            #Read lines from the file and filter out empty lines and comments
            lines = file.readlines()
            #Process each line
            for line in lines:
                #strip whitespace and new line characters
                requirement = line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")


    return requirements_list
print(get_requirements())
setup(
    name="AI-Travel-Planner",
    version='0.0.1',
    author="Vasundhara Kaushal",
    author_email="vasundharakaus2000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)