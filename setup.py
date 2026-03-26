from setuptools import setup, find_packages

setup(
    name="wordle",
    version="0.2.6",
    description="",
    url="https://github.com/Jah135/wordle",
    author="Elijah Hopper",
    license="MIT",
    packages=find_packages(),
    # package_data={"": ["*.txt"]},
    # include_package_data=True,
    python_requires=">=3.12",
    install_requires=["pyansi @ git+https://github.com/Jah135/pyansi.git"],
)
