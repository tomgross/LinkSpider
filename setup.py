from setuptools import find_packages
from setuptools import setup


try:
    README = open('README.rst').read()
except IOError:
    README = None

setup(
    name='linkspider',
    version="1.0.0",
    description='An asyncronous linkchecker written in Python 3',
    long_description=README,
    install_requires=[
        'guillotina',
        'httpie'
    ],
    author='Tom Gross',
    author_email='itconsense@gmail.com',
    url='',
    packages=find_packages(exclude=['demo']),
    include_package_data=True,
    tests_require=[
        'pytest',
    ],
    extras_require={
        'test': [
            'pytest'
        ]
    },
    classifiers=[],
    entry_points={
    }
)
