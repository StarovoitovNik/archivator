import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="archiver",
    version="1.0.2",
    author="Nikita Starovoitov",
    author_email="nikita.starr02@gmail.com",
    description="Package for archiving files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StarovoitovNik/archivator",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 7",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
