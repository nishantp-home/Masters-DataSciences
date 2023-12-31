import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split

filePath = "E:\\Eskills-Academy-projects\\TensorFlow-and-Keras-Lecture-Data\\Data\\section5"
filePath += "\\creditcard.csv"

df = pd.read_csv(filePath)

# Explore the data
fraud_indices = df[df.Class == 1].index
number_records_fraud = len(fraud_indices)

normal_indices = df[df.Class == 0].index
number_records_normal = len(normal_indices)

print("Normal transactions:", number_records_normal)
print("Fraud transations:", number_records_fraud)


y = df.Class    # Response variable
x = df.drop(['Class', 'Time'], axis=1)   # Class is predictor, we do not need time
x_scaled = (x - x.min()) / (x.max() - x.min())

# Since all predictors are numerical
# We will need to pass our feature columns to canned estimator when instantiating it

nV01 = tf.feature_column.numeric_column('V1')
nV02 = tf.feature_column.numeric_column('V2')
nV03 = tf.feature_column.numeric_column('V3')
nV04 = tf.feature_column.numeric_column('V4')
nV05 = tf.feature_column.numeric_column('V5')
nV06 = tf.feature_column.numeric_column('V6')
nV07 = tf.feature_column.numeric_column('V7')
nV08 = tf.feature_column.numeric_column('V8')
nV09 = tf.feature_column.numeric_column('V9')
nV10 = tf.feature_column.numeric_column('V10')
nV11 = tf.feature_column.numeric_column('V11')
nV12 = tf.feature_column.numeric_column('V12')
nV13 = tf.feature_column.numeric_column('V13')
nV14 = tf.feature_column.numeric_column('V14')
nV15 = tf.feature_column.numeric_column('V15')
nV16 = tf.feature_column.numeric_column('V16')
nV17 = tf.feature_column.numeric_column('V17')
nV18 = tf.feature_column.numeric_column('V18')
nV19 = tf.feature_column.numeric_column('V19')
nV20 = tf.feature_column.numeric_column('V20')
nV21 = tf.feature_column.numeric_column('V21')
nV22 = tf.feature_column.numeric_column('V22')
nV23 = tf.feature_column.numeric_column('V23')
nV24 = tf.feature_column.numeric_column('V24')
nV25 = tf.feature_column.numeric_column('V25')
nV26 = tf.feature_column.numeric_column('V26')
nV27 = tf.feature_column.numeric_column('V27')
nV28 = tf.feature_column.numeric_column('V28')
nV30 = tf.feature_column.numeric_column('Amount')

features = [nV01, nV02, nV03, nV04,
            nV05, nV06, nV07, nV08,
            nV09, nV10, nV11, nV12,
            nV13, nV14, nV15, nV16,
            nV17, nV18, nV19, nV20,
            nV21, nV22, nV23, nV24,
            nV25, nV26, nV27, nV28,
            nV30]     # numeric predictors

X_train, X_test, y_train, y_test = train_test_split(x_scaled, y,
                                                    train_size=0.75,
                                                    random_state=101)

# Build a binary classification model
input_func = tf.compat.v1.estimator.inputs.pandas_input_fn(x=X_train, 
                                                           y=y_train,
                                                           batch_size=100, 
                                                           num_epochs=1000, 
                                                           shuffle=True) 

model = tf.estimator.LinearClassifier(feature_columns=features, n_classes=2)   # Linear classifier model
model.train(input_fn=input_func, steps=1000)

# Test on training data
train_input_func = tf.compat.v1.estimator.inputs.pandas_input_fn(x=X_train,
                                                                y=y_train,
                                                                batch_size=10, 
                                                                num_epochs=1, 
                                                                shuffle=False) 

results = model.evaluate(train_input_func)

# Test on testing data
eval_input_func = tf.compat.v1.estimator.inputs.pandas_input_fn(x=X_test,
                                                                y=y_test,
                                                                batch_size=10, 
                                                                num_epochs=1, 
                                                                shuffle=False)

test_results = model.evaluate(eval_input_func)
