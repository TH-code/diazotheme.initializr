from setuptools import setup, find_packages
import os

version = '1.0'

long_description = (
    read('README.txt')
    + '\n' +
    read('plonetheme', 'h5bp', 'README.txt')
    + '\n' +
    read('CHANGES.txt')
    + '\n'
    )

setup(name='plonetheme.h5bp',
      version=version,
      description="Diazo Theme with defaults HTML5 Boilerplate",
      long_description=long_description,
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
        ],
      keywords='Diazo Theme HTML5 Boilerplate',
      author='TH-code',
      author_email='t.jonkman@gmail.com',
      url='https://github.com/TH-code',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
