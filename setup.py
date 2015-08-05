import setuptools

setuptools.setup(
    name="piianalyzer",
    version="0.1.0",
    url="https://github.com/github/piianalyzer",

    author="Savio Abuga",
    author_email="savioabuga@gmail.com",

    description="Analyzing PII in datasets",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['commonregex>=1.5.4',
                      'nltk>=3.0.4',
                      'pandas-0.16.2'
                      ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
