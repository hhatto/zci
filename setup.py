#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import zci

setup(
    name='zci',
    version=zci.__version__,
    description="Zsh Completion function Installer",
    #long_description=open("README.rst").read(),
    license='MIT',
    author='Hideo Hattori',
    author_email='hhatto.jp@gmail.com',
    url='https://github.com/hhatto/zci',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Operating System :: Unix',
        'Programming Language :: Unix Shell',
    ],
    install_requires=['requests', 'PyYAML'],
    py_modules=['zci'],
    zip_safe=False,
    entry_points={'console_scripts': ['zci = zci:main']},
)
