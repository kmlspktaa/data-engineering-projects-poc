-- Databricks notebook source
-- MAGIC %sql
-- MAGIC  CREATE TABLE IF NOT EXISTS
-- MAGIC   lineage_data.lineage_schema.menu (
-- MAGIC     recipe_id INT,
-- MAGIC     app string,
-- MAGIC     main string,
-- MAGIC     dessert string
-- MAGIC   );

-- COMMAND ----------

-- MAGIC %sql
-- MAGIC INSERT INTO lineage_data.lineage_schema.menu
-- MAGIC     (recipe_id, app, main, dessert)
-- MAGIC VALUES
-- MAGIC     (1,"Ceviche", "Tacos", "Flan"),
-- MAGIC     (2,"Tomato Soup", "Souffle", "Creme Brulee"),
-- MAGIC     (3,"Chips","Grilled Cheese","Cheesecake");

-- COMMAND ----------

CREATE TABLE
  lineage_data.lineage_schema.dinner
AS SELECT
  recipe_id, concat(app," + ", main," + ",dessert)
AS
  full_menu
FROM
  lineage_data.lineage_schema.menu

-- COMMAND ----------

select * from lineage_data.lineage_schema.dinner
