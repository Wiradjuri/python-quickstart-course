#!/usr/bin/env python3
"""
Setup script for Python QuickStart Course
"""

from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
def read_requirements():
    """Read requirements from requirements.txt if it exists"""
    req_file = "requirements.txt"
    if os.path.exists(req_file):
        with open(req_file, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

setup(
    name="python-quickstart-course",
    version="1.0.0",
    author="Python QuickStart Team",
    author_email="contact@pythonquickstart.com",
    description="Learn Python the fastest and easiest way possible with interactive lessons and projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wiradjuri/python-quickstart-course",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.py"],
    },
    entry_points={
        "console_scripts": [
            "python-quickstart=quick_start:main",
            "pyqs=quick_start:main",
        ],
    },
    keywords="python, learning, tutorial, education, programming, beginner, course, interactive",
    project_urls={
        "Bug Reports": "https://github.com/wiradjuri/python-quickstart-course/issues",
        "Source": "https://github.com/wiradjuri/python-quickstart-course",
        "Documentation": "https://github.com/wiradjuri/python-quickstart-course#readme",
    },
)
