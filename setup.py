from setuptools import setup, find_packages

setup(
    name='ChromeFetcher',
    version='0.0.9',
    author='Eugene Evstafev',
    author_email='chigwel@gmail.com',
    description='Automatically fetches and downloads the appropriate Chrome version based on OS and architecture.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chigwell/ChromeFetcher',
    packages=find_packages(),
    install_requires=[
        'requests',
        'osarch==0.0.2',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
