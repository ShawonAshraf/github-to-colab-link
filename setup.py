from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()
setup(
    name='github-to-colab-link',
    version='1.0.1',
    author='Shawon Ashraf',
    author_email='shawon13@live.com',
    license='MIT',
    description='Generates Google Colab link for jupyter notebooks in public Github repos.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ShawonAshraf/github-to-colab-link',
    py_modules=['link', 'cli'],
    packages=find_packages(),
    install_requires=[requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        colab-link-gen=cli:run
    '''
)
