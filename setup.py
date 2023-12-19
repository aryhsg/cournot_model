from setuptools import setup, find_packages

setup(
    name='simple_Cournot_model',
    version='1.0.0',
    author='Yang, Ching-Yu',
    author_email='kevin81815@email.com',
    description='Test',
    packages=find_packages(),
    install_requires=[
        'numpy',
        "sympy",
        "matplotlib"  
    ],
)
