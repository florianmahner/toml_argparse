try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name="toml_argparse",
    version="0.0.1",
    author="Florian P. Mahner",
    author_email="florian.mahner@gmail.com",
    license="LICENSE",
    install_requires=["toml"],
    long_description=open("README.md").read(),
    packages=find_packages(),
    python_requires=">=3.7",
)