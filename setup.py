from setuptools import setup

setup(name = 'codecheck',
	version = '1.0',
	description = 'Checker scripts for basic_level files',
	url = 'https://github.com/BergelsonLab/codecheck',
	author = 'Estelle He, Selen Berkman',
	packages = ['codecheck'],
        install_requires=['msgpack', 'distance', 'argparse'],
	include_package_data=True
        )
