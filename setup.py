import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()
	
setuptools.setup(
	name="example-pkg-markonieme", # Replace with your own username
	version="0.0.1",
	author="Marko Niemelä",
	author_email="marko.p.niemela@jyu.fi",
	description="A small example package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/markonieme/example_pkg",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.5',
)
