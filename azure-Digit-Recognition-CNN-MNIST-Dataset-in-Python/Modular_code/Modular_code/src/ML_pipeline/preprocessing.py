from tensorflow.keras.utils import to_categorical

# Function to reshape data 
def data_reshape(data, shape):
    #reshaping data into size of 4
    if len(shape)==4 : 
        reshape_data=data.reshape(shape[0], shape[1], shape[2], shape[3]) #function for reshaping the data
        return reshape_data
    else:
        print("The length of reshape array is not 4")


# Function to convert numerical data to catgorical
def convert_to_cat(data,labels):
    #converting numerical data to categorical into number of classes(labels)
    if labels!=0: #number of classes  can't be 0
        data_cat = to_categorical(data, labels) #function for converting the numerical data to categorical
        return data_cat
    else:
        print("The value for label can not be 0")    


# Function for feature scaling 
def feature_scale(data, type, div):
    #changing the numerical data to float data type
    if type=='float32':
        data = data.astype(type) #function for converting the data type of the data
    else:
        print("Type is not float32")

    if div != 0:
        data /= div  #dividing data with the non-zero number
        return data
    else:
        print("Division by zero is not allowed")