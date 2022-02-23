import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pyutil",
    version="1.0.0",
    author="Koki NAKAMURA",
    author_email="koki.nakamura22@gmail.com",
    description="original python utility",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/koki-nakamura22/pyutil/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: Apache License 2.0",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
