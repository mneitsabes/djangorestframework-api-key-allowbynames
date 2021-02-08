import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="djangorestframework-api-key-allowbynames", 
    version="1.0.1",
    author="mneitsabes",
    author_email="mneitsabes@nulloz.be",
    description="A djangorestframework-api-key decorator to allow access by key names",
    long_description=long_description,
    long_description_content_type="text/markdown",
	keywords = ['django', 'djangorestframework-api-key'],
    url="https://github.com/mneitsabes/djangorestframework-api-key-allowbynames",
	packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[       
          'djangorestframework',
          'djangorestframework-api-key',
      ],
    python_requires='>=3.6',
)
