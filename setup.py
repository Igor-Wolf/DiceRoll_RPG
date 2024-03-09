from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="diceroll_RPG",
    version="0.0.1",
    author="Igor Reis Barbosa",
    description="An application to roll dices",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Igor-Wolf/DiceRoll_RPG/tree/main",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.1',
)