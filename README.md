# Metrics Labels

This code is the base to create Class-based label captures (CLC) and compare knowledge graphs based on their labeling and multilinguality.

## Data
In the data folder is the entire data needed for the comparison of KGs based on the QALD questions. 
* *qald-9-train-multilingual.json* is the original file from https://github.com/ag-sc/QALD/blob/master/9/data/qald-9-train-multilingual.json
* *all-qald-questions.json* is the file of all questions from the QALD dataset that we used in all languages provided by the dataset. They are used for the crowdsourcing evaluation
* *all-query-results.json* are the responses if the queries for each QALD question are executed on the respective KG
* *query-ids.json* is a file containing all IDs for the QALD questions 
* *classes.json* are the classes for each QALD question for the 5 KGs
* The file *all-query-results.json* contains the answer for the list of queries based on QALD.
* *Queries.pdf* are the queries to create the CLCs
* The folder *goldstandard* contains the aggregated results from the crowdsourcing evaluation for each QALD question, creating the gold standard (each question has one KG that answers the question best, if multiple KGs have the same answer, they are listed with a comma)
* The folder *rdfmt* contains the CLCs for each KG
* The folder *crowdsourcing* contains the raw aggregated data from the crowdsourcing results and the questions and answers as csv file that were used to upload on Figure Eight. Further, a jupyter notebook for the creation of those files and the evaluation of the results (including the creation of the gold standard) is included


## Create CLC (Creator)

The *Creator* module creates the CLCs based on the results of the queries in *Queries.pfd* written to a single file each. Careful! The queries for Wikidata need *a* (rdf:type) to be replaced by *wdt:P31* (Wikidata's instance of).
*\<RDFMT1\>* or *\<%s\>* need to be replaced with the respective classes of the knowledge graph, i.e., the queries will be executed once for each class.

The creation can be run using **run-rdfmt.py**, which writes the CLC files as json files to the *data/rdfmt/* folder.
 
## Compare data (Processor)

The *Processor* module can be run independently of the Creator or in a pipeline right after. It reads from the files created previously in the *data* folder.
The class *Ranker.py* creates a ranking of the datasets based on the queries of *all-query-results.json* and the CLCs, compared with just the results from the queries.

The ranking can be run using **run-ranking.py**, which writes to the *results/* folder.

The code to calculate Normalized Discounted Cumulative Gain is part of ranking-measures https://github.com/dkaterenchuk/ranking_measures 

## Graphs

The *graphs* folder contains a jupyter notebook to create figures and analyze the CLCs and the results from the ranking.
