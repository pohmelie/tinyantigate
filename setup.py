from setuptools import setup

import tinyantigate


with open("README.md") as fin:

    long_description = fin.read()

setup(
    name="tinyantigate",
    version=tinyantigate.__version__,
    description=("Tiny antigate/anti-captcha api wrapper."),
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    author="pohmelie",
    author_email="multisosnooley@gmail.com",
    url="https://github.com/pohmelie/tinyantigate",
    license="WTFPL",
    packages=["tinyantigate"],
    install_requires=["requests"],
    include_package_data=True
)
