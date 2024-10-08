from setuptools import setup, find_packages
from typing import List 

with open("READ.md", "r", encoding="utf-8") as f: 
    long_description = f.read()

__version__ = "0.0.4"
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME = "databaseautomation"
AUTHOR_USER_NAME = "peniel18"
AUTHOR_EMAIL = "penieletornam18@gmail.com"


setup(
    name=PKG_NAME, 
    version=__version__, 
    author=AUTHOR_USER_NAME, 
    author_email=AUTHOR_EMAIL, 
    description="A python package for connecting with database.", 
    long_description=long_description, 
    long_description_content_type="text/markdown", 
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", 
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", 
    }, 
    package_dir={"": "src"}, 
    packages=find_packages(where="src")
)