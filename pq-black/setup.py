from setuptools import setup, find_packages

setup(
    name="pq-black",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pq-black=pq_black.cli:main",
        ],
    },
)
