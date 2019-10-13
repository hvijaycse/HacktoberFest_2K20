
# coding: utf-8

# In[1]:


# importing required packages

import pandas as pd
import numpy as np
import nltk
import re
from nltk.corpus import stopwords
from gensim.models import Word2Vec
from sklearn.cross_validation import KFold
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn import ensemble
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
from sklearn.metrics import cohen_kappa_score
from keras.layers import Embedding, LSTM, Dense, Dropout, Lambda, Flatten
from keras.models import Sequential, load_model, model_from_config
import keras.backend as K


# In[2]:


importing_dataset = pd.read_csv('training_set_rel3.tsv', sep='\t', encoding='ISO-8859-1')

# dependent variable
scores = importing_dataset['domain1_score']
dataset = importing_dataset.loc[:,['essay_id', 'essay_set', 'essay', 'domain1_score']]


# In[3]:


# Generating word tokens after removing characters other than alphabets, converting them to lower case and
# removing stopwords from the text'''

def word_tokens(essay_text):
    essay_text = re.sub("[^a-zA-Z]", " ", essay_text)
    words = essay_text.lower().split()
    stop_words = set(stopwords.words("english"))
    words = [w for w in words if not w in stop_words]
    return (words)


# In[4]:


# Generating sentence tokens from the essay and finally the word tokens

def sentence_tokens(essay_text):
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sent_tokens = tokenizer.tokenize(essay_text.strip())
    sentences = []
    for sent_token in sent_tokens:
        if len(sent_token) > 0:
            sentences.append(word_tokens(sent_token))
    return sentences


# In[5]:


# Generating a vector of features

def makeFeatureVec(words, model, num_features):
    featureVec = np.zeros((num_features,),dtype="float32")
    num_words = 0.
    index2word_set = set(model.wv.index2word)
    for word in words:
        if word in index2word_set:
            num_words += 1
            featureVec = np.add(featureVec,model[word])        
    featureVec = np.divide(featureVec,num_words)
    return featureVec


# In[6]:


# Generating word vectors to be used in word2vec model

def getAvgFeatureVecs(essays, model, num_features):
    counter = 0
    essayFeatureVecs = np.zeros((len(essays),num_features),dtype="float32")
    for essay_text in essays:
        essayFeatureVecs[counter] = makeFeatureVec(essay_text, model, num_features)
        counter = counter + 1
    return essayFeatureVecs


# In[7]:


def get_model():
    model = Sequential()
    model.add(LSTM(300, dropout=0.4, recurrent_dropout=0.4, input_shape=[1, 300], return_sequences=True))
    model.add(LSTM(64, recurrent_dropout=0.4))
    model.add(Dropout(0.5))
    model.add(Dense(1, activation='relu'))

    model.compile(loss='mean_squared_error', optimizer='rmsprop', metrics=['mae'])
    model.summary()

    return model


# In[8]:


# Applying k-fold cross validation

cv = KFold(len(dataset), n_folds=5, shuffle=True)
results = []
y_pred_list = []

count = 1
for traincv, testcv in cv:
    print("\n------------Fold {}------------\n".format(count))
    X_test, X_train, y_test, y_train = dataset.iloc[testcv], dataset.iloc[traincv], scores.iloc[testcv], scores.iloc[traincv]
    
    train_essays = X_train['essay']
    test_essays = X_test['essay']
    
    sentences = []
    
    for essay in train_essays:
            # Obtaining all sentences from the training set of essays.
            sentences += sentence_tokens(essay)
            
    # Initializing variables for word2vec model.
    num_features = 300 
    min_word_count = 40
    num_workers = 4
    context = 10
    downsampling = 1e-3

    print("Training Word2Vec Model...")
    model = Word2Vec(sentences, workers=num_workers, size=num_features, min_count = min_word_count, window = context, sample = downsampling)

    model.init_sims(replace=True)
    model.wv.save_word2vec_format('word2vecmodel.bin', binary=True)

    clean_train_essays = []
    
    # Generate training and testing data word vectors.
    for essay_text in train_essays:
        clean_train_essays.append(word_tokens(essay_text))
    trainDataVecs = getAvgFeatureVecs(clean_train_essays, model, num_features)
    
    clean_test_essays = []
    for essay_text in test_essays:
        clean_test_essays.append(word_tokens(essay_text))
    testDataVecs = getAvgFeatureVecs(clean_test_essays, model, num_features)
    
    trainDataVecs = np.array(trainDataVecs)
    testDataVecs = np.array(testDataVecs)
    # Reshaping train and test vectors to 3 dimensions. (1 represnts one timestep)
    trainDataVecs = np.reshape(trainDataVecs, (trainDataVecs.shape[0], 1, trainDataVecs.shape[1]))
    testDataVecs = np.reshape(testDataVecs, (testDataVecs.shape[0], 1, testDataVecs.shape[1]))
    
    lstm_model = get_model()
    lstm_model.fit(trainDataVecs, y_train, batch_size=64, epochs=50)
    #lstm_model.load_weights('./model_weights/final_lstm.h5')
    y_pred = lstm_model.predict(testDataVecs)
    
    # Round y_pred to the nearest integer.
    y_pred = np.around(y_pred)
    
    '''Evaluation metric used : 
    1. Mean squared error
    2. Variance
    3. Cohen's kappa score
    Expected results - Minimum error, maximum variance(For variance, best possible score is 1.0, lower 
    values are worse.) and maximum kappa score(1 depicting the best scores)'''
    
    # Mean squared error
    print("Mean squared error: {0:.2f}".format(mean_squared_error(y_test.values, y_pred)))

    # Explained variance score: 1 is perfect prediction
    print('Variance: {0:.2f}'.format(explained_variance_score(y_test.values, y_pred)))  
    
    #Cohen's kappa score
    result = cohen_kappa_score(y_test.values,y_pred,weights='quadratic')
    print("Kappa Score: {0:.2f}".format(result))
    results.append(result)

    count += 1


# In[11]:


print("Average Kappa score after a 5-fold cross validation: ",np.around(np.array(results).mean(),decimals=2))


# In[14]:


# Splitting dataset into training and test set and generating word embeddings for other models other than
# neural networks

indep_train, indep_test, dep_train, dep_test = train_test_split(dataset, scores, test_size = 0.25)

train_essays2 = indep_train['essay']
test_essays2 = indep_test['essay']
    
sentences2 = []


for essay2 in train_essays2:
            # Obtaining all sentences from the training set of essays.
            sentences2 += sentence_tokens(essay2)
            
# Initializing variables for word2vec model.
num_features = 300 
min_word_count = 40
num_workers = 4
context = 10
downsampling = 1e-3

print("Training Word2Vec Model...")
model = Word2Vec(sentences, workers=num_workers, size=num_features, min_count = min_word_count, window = context, sample = downsampling)

model.init_sims(replace=True)
model.wv.save_word2vec_format('word2vecmodel.bin', binary=True)

clean_train_essays2 = []
    
# Generate training and testing data word vectors.
for essay_text2 in train_essays2:
    clean_train_essays2.append(word_tokens(essay_text2))
trainDataVecs2 = getAvgFeatureVecs(clean_train_essays2, model, num_features)
    
clean_test_essays2 = []
for essay_text2 in test_essays2:
    clean_test_essays2.append(word_tokens(essay_text2))
testDataVecs2 = getAvgFeatureVecs(clean_test_essays2, model, num_features)
    
trainDataVecs2 = np.array(trainDataVecs2)
testDataVecs2 = np.array(testDataVecs2)


# In[15]:


# Generating scores using Linear Regression Model

linear_regressor = LinearRegression()

linear_regressor.fit(trainDataVecs2, dep_train)

dep_pred = linear_regressor.predict(testDataVecs2)

# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(dep_test, dep_pred))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % explained_variance_score(dep_test,dep_pred))

#print('Cohen\'s kappa score: %.2f' % cohen_kappa_score(dep_pred, dep_test))
print("Kappa Score: {0:.2f}".format(cohen_kappa_score(dep_test.values,np.around(dep_pred),weights='quadratic')))


# In[16]:


#Generating scores using Gradient Boosting regressor

'''from sklearn.model_selection import GridSearchCV
params = {'n_estimators':[100, 1000], 'max_depth':[2], 'min_samples_split': [2],
          'learning_rate':[3, 1, 0.1, 0.3], 'loss': ['ls']}

gbr = ensemble.GradientBoostingRegressor()

grid = GridSearchCV(gbr, params)
grid.fit(trainDataVecs2, dep_train)

y_pred = grid.predict(testDataVecs2)

# summarize the results of the grid search
print(grid.best_score_)
print(grid.best_estimator_)'''

#USING THE PARAMS FOUND OUT USING GRID SEARCH CV
gbr = ensemble.GradientBoostingRegressor(alpha=0.9, criterion='friedman_mse', init=None,
             learning_rate=0.1, loss='ls', max_depth=2, max_features=None,
             max_leaf_nodes=None, min_impurity_decrease=0.0,
             min_impurity_split=None, min_samples_leaf=1,
             min_samples_split=2, min_weight_fraction_leaf=0.0,
             n_estimators=1000, presort='auto', random_state=None,
             subsample=1.0, verbose=0, warm_start=False)
gbr.fit(trainDataVecs2, dep_train)
dep_pred = gbr.predict(testDataVecs2)

# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(dep_test, dep_pred))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % explained_variance_score(dep_test,dep_pred))

print("Kappa Score: {0:.2f}".format(cohen_kappa_score(dep_test.values,np.around(dep_pred),weights='quadratic')))


# In[17]:


svr = SVR()

'''parameters = {'kernel':['linear', 'rbf'], 'C':[1, 100], 'gamma':[0.1, 0.001]}

grid = GridSearchCV(svr, parameters)
grid.fit(trainDataVecs2, dep_train)

y_pred = grid.predict(testDataVecs2)

# summarize the results of the grid search
print(grid.best_score_)
print(grid.best_estimator_)'''

#USING THE PARAMS FOUND OUT USING GRID SEARCH CV
svr = SVR(C=100, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma=0.1,kernel='rbf', max_iter=-1, shrinking=True, tol=0.001, verbose=False)
svr.fit(trainDataVecs2, dep_train)
dep_pred = svr.predict(testDataVecs2)


# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(dep_test, dep_pred))

# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % explained_variance_score(dep_test,dep_pred))

#Cohen's Kappa score
print("Kappa Score: {0:.2f}".format(cohen_kappa_score(dep_test.values,np.around(dep_pred),weights='quadratic')))


# In[45]:


# As lstm outperforms all other models, so using it for predicting the scores for the final dataset
valid_set = pd.read_csv('valid_set.tsv', sep='\t', encoding='ISO-8859-1')


# In[46]:


valid_set = valid_set.drop(['domain2_predictionid'], axis = 1)


# In[47]:


valid_set.head()


# In[50]:


valid_test_essays = valid_set['essay']


# In[51]:


valid_test_essays


# In[55]:


sentences = []
    
for valid_essay in valid_test_essays:
        sentences += sentence_tokens(valid_essay)
            
num_features = 300 
min_word_count = 40
num_workers = 4
context = 10
downsampling = 1e-3

print("Training Word2Vec Model...")
model = Word2Vec(sentences, workers=num_workers, size=num_features, min_count = min_word_count, window = context, sample = downsampling)

model.init_sims(replace=True)
model.wv.save_word2vec_format('word2vecmodel.bin', binary=True)

valid_clean_test_essays = []
    
# Generate training and testing data word vectors.
for essay_text in valid_test_essays:
    valid_clean_test_essays.append(word_tokens(essay_text))
valid_testDataVecs = getAvgFeatureVecs(valid_clean_test_essays, model, num_features)

valid_testDataVecs = np.array(valid_testDataVecs)
# Reshaping train and test vectors to 3 dimensions. (1 represnts one timestep)
valid_testDataVecs = np.reshape(valid_testDataVecs, (valid_testDataVecs.shape[0], 1, valid_testDataVecs.shape[1]))
    
predicted_scores = lstm_model.predict(valid_testDataVecs)
    
# Round y_pred to the nearest integer.
predicted_scores = np.around(predicted_scores)


# In[155]:


submission = valid_set.drop(['essay'], axis = 1)


# In[156]:


predicted_score = predicted_scores.tolist()


# In[157]:


predicted_score = pd.Series([score for sublist in predicted_scores for score in sublist])


# In[158]:


predicted_score.head()


# In[159]:


submission = pd.concat([submission, predicted_score], axis = 1).rename(columns = {0:"predicted_score"}).iloc[:,[2,0,1,3]]
submission.to_excel("Submission.xls",index=False)

