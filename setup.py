from setuptools import setup, find_packages

setup(
    name="pypacm",
    version="1.0",
    author="ethanmal30",
    description="A command-line package manager CLI for Python.",
    packages=find_packages(),
    install_requires=[
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "pypacm = pypacm.__main__:main",
        ],
    },
    python_requires=">=3.13",
)