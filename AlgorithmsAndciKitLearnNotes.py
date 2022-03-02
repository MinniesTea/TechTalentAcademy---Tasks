# -------------------------------------------Algorithms----------------------------------------------------------#
# 1. What is an Algorithm

# An algorithm is a tool that provides a well-defined & efficient computational procedure to transform your data
# input into meaningful information that is output.

# 2. What is Machine Learning

# Machine learning is a subset of AI: Artificial Intelligence, Machine Learning, Deep Learning.

# 3. Different types of Learning

# Supervised Learning, Unsupervised Learning and Reinforcement Learning.

# 4. The maths behind machine learning

# Probability - Probability is the branch of mathematics concerning numerical descriptions of how likely
#               an event is to occur, or how likely it is that a proposition is true. The probability of an event
#               is a number between 0 and 1, where, roughly speaking, 0 indicates impossibility of the
#               event and 1 indicates certainty.
# Bayes Theorem - Describes the probability of an event, based on prior knowledge of conditions that might
#                 be related to the event
# Statistics -  Statistics is the discipline that concerns the collection, organization, analysis, interpretation,
#               and presentation of data. In applying statistics to a scientific, industrial, or social problem, it is
#               conventional to begin with a statistical population or a statistical
#               model to be studied.
# Descriptive Statistics - A descriptive statistic is a summary statistic that quantitatively describes or summarizes
#                          features from a collection of information, while descriptive statistics is the process of
#                          using and analysing those statistics.
# Inferential Statistics - Statistical inference is the process of using data analysis to infer properties of an
#                          underlying distribution of probability. Inferential statistical analysis infers properties
#                          of a population, for example by testing hypotheses and deriving estimates.
# Linear Algebra - Linear algebra is about linear combinations. That is, using arithmetic on columns of numbers called
#                  vectors and arrays of numbers called matrices, to create new columns and arrays of numbers. Linear
#                  algebra is the study of lines and planes, vector spaces and mappings that are required for linear
#                  transforms.
# Vector calculus - Vector calculus, or vector analysis, is a branch of mathematics concerned with differentiation
#                   and integration of vector fields, primarily in 3-dimensional Euclidean space R 3.

# 5. Algorithms used in Machine Learning

# Regression Algorithms (Linear, Polynomial, Logistic)
# Classification Algorithms (K-Nearest Neighbour, Decision Trees)
# Clustering Algorithms (K-Means, Hierarchical)
# Association
# Dimensionality Reduction

# 6. Process of training a Machine Learning Model

# 1. Frame the problem and look at the big picture
# 2. Get the data
# 3. Explore the data
# 4. Prepare the data to better expose the underlying data patterns to machine learning algorithms
# 5. Explore many models and shortlist the best ones
# 6. Fine tune your models and combine them into a great solution
# 7. Present your solution
# 8. Launch, monitor and maintain your system

# The Steps for Machine Learning:
# • Load dataset
# • Explore dataset
# • Process data
# • Visualise data
# • Pick algorithms
# • Train and test sets
# • Standardise data (scale)
# • Compile and fit
# • Learning from the model and evaluations

# -------------------------------------------Scikit-Learn----------------------------------------------------------#

# Scikit-learn is a library in Python that provides many unsupervised and supervised learning algorithms.
# It’s built upon some of the technology you might already be familiar with, like NumPy, pandas, and Matplotlib!

# ------------------------------------------------- Linear Regression --------------------------------------------
# When we are trying to find a line that fits a set of data best, we are performing Linear Regression.
# For each point y on a line we can say:
# y = m x + by=mx+b
# where m is the slope, and b is the intercept. y is a given point on the y-axis, and it corresponds to a given x on the x-axis.
#
# Import and create the model:
#
# from sklearn.linear_model import LinearRegression
# your_model = LinearRegression()
#
# Fit:
#
# your_model.fit(x_training_data, y_training_data)
# - coef_: contains the coefficients
# - intercept_: contains the intercept
#
# Predict:
#
# predictions = your_model.predict(your_x_data)
# - score(): returns the coefficient of determination R²

# --------------------------------------------------- Naive Bayes --------------------------------------------------
#
# Import and create the model:
#
# from sklearn.naive_bayes import MultinomialNB
# your_model = MultinomialNB()
#
# Fit:
#
# your_model.fit(x_training_data, y_training_data)
#
# Predict:
#
# # Returns a list of predicted classes - one prediction for every data point
# predictions = your_model.predict(your_x_data)
# # For every data point, returns a list of probabilities of each class
# probabilities = your_model.predict_proba(your_x_data)

# --------------------------------------------------- K-Nearest Neighbors --------------------------------------------------

# Import and create the model:
#
# from sklearn.neigbors import KNeighborsclassifier
# your_model KNeighborsclassifier()
#
# Fit:
# your_model.fit(x_training_data, y_training_data)
#
# Predict:
#
# # Returns a list of predicted classes one prediction for every data point
# predictions = your_model.predict(your_x_data)
# # For every data point, returns a list of probabilities of each class
# probabilities = your_model.predict_proba(your_x_data)

# --------------------------------------------------- K-Means --------------------------------------------------

# Import and create the model:
#
# from sklearn.cluster import KMeans
# your_model = KMeans (n_clusters=4, init='random')
#
# - n_clusters: number of clusters to form and number of centroids to generate
# - init: method for initialization
#     - k-means++: K-Means++ [default]
#     - random: K-Means
# - random_state: the seed used by the random number generator [optional]
#
# Fit:
#
# your_model.fit(x_training_data)
#
# Predict:
#
# predictions = your_model.predict(your_x_data)

# --------------------------------------------------- Validating the Model -------------------------------------------

# Import and print accuracy, recall, precision, and F1 score:
#
# from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
#
# print(accuracy_score(true_labels, guesses))
# print(recall_score(true_labels, guesses))
# print(precision_score(true_labels, guesses))
# print(f1_score(true_labels, guesses))
#
# Import and print the confusion matrix:
#
# from sklearn.metrics import confusion_matrix
# print(confusion_matrix(true_labels, guesses))

# ---------------------------------------------------Training Sets and Test Sets---------------------------------------

# from sklearn.model_selection import train_test_split
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, test_size=0.2)
#
# - train_size: the proportion of the dataset to include in the train split
# - test_size: the proportion of the dataset to include in the test split
# - random_state: the seed used by the random number generator [optional]

