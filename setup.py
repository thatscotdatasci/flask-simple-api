try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('packages.dat') as f:
    packages = f.readlines()
packages = [s.strip() for s in packages]


setup(
    name='flaskapi',
    version=open('version.txt').read().strip(),
    packages=packages,
    description='Simple API written in Flask to test various AWS features',
    author='Alan Clark',
    author_email='alan@thatscotdatasci.com',
    url='thatscotdatasci.com',
    platforms='linux',
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').read()
)
