import warnings

from tensorflow.keras.datasets import mnist
from ML_pipeline.preprocessing import data_reshape
from ML_pipeline.preprocessing import convert_to_cat
from ML_pipeline.preprocessing import feature_scale
from ML_pipeline.model import train_model
from ML_pipeline.model import create_cnn_model
from ML_pipeline.model_evaluation import model_evaluate
from ML_pipeline.model_evaluation import predict
from ML_pipeline.model_evaluation import confusion_mat
from ML_pipeline.model_evaluation import classification_mat
from ML_pipeline.model_evaluation import model_performance
from ML_pipeline.model import store_model

warnings.simplefilter(action='ignore')
try:
    #Loading MNIST dataset
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    
    # Reshape training and testing data as required to build CNN model
    reshape_train_size= list(X_train.shape)
    reshape_train_size.append(1)
    X_train=data_reshape(X_train, reshape_train_size)

    reshape_test_size= list(X_test.shape)
    reshape_test_size.append(1)
    X_test=data_reshape(X_test, reshape_test_size)
     
    # Converting numerical variables to categoriacl variables in test dataset
    n_label=10
    y_cat_train=convert_to_cat(y_train, n_label)
    y_cat_test=convert_to_cat(y_test, n_label)

    # Feature Scaling
    m=255
    X_train=feature_scale(X_train, 'float32', m)
    X_test=feature_scale(X_test, 'float32', m)

    # CNN Model Creation
    input_shape=(28, 28, 1)
    kernel_size=(3, 3)
    pool_size=(2, 2)
    drop=0.25
    cnn_model=create_cnn_model(input_shape, kernel_size, pool_size, drop)
    
    # CNN Model Building
    epochs=10
    model=train_model(cnn_model, X_train, y_cat_train, X_test, y_cat_test, epochs)
    
    # Saving the fitted model
    store_model(model, file_name= 'mnist_cnn_model')

    # Model performance during training and validation
    training_metrics = model_performance(model)
    print('Training Metrics: \n', training_metrics.columns)


    # Model Evaluation
    score = model_evaluate(model, X_test, y_cat_test)
    print('Test loss:', score[0])
    print('Test accuracy:', score[1])

    # Model Predictions
    predictions = predict(model, X_test)
        
    # Classification matrix
    class_mat=classification_mat(y_test, predictions)
    print('Classification Report : \n', class_mat)

    # Confusion matrix
    conf_mat=confusion_mat(y_test, predictions)
    print('Classification Report : \n', conf_mat)

except Exception as e:
    print('!! Exception Details: !!\n', e.__class__)
    print('Please debug for further details')