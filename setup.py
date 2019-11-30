# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="preimport",
    setup_requires=['setuptools_scm'],
    # version="1.0",
    use_scm_version=True,
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
    url="https://github.com/hustlei/preimport",
    project_urls={"Source Code": "https://github.com/hustlei/preimport"},
    classifiers=[
        "License :: OSI Approved :: GNU LESSER GENERAL PUBLIC LICENSE v2.1 (LGPLv2.1)",
        "Programming Language :: Python",
        "Operating System :: OS Independent"
    ]
)

# python setup.py bdist_wheel
# pip install xx.whl
#or
# python setup.py sdist
# python setup.py install