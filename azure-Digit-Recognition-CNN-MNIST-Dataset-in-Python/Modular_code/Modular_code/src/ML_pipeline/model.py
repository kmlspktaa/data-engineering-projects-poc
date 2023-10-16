from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# Function to create CNN model
def create_cnn_model(input_shape,kernel_size,pool_size,drop):
    model = Sequential()

    model.add(Conv2D(32, kernel_size=kernel_size, activation='relu', input_shape=input_shape))
    model.add(Conv2D(64, kernel_size, activation='relu'))
    model.add(MaxPool2D(pool_size=pool_size))
    model.add(Dropout(drop))
    model.add(Flatten())

    model.add(Dense(256, activation='relu'))
    model.add(Dropout(drop))
    model.add(Dense(10, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Function for model training
def train_model(cnn_model, X_train, y_train, X_test, y_test, epochs):
    early_stop = EarlyStopping(monitor='val_loss', patience=2)
    cnn_model.fit(X_train, y_train, epochs=epochs, callbacks=[early_stop], validation_data=(X_test, y_test))
    return cnn_model

def store_model(model,file_path='../output/',file_name='trained_model'):
    # Store the model as json and 
    # store model weights as HDF5
    
    # serialize model to JSON
    model_json = model.to_json()
    with open(file_path+file_name+'.json', "w") as json_file:
        json_file.write(model_json)
    # serialize weights to HDF5
    model.save_weights(file_path+file_name+'.h5')
    print(f"Saved model to disk in path {file_path} as {file_name + '.json'}")
    print(f"Saved weights to disk in path {file_path} as {file_name + '.h5'}")
