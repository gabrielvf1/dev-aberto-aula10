from setuptools import setup
setup(name='dev_aberto_gabrielvf',
version='0.1',
author='gabrielvf',
classifiers=['Operating System :: MacOS :: MacOS X', 'Operating System :: Microsoft :: Windows', 'Operating System :: POSIX', 'Programming Language :: Python'],
install_requires=[
'requests'
],
scripts=['scripts/hello.py'],
packages=['dev_aberto']
)
