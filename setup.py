from setuptools import setup, find_packages

# Utility function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line and not line.startswith('#')]

setup(
    name='mi_py_test',               # Replace with your package's name
    version='0.1.1',
    packages=find_packages(),        # Automatically find sub
    install_requires=parse_requirements('requirements.txt'),
    author='Michael Mueller',
    author_email='michaelmuelleronline@gmx.de',
    description='Custom testing library for python',
    url='https://github.com/MichaelMueller/mi_py_test_lib.git',  # Link to your repository
)
