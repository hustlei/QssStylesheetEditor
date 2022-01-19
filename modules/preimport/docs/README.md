# install 

~~~
pip install -U sphinx sphinx-autobuild
~~~

# generate docs

~~~shell
cd docs
sphinx-apidoc -Mfo source ../preimport/
sphinx-build -b html source build
~~~

or

~~~
cd docs
sphinx-apidoc -Mfo source ../preimport/
make clean
make html
~~~


sphinx-apidoc generate rst docs from python source code.

sphinx-build build rst docs to html or other format.