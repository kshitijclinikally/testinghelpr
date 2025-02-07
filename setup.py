from setuptools import setup, find_packages

def read_requirements(file):
    """Read requirements file and return a list of dependencies."""
    with open(file, encoding="utf-8") as f:
        return f.read().splitlines()

def read_file(file):
    """Read a file and return its contents."""
    with open(file, encoding="utf-8") as f:
        return f.read().strip()

# Read metadata files
long_description = read_file("README.rst")
version = read_file("VERSION")
requirements = read_requirements("requirements.txt")

setup(
    name="helpr",
    version=version,
    author="Clinikally",
    author_email="kshitijsrivastava@clinikally.com",
    url="https://github.com/kshitijclinikally/testinghelpr",
    description="A Python package to help you with your daily tasks",
    long_description=long_description,
    long_description_content_type="text/x-rst",  # Ensure correct rendering on PyPI
    license="MIT license",
    packages=find_packages(exclude=["tests", "docs"]),  # Exclude unnecessary directories
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Specify supported Python versions
)
