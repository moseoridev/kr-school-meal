import setuptools

with open("README.md", "r", encoding='UTF8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="kr_school_meal",
    version="0.0.1",
    author="moseoridev",
    author_email="sjssjs1344@gmail.com",
    description="Korea School Meal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/moseoridev/korea-school-meal",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Natural Language :: Korean"
    ],
    python_requires='>=3.6',
)
