import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

with open(
    os.path.join(os.path.dirname(__file__), "requirements.txt")
) as requirements_txt:
    requirements = requirements_txt.read().strip().splitlines()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django_crypto_extensions",
    version="0.0.1",
    packages=["django_crypto_extensions", "django_crypto_extensions.runtests"],
    include_package_data=True,
    license="Apache-2.0",
    license_files=["LICENSE"],
    description="Extensions for Django in terms of Cryptography.",
    long_description=README,
    long_description_content_type="text/markdown",
    author="DjangoCrypto",
    author_email="kamil1marczak@gmail.com",
    url="https://github.com/DjangoCrypto/django-crypto-extensions",
    python_requires=">=3.6",
    install_requires=requirements,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
