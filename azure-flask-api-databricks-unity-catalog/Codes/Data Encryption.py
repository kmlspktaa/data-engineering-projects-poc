# Databricks notebook source
from pyspark.sql.functions import * 
from pyspark.sql import functions as F

# COMMAND ----------

df1=spark.read.option("header",True).option("inferschema",True).csv("dbfs:/mnt/input/Input_DB/employees.csv")

# COMMAND ----------

dbutils.fs.ls("/mnt/input/Input_DB/")

# COMMAND ----------

df1=df1.withColumn("SIN",expr('row_number() over(partition by "1" order by "1")'))

# COMMAND ----------

df1=df1.withColumn("SIN",expr('row_number() over(partition by "1" order by "1")'))

# COMMAND ----------

df1=df1.withColumn("Bank_Acct_number",expr('row_number() over(partition by "1" order by "1")'))

# COMMAND ----------

from cryptography.fernet import Fernet

# COMMAND ----------

from pyspark.sql.functions import udf, lit, md5
from pyspark.sql.types import StringType

# COMMAND ----------

from cryptography.fernet import Fernet
from cryptography.fernet import Fernet


def encrypt(message):
    # we will be encrypting the below string.
    # message = "hello geeks"

    # generate a key for encryption and decryption
    # You can use fernet to generate
    # the key or use random key generator
    # here I'm using fernet to generate key

    key = Fernet.generate_key()

    # Instance the Fernet class with the key

    fernet = Fernet(key)

    # then use the Fernet class instance
    # to encrypt the string string must
    # be encoded to byte string before encryption
    encMessage = fernet.encrypt(message.encode())
    return encMessage
# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods

# COMMAND ----------

encrypt("message")

# COMMAND ----------

spark.udf.register("encrypt", encrypt,StringType())

# COMMAND ----------

from pyspark.sql.types import ByteType

# COMMAND ----------

df1=df1.withColumn("SIN",expr("cast (SIN as string)"))

# COMMAND ----------

df1.display()

# COMMAND ----------

df1=df1.withColumn("encrypt_sin",expr("encrypt(SIN)"))
df1=df1.withColumn("encrypt_bank_account",expr("encrypt(cast (Bank_Acct_number as string))"))

# COMMAND ----------

df1.display()

# COMMAND ----------

df1=df1.withColumn("encrypt_email_address",expr("encrypt( (email))"))

# COMMAND ----------

df1.display()

# COMMAND ----------

from datetime import date

# COMMAND ----------

today = date.today()

# COMMAND ----------

str(today)

# COMMAND ----------

df1.repartition(1).write.save("/mnt/input/abc")
