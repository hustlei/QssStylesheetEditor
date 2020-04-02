# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def myversion():
    from setuptools_scm.version import guess_next_version, _bump_regex, _strip_local

    def local_scheme(version):
        return ""
        # return ".{}".format(version.distance)#version.format_choice(".{distance}","") if version.distance else ""
        # return version.format_choice(".r{distance}", ".a{distance}") if version.distance else ""
        # return version.format_choice(".d{time:%Y%m%d}", ".{distance}.{node}.{time:%Y%m%d}")
        # return ".dev{}".format(version.distance)
    def version_scheme(version):
        verstr = str(version.tag)
        ver = verstr.split(".")
        if ver[2] != "0":
            return "{}.{}".format(verstr, version.distance)
        else:
            return "{}.{}.{}".format(ver[0],ver[1],version.distance)
        # return guess_next_version(version.tag)

    return {'version_scheme': version_scheme, 'local_scheme': local_scheme}


with open("README.md", "r", encoding='utf-8') as fh:
    long_desc = fh.read()

setup(
    name="preimport",
    setup_requires=['setuptools_scm'],
    # version="1.0",
    use_scm_version=myversion,
    python_requires='>=2.7.*',
    # src_root = ".",
    package_dir={'': '.'},
    packages=find_packages(include=['preimport']),
    # include_package_data = True,
    # package_data={'':['']},
    # data_files = [('Lib/site-packages/preimport', ['README.md'])],

    # metadata to display on PyPI
    author='lileilei',
    author_email='hustlei@sina.cn',
    description="Preimport python modules to accelerate running speed.",
    keywords="preimport",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/hustlei/preimport",
    project_urls={"Source Code": "https://github.com/hustlei/preimport"},
    classifiers=[
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python", "Operating System :: OS Independent"
    ])

# python setup.py bdist_wheel
# pip install xx.whl
# or
# python setup.py sdist
# python setup.py install
