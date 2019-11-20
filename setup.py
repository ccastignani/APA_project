from setuptools import setup

setup(
    name='morphocell',
    version='0.1.0',
    description='A nearest neighbour search for morphological image files',
    keywords='cell-image kd-tree morphology',
    packages=['morphocell', 'morphocell.test'],
    scripts=['bin/morphocell'],
    license='GNU GPLv3',
    long_description=open('README.md').read(),
    install_requires=[
        "argparse",
        "numpy",
        "pytest",
        "pytest-cov",
        "coverage"
    ],
    python_requires='>=3',
)
