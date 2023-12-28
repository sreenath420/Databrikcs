# Databricks notebook source
# MAGIC %sql
# MAGIC -- MAGIC %md
# MAGIC -- MAGIC ## Preparing Sample Data
# MAGIC -- COMMAND ----------
# MAGIC
# MAGIC CREATE TABLE IF NOT EXISTS smartphones_data
# MAGIC (id INT, name STRING, brand STRING, year INT);

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO smartphones_data
# MAGIC VALUES (1, 'iPhone 14', 'Apple', 2022),
# MAGIC       (2, 'iPhone 13', 'Apple', 2021),
# MAGIC       (3, 'iPhone 6', 'Apple', 2014),
# MAGIC       (4, 'iPad Air', 'Apple', 2013),
# MAGIC       (5, 'Galaxy S22', 'Samsung', 2022),
# MAGIC       (6, 'Galaxy Z Fold', 'Samsung', 2022),
# MAGIC       (7, 'Galaxy S9', 'Samsung', 2016),
# MAGIC       (8, '12 Pro', 'Xiaomi', 2022),
# MAGIC       (9, 'Redmi 11T Pro', 'Xiaomi', 2022),
# MAGIC       (10, 'Redmi Note 11', 'Xiaomi', 2021)

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW TABLES

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE VIEW view_apple_phones
# MAGIC AS  SELECT * 
# MAGIC     FROM smartphones_data 
# MAGIC     WHERE brand = 'Apple';
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from view_apple_phones

# COMMAND ----------

# MAGIC %sql show tables

# COMMAND ----------

# MAGIC %sql
# MAGIC --Creating Temporary Views
# MAGIC -- This temp views available only within spark session after that automatically it will close the views in spark
# MAGIC CREATE TEMP VIEW temp_view_phones_brands
# MAGIC AS  SELECT DISTINCT brand
# MAGIC     FROM smartphones_data;

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables

# COMMAND ----------

# MAGIC %sql
# MAGIC --global temp views existings with the cluster
# MAGIC
# MAGIC CREATE GLOBAL TEMP VIEW global_temp_view_latest_phones
# MAGIC AS SELECT * FROM smartphones_data
# MAGIC     WHERE year > 2020
# MAGIC     ORDER BY year DESC;
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC --if you retrive data from global views tables you should mention the schema(global_temp.tablename)
# MAGIC select * from global_temp.global_temp_view_latest_phones

# COMMAND ----------

# MAGIC %sql
# MAGIC show tables

# COMMAND ----------

# MAGIC %sql
# MAGIC --if you want know the global temp views tables use below command
# MAGIC show tables in global_temp

# COMMAND ----------

# MAGIC %sql
# MAGIC --drop the views
# MAGIC
# MAGIC DROP TABLE smartphones_data;
# MAGIC DROP VIEW view_apple_phones;
# MAGIC DROP VIEW global_temp.global_temp_view_latest_phones;
