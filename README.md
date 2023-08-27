# Automatic_corpora_generation_and_statistical_analysis_of_texts
This quantitative linguistics project consists of two parts: database generation of input texts and their statistical analysis.
Script for database generation can receive multiple text files, but we provided 2 texts of different genres for this task - "History of Ukraine-Rus" by Mykola Arkas and translation of the Bible into Ukrainian by Ivan Ohiienko. The newly created databases consist of the following columns: word_id, word, lemma, pos (part of speech tag), and sent_number (number of the sentence in which a particular word appears). The approximate number of rows (records) in each database is 23000. Besides word dictionaries, frequency dictionaries were generated for these texts. The first frequency dictionary, which can be found in 'pos_freq' table, depicts frequencies for different parts of speech (14 in total + NONE tag) in 20 subsamples with 1000 words each. Another frequency dictionary can be found in 'word_info' table and it depicts the frequencies of each word in each subsample (again, each subsample is 1000 words, number of subsamples is 20, 20000 words in total were analyzed).
Files in this repository:
* dictionary_generator.py - script for database generation
* text_statistics.py - script for statistical analysis of input texts. Characteristics evaluated using this script:
1. absolute frequency
2. mean frequency
3. relative error
4. standard deviation
5. confidence interval 95%
6. coefficient of variation of mean frequency
7. confidence interval 99%
8. coefficient of variation
9. maximum coefficient of variation
10. coefficient of stability
11. relative error
12. standard error
* texts - input text file in .txt format
* db - folder for saving newly generated databases
* statistics - folder for saving newly generated .csv files containing text statistics
* requirements.txt - modules required to be installed for this project

    
