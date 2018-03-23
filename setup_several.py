# several files with ext .pyx, that i will call by their name
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[
    Extension("primes",       ["primes.pyx"]),
    Extension("spam",         ["spam.pyx"]),

]

setup(
  name = 'MyProject',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules,
)

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["folder1/file1.pyx", "folder2/file2.pyx"])
)