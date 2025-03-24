from Cython.Build import cythonize
from setuptools import Extension, setup

extensions = [
    Extension("allocation.optimized", ["cython/allocation/optimized.py"]),
    Extension("loop.optimized", ["cython/loop/optimized.py"]),
    Extension(
        "lettercount.optimized",
        ["cython/lettercount/optimized.py"],
        language="c++",
    ),
    Extension(
        "pi.optimized",
        ["cython/pi/optimized.py"],
        extra_compile_args=["-fopenmp"],
        extra_link_args=["-fopenmp"],
        define_macros=[
            ("CYTHON_PROFILE", "1"),
            ("CYTHON_TRACE", "1"),
            ("CYTHON_TRACE_NOGIL", "1"),
        ],
    ),
]

setup(
    ext_modules=cythonize(extensions, annotate=True),
)
