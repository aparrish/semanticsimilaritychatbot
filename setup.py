import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="semanticsimilaritychatbot",
    version="0.0.1",
    author="Allison Parrish",
    author_email="allison@decontextualize.com",
    description="A little chatbot based on semantic similarity",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aparrish/semanticsimilaritychatbot",
    packages=setuptools.find_packages(),
    install_requires=[
        'simpleneighbors',
        'spacy',
        'numpy'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
