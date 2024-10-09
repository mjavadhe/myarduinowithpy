from setuptools import setup, find_packages

setup(
    name='myarduinowithpy',
    version='1.0',
    packages=find_packages(),
    install_requires=[],  #No Prerequisites
    description='A Python package to program and control Arduino without external dependencies.',
    author='Mohamadjavad Heydarpanah',
    author_email='mjavad.heydarpanah@gmail.com',
    url='https://github.com/mjavadhe/arduinopy',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
