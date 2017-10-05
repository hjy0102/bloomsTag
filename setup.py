from setuptools import setup

setup(
    name='bloomsTag',
    version='0.1',
    py_modules=['blooms'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        blooms=blooms:cli
    ''',

)