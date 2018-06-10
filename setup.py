from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='sample',
      version='1.0',
      description='Python Distribution Utilities',
      long_description=readme,
      author='Anubhav Jain',
      author_email='anubhavj880@gmail.com',
      url='https://github.com/anubhavj880/sample',
      license=license,
      packages=['package1', 'package2', 'package1.subpackage1_1', 'package2.subpackage2_1'],
      py_modules=['home']
      )
