import sys, os
from distutils.core import setup

sys.path.insert(0, '.')


def is_package(path):
    return os.path.isfile(os.path.join(path, '__init__.py'))


def find_packages(root):
    """Find all packages under this directory"""
    for path, directories, files in os.walk(root):
        if is_package(path):
            yield path.replace('/', '.')


setup(
    name='OpenGLCffi',
    version='0.1dev',
    author='C. Denizol',
    author_email='cdenizol@gmail.com',
    packages=list(find_packages('OpenGLCffi')),
    url='http://github.com/cydenix/OpenGLCffi',
    license='LICENSE',
    description='OpenGL Cffi ABI for Python 2.7',
    long_description=open('README.md').read(),
    install_requires=["python2-xcffib"],
)
