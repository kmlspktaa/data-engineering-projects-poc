# Databricks notebook source
from delta.tables import *
from pyspark.sql import functions as F
import json
import datetime
from pyspark.sql.functions import when
from pyspark.sql.functions  import *

# COMMAND ----------

current_time_stamp=str(datetime.datetime.today())

# COMMAND ----------

current_time_stamp

# COMMAND ----------

dbutils.widgets.text('list1', "[{'city_id': 1, 'year': 2017, 'month': 1, 'day': 1, 'hour': 100}, {'city_id': 1, 'end_year': 2017, 'end_month': 2, 'end_day': 15, 'end_hour': 600}]")
input=dbutils.widgets.get("list1")
dbutils.widgets.removeAll()

# COMMAND ----------

type(input)

# COMMAND ----------

l1=eval(input)

# COMMAND ----------

type(l1)

# COMMAND ----------

l1[0]

# COMMAND ----------

l1[1]

# COMMAND ----------

city_id=l1[0]["city_id"]
start_year=(l1[0]["year"])
end_year=(l1[1]["end_year"])
start_month=l1[0]["month"]
end_month=l1[1]["end_month"]
start_hour=l1[0]["hour"]
end_hour=l1[1]["end_hour"]
start_day=l1[0]["day"]
end_day=l1[1]["end_day"]

# COMMAND ----------

dbutils.fs.ls("/mnt/input")

# COMMAND ----------

df1=spark.read.option("inferschema",True).option("header",True).csv("dbfs:/mnt/input/weather_data.csv")

# COMMAND ----------

df1=df1.withColumn("year",year("date"))

# COMMAND ----------

df1=df1.withColumn("day",dayofmonth("date"))

# COMMAND ----------

df1=df1.withColumn("month",month("date"))

# COMMAND ----------

df1.display()

# COMMAND ----------

if start_month<9:
    start_month1='0'+str(start_month)
else:
    start_month1=start_month
if start_day<9:
    start_day1='0'+str(start_day)
else:
    start_day1=start_day

start_date=str(start_year)+'-'+str(start_month1)+'-'+str(start_day1)

# COMMAND ----------

if end_month<9:
    end_month1='0'+str(end_month)
else:
    end_month1=end_month
if end_day<9:
    end_day1='0'+str(end_day)
else:
    end_day1=end_day



end_date=str(start_year)+'-'+str(end_month1)+'-'+str(end_day1)

# COMMAND ----------

start_date

# COMMAND ----------

end_date

# COMMAND ----------

df1=df1.filter((df1.city_id==city_id)& (df1.date>= start_date) & (df1.date<=end_date) )

# COMMAND ----------

df2=df1.withColumn("cond", when ((df1.date==start_date) & (df1.hour< start_hour), 1).when ((df1.date==end_date) & (df1.hour>end_hour),1).otherwise(0))

# COMMAND ----------

df3=df2.filter(df2.cond==0)

# COMMAND ----------

df3.display()

# COMMAND ----------

current_time_stamp=current_time_stamp.replace(":","")

# COMMAND ----------

df2.write.save("/mnt/replication/weather_request/"+current_time_stamp)

# COMMAND ----------

dbutils.fs.ls("/mnt/replication/weather_request")
