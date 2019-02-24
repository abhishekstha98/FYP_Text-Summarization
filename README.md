# FYP_Text-Summarization Using Bleu

## Commiters
  Abhishek Krishna Shrestha
  Japneet Dhaliwal
  Dhannanjai Nautiyal
  
### Extractive Summarization
  Extractive summarization of wikipedia contents. It is done by calculating the BLEU scores of each sentence (using individual N-Gram 
  scores).
 
### BLEU
  The Bilingual Evaluation Understudy Score, or BLEU for short, is a metric for evaluating a generated sentence to a reference sentence.

  A perfect match results in a score of 1.0, whereas a perfect mismatch results in a score of 0.0.

  The score was developed for evaluating the predictions made by automatic machine translation systems. It is not perfect, but does offer   5 compelling benefits:

  It is quick and inexpensive to calculate.
  It is easy to understand.
  It is language independent.
  It correlates highly with human evaluation.
  It has been widely adopted.
  The BLEU score was proposed by Kishore Papineni, et al. in their 2002 paper “BLEU: a Method for Automatic Evaluation of Machine         
  Translation“. *https://machinelearningmastery.com/calculate-bleu-score-for-text-python/*
  
  **Individual N-Gram Scores**
  An individual N-gram score is the evaluation of just matching grams of a specific order, such as single words (1-gram) or word pairs (2-
  gram or bigram).

  The weights are specified as a tuple where each index refers to the gram order. To calculate the BLEU score only for 1-gram matches, you 
  can specify a weight of 1 for 1-gram and 0 for 2, 3 and 4 (1, 0, 0, 0).
  
 ### This was performed using the nltk library in python
 
 
