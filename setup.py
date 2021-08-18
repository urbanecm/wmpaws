"""
wmpaws
-------------

This is the description for that library
"""
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='wmpaws',
    version='0.1',
    license='GNU',
    author='Martin Urbanec',
    author_email='martin@urbanec.cz',
    description='To be done',
    long_description=long_description,
    long_description_content_type='text/markdown',
    py_modules=['wmpaws'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'pymysql',
        'pandas'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
