import pathlib
from setuptools import setup, find_packages
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(name='pkg_builder',
      version="1.1.2",
      # Below to deal with cleaner versionning
      #setup_requires=['setuptools_scm'],
      #install_requires=['setuptools_scm'],
      #use_scm_version={'write_to': 'pkg_builder/version.txt'},
      description="Package builder with CI included",
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/lologibus2/wagon_tools",
      author='Jean Bizot', author_email="jea@gmail.com",
      packages=find_packages(),
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/build-package'],
      zip_safe=False)
