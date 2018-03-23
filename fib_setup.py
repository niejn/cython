from distutils.core import setup
from Cython.Build import cythonize
import Cython.Compiler.Options
Cython.Compiler.Options.annotate = True
from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'MyProject',
  ext_modules = cythonize(["*.pyx"]),
)
#python fib_setup.py build_ext --inplace

