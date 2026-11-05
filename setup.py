from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements() -> List[str]:
    """
    This function returns the list of requirements
    """
    requirements = []

    try:
        with open("requirements.txt", "r") as file:
            requirements = file.readlines()
            requirements = [req.strip() for req in requirements]

            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)

    except Exception as e:
        print(f"Error reading requirements.txt: {e}")

    return requirements


setup(
    name="network_security",
    version="0.0.1",
    author="Sai Teja",
    author_email="your_email@example.com",
    packages=find_packages(),
    install_requires=get_requirements()
)