"""A setuptools based setup module."""

from setuptools import setup, find_packages


with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = "gem5art",
    version = "0.1.0",
    description = "An artifact, reproducibility, and testing library for gem5",
    long_description = long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/darchr/gem5art',
    author='Davis Architecture Research Group (DArchR)',
    author_email='jlowepower@ucdavis.edu',
    license='BSD',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Topic :: System :: Hardware',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        ],
    keywords='simulation architecture gem5',
    packages=find_packages(),
    install_requires=['pymongo'],
    python_requires='>=3.6',
    extras_require={
         'celery': ['celery', 'flower'],
    },
    project_urls={
        'Bug Reports':'https://github.com/darchr/gem5art/issues',
        'Source':'https://github.com/darchr/gem5art',
        'Documentation':'https://gem5art.readthedocs.io/en/latest/',
    }
)
