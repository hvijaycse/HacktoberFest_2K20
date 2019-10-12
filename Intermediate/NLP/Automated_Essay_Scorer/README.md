# Automated_Essay_Scorer
> Deep learning & NLP based project, using word2vec model for creating word embeddings and
> using it to feed to LSTM neural network to predict the essay score awarded to a student.

# Pre-requisites
* Pandas
* Numpy
* Natural language toolkit (NLTK)
* Gensim 3.5
* Scikit-learn
* Keras 2.2.2
* Tensorflow 1.9

# Models used in training

* Linear Regressor
* Gradient Boosting Regressor
* Support Vector Regressor
* Long Short Term Memory(LSTM)

# Evaluation metric

* Mean squared error
* Variance
* Cohen's Kappa score



# Approach

Here, Word2vec model is used to generate word embeddings on which the whole model relies to predict the scores. Before generating word vectors, essays given in the essay sets are cleaned(removing stopwords, punctuations, special symbols etc.) and then word vectors are created so as to feed it to the word2vec model for generating word embeddings. After that, model is trained on various regression algorithms and each is evaluated on the basis of certain evaluation metric.


# Installation

1. Install the packages which are mentioned above using the following commands:
```
pip install keras
pip install numpy
pip install pandas
pip install sklearn
pip install gensim
pip install nltk
```
2. Run the essay_scorer.py file in jupyter notebook.
3. Have a cup of coffee and wait for the models to generate their respective mean squared error values, variances, cohen kappa scores.

**Out of all the models that were trained and tested, _LSTMs_ outperform all other models and hence the same is used to generate scores for the final dataset**.

# References
* [Check out this awesome article on word2vec model](https://medium.com/explore-artificial-intelligence/word2vec-a-baby-step-in-deep-learning-but-a-giant-leap-towards-natural-language-processing-40fe4e8602ba)
* [Check out this awesome article on Cohen's Kappa Score](https://towardsdatascience.com/inter-rater-agreement-kappas-69cd8b91ff75)
* [Automatic Text Scoring Using Neural Networks](https://arxiv.org/pdf/1606.04289.pdf)
* [A Neural Approach to Automated Essay Scoring](http://aclweb.org/anthology/D/D16/D16-1193.pdf)
