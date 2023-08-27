# Automatic_corpora_generation_and_statistical_analysis_of_texts
This quantitative linguistics project is aimed at automatic generation of word databases. Script for datanase generation can receive multiple text files, but we provided 2 texts of different genres for this task - "History of Ukraine-Rus" by Mykola Arkas and translation of the Bible into Ukrainian by Ivan Ohiienko. The newly created databases consists of the following columns: word_id, word, lemma, pos (part of speech tag) and sent_number (number of the sentence in which a particular word appears). The approximate number of rows (records) in a database is 23000. Beside word dictionaries, frequency dictionaries were generated for these texts. The first frequency dictionary, which can be found in 'pos_freq' table depicts statistics for different parts of speech (14 in total + NONE tag) for 20 subsamples with 1000 words each. Another frequency dictionary can be found in 'word_info' table and it depicts the number each word occurs in each subsample (again, each subsample is 1000 words, number of subsamples is 20).
text_statistics.py is a script for evaluating different statistical characteristics of the given texts. These characteristics include: 
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
    
