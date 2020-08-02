import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="firetabs",
    version="0.0.1",
    author="rokie95",
    author_email="motiurga@gmail.com",
    description="Gets tab information from Firefox 55+",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rokie95/firetabs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
