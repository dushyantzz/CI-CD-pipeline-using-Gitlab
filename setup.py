from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="CI-CD-Pipeline-using-Gitlab",
    version="0.1",
    author="Dushyant",
    packages=find_packages(),
    install_requires = requirements,
)