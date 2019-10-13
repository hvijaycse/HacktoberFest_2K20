import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
import random

TRAIN_PERCENT = 70

# get dataSet of digits from excising directory
digits = datasets.load_digits()

# getting the size of
sizeOfSet = len(digits.data)

# getting size of train
sizeOfTrain = int(sizeOfSet * TRAIN_PERCENT / 100)
sizeOfTest = sizeOfSet - sizeOfTrain

print("Data set size: ", sizeOfTrain)
print("Test set size: ", sizeOfTest)


# defining the classifier with param to determine how it will learn
classifier = svm.SVC(gamma=0.0001, C=100)

# extracting from digits the data set and target set
data, target = digits.data[:sizeOfTrain], digits.target[:sizeOfTrain]

# training the classifier
classifier.fit(data, target)

# calculating accuracy
right = 0
wrong = 0
# go over all test data
for i in range(sizeOfTrain + 1, sizeOfSet):
    #predict
    prediction = classifier.predict(digits.data[[i]])
    #check if prediction correct and save statistic
    if prediction == digits.target[i]:
        right += 1
    else:
        wrong += 1

# calculating summary
rightPercentage = right/(right+wrong)*100
wrongPercentage = wrong/(right+wrong)*100

print("Overall accuracy:")
print("right: ",rightPercentage,"%")
print("wrong: ",wrongPercentage,"%")

# show and predict single image
answer = input("would you like to predict single image? [y,n]")
while answer is not 'n':
    imgIndex = random.randint(sizeOfTrain + 1, sizeOfSet)
    # prediction is happening
    prediction = classifier.predict(digits.data[[imgIndex]])
    print("prediction: ",prediction)
    # displaying the image
    plt.imshow(digits.images[imgIndex],cmap=plt.cm.gray_r, interpolation="nearest")
    plt.show()
    answer = input("wanna go again? [y,n]")
