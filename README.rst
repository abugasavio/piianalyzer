piianalyzer
===========
Analyzing PII in datasets


Task: Having an automated routine that classifies datasets and resources into ‘PII’ and ‘Not PII’.
===========

The task requires creation of a tool that will detect whether new datasets uploaded to HDX contain any personally
identifiable information - data that can be used on its own or with other information to identify, contact, or
locate a single person, or to identify an individual in context. Examples of PII.

The tool should then alert the HDX data manager whether any such data sets have been uploaded
and also alert the data owner about this.

Solution
---

I decided to use the following tools for the above task:

1. pandas for reading the data files into python and manipulating the datasets.

2. [Common Regular expressions](https://github.com/madisonmay/CommonRegex) for extracting some types of 'PII' such as email addresses, phone numbers, street addresses,
   credit card numbers,

3. [Stanford Named Entity Tagger](http://nlp.stanford.edu/software/CRF-NER.shtml) for extracting the locations, organizations and peoples names.


The analyzer opens the provided file and checks scans returns a summary of the types of data that are in the provided dataset.
With this information the data manager can easily classify the data.


Usage
-----


>>> from piianalyzer.analyzer import PiiAnalyzer
>>> filepath = '/path/pr/url/to/your/file.csv'
>>> piianalyzer = PiiAnalyzer(filepath)
>>> analysis = piianalyzer.analysis()



Installation
------------



Requirements
^^^^^^^^^^^^

Requires the Standford Tagger models.
They can be downloaded from http://nlp.stanford.edu/software
and the STANFORD_MODELS environment variable set (a colon-separated list of paths).

Compatibility
-------------

Licence
-------

TODO
----




Authors
-------

`piianalyzer` was written by `Savio Abuga <savioabuga@gmail.com>`_.
