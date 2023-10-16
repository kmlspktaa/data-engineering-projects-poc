# Databricks notebook source
# MAGIC %run ./read_data

# COMMAND ----------

# MAGIC %run ./preprocessing

# COMMAND ----------

# MAGIC %run ./training_model

# COMMAND ----------

# MAGIC %run ./return_embed

# COMMAND ----------

# MAGIC %run ./top_n

# COMMAND ----------

def load_model(model,column_name,vector_size,window_size):
  df = read_data()
  x = output_text(df,column_name)
  word2vec_model = model_train(x,vector_size,window_size,model)
  vectors = return_embed(word2vec_model,df,column_name)
  Vec = pd.DataFrame(vectors).transpose() # Saving vectors of each abstract in data frame so that we can use directly while running code again
  if model == 'Skipgram':
    Vec.to_csv('/dbfs/mnt/data/data/output/Skipgram_vec.csv')
  else:
    Vec.to_csv('/dbfs/mnt/data/data/output/Fasttext_vec.csv')

if __name__ == '__main__':
  load_model('Skipgram','Abstract',100,3)
  load_model('Fasttext','Abstract',100,3)
  results,sim = top_n('Coronavirus','Skipgram','Abstract')
  results1,sim1 = top_n('Coronavirus','Fasttext','Abstract')
  
