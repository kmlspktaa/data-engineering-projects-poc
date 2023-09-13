
#  Spark Integration with  Redshift and Kafka
Spark can read and write data from anywhere.
# Why we need Integration
To fast data processing.

    
# Extract , Transformation and Load 
To create data pipline we need ETL .


# PySpark Integration with Redshift.
Read write data from Redshift

#Note- 
- need redshift jdbc jar file
- need aws credentials : AccessKey and AccessSecretKey





# PySpark Integration with Kafka.
Data extraction using Kafka
#Requirements: AWS Cloud

- Amazon Simple Storage Service (Amazon S3, Redshift)
# Code Description
    File Name : pyspark_redshift.ipynb, pyspark_kafka.ipynb, pyspark_redshift.py and pyspark_kafka.py
    DataSets : airlines1.csv
    Jar files : redshift-jdbc42-2.0.0.4.jar
    File Description : Integration of pyspark with Redshift and Kafka.
    

#NOTE :- use findspark library when executing python script

 - import findspark
 - findspark.init()

## Steps to Run
There are two ways to execute the end to end flow.
 - Command Prompt => python script
 - spark_path spark-submit file_path
 - spark_path => <path_to_spark>>
 - file_path => <path_to_file>
 - Data file path is same as script file path

eg. <C:\Users\admin\Desktop\spark\bin>spark-submit C:\Users\admin\Desktop\Integration\pyspark_redshift.py>


- IPython

### Modular code
- Create virtualenv
- Install requirements `pip install -r requirements.txt`
- Run Code `python pyspark_redshift.py`
- Run Code `python pyspark_kafka.py`
- Check output for all the visualization
### IPython
Follow the instructions in the notebook `pyspark_redshift.ipynb`
Follow the instructions in the notebook `pyspark_kafka.ipynb`

 
