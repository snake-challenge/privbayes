from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension

setup(
    name="privbayes",
    ext_modules=cythonize(
        Extension(
            "privbayes",
            sources=[
                "privbayes.pyx",
                "lib/methods.cpp",
                "lib/table.cpp",
                "lib/noise.cpp",
                "lib/translator.cpp",
            ],
            language="c++",
            extra_compile_args=["-std=c++14"],
            extra_link_args=["-std=c++14"],
        ),
        language_level=3,
    ),
)
