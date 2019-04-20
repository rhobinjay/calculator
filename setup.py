from setuptools import setup, find_packages


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='calculator-rhobinjay',
    version='0.1.4',
    description='Performs addition and subtraction.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rhobinjay/calculator',
    author='Rhobin Jay Faigones',
    author_email='rhobinjayfaigones@gmail.com',
    packages=find_packages(exclude=['docs', 'tests']),
    entry_points={
        'console_scripts': [
            'calculator=calculator.cli:main',
        ],
    },
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
