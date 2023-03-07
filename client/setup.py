from setuptools import setup

setup(
    name='ordersystem-client',
    version='0.1.0',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests==2.28.2',
        'setuptools==67.5.1',
    ],
)
