#!/usr/bin/env python

from distutils.core import setup

setup(name='Tuenti library',
      version='0.1',
      description='Python library for tuenti interact',
      author='David Francos Cuartero (XayOn), Ruben Lopez Angos (Ruffo)',
      author_email='xayon@xayon.net, ruben.lopez.angos@gmail.com',
      url='http://xayon.github.com/tuenti',
      packages=['tuenti'],
      requires=['mechanize','BeautifulSoup','re','urllib','thread']
     )
