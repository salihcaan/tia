from setuptools import setup

setup(
    name='tia',
    version='0.0.1',
    description='converted via lib from python2 to python3',
    url='git@github.com:salihcaan/tia.git',
    author='Salih Can',
    author_email='hasansalihcan@gmail.com',
    license='unlicense',
    install_requires=['numpy', 'matplotlib', 'pandas', 'seaborn', 'reportlab',
                      'pywin32', 'win32com', 'blpapi', 'pdfrw'],
    packages=['tia'],
    zip_safe=False
)




