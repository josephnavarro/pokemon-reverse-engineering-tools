try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# for uploading to pypi
# if sys.argv[-1] == 'publish':
#     os.system('python setup.py sdist upload')
#     sys.exit()

# There's some intersection with requirements.txt but pypi can't handle git
# dependencies.
requires = [
    "mock",
    "nose",
    "vba_wrapper==0.0.2",
]

setup(
    name="pokemontools",
    version="1.6.1a",
    description="Tools for compiling and disassembling Pokémon Red and Pokémon Crystal.",
    long_description=open("README.md", "r").read(),
    license="BSD",
    author="Joey Navarro",
    author_email="",
    url="https://github.com/josephnavarro/pokemon-reverse-engineering-tools",
    packages=[
        "pokemontools",
        "redtools",
    ],
    package_dir={
        "pokemontools": "pokemontools",
        "redtools": "redtools"
    },
    include_package_data=True,
    install_requires=requires,
    platforms="any",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
    ]
)
