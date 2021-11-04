import setuptools
from distutils.core import setup
setup(
    name = 'linenotify',
    packages = ['linenotify'],
    version = '1.0.0',
    license = 'MIT',
    description = 'Easy Line-Notify syntax',
    author = 'Borworntat Dendumrongkul',
    author_email = 'borworntat.d@gmail.com',
    url = 'https://github.com/MasterIceZ/LineNotify',
    download_url = 'https://github.com/MasterIceZ/LineNotify/archive/v_100.tar.gz',
    keywords = ["LINE"],
    install_requires=[
        'requests'
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ]
)
