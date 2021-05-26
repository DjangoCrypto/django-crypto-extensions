import os
import sys

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

with open(
        os.path.join(os.path.dirname(__file__), "requirements.txt")
) as requirements_txt:
    requirements = requirements_txt.read().strip().splitlines()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

version = __import__("django_crypto_extensions").__version__

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

setup(
    name="django-crypto-extensions",
    version=version,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    license="MIT",
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
