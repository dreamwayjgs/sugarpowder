from setuptools import setup, find_packages

setup(
    name="sugarpowder",
    version="0.0.1",
    description="Package of Python syntactic sugars inspired by Elixir, Go, Rust, Julia, and other languages",
    author="Geunseong Jung",
    author_email="dreamwayjgs@gmail.com",
    license="MIT License",
    package_dir={"": "src"},
    packages=find_packages("src", exclude=["test"]),
    zip_safe=False,
    install_requires=[],
)
