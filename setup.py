from setuptools import setup, find_packages
PROJECT_NAME = 'NeuraGraphServer'
VERSION = '0.0.1'

setup(name=PROJECT_NAME,
      version=VERSION,
      entry_points={
          'console_scripts': [
              'manager = manager:main'
          ]
      },
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests==2.27.1',
          'pandas==1.4.1',
          'numpy==1.22.3',
      ],
      zip_safe=False
)