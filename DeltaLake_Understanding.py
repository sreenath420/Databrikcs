# Databricks notebook source
# MAGIC %sql
# MAGIC
# MAGIC CREATE TABLE employees_value
# MAGIC   (id INT, name STRING, salary DOUBLE);

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO employees_value
# MAGIC VALUES 
# MAGIC   (1, "Adam", 3500.0),
# MAGIC   (2, "Sarah", 4020.5),
# MAGIC   (3, "John", 2999.3),
# MAGIC   (4, "Thomas", 4000.3),
# MAGIC   (5, "Anna", 2500.0),
# MAGIC   (6, "Kim", 6200.3)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees_value

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail employees_value

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees_value'
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC update employees_value 
# MAGIC set salary = salary+100
# MAGIC where name like "A%"

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history employees_value

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees_value'

# COMMAND ----------

# MAGIC %fs ls 'dbfs:/user/hive/warehouse/employees_value/_delta_log/'

# COMMAND ----------

# MAGIC %fs head 'dbfs:/user/hive/warehouse/employees_value/_delta_log/00000000000000000001.json'

# COMMAND ----------

# MAGIC %sql
# MAGIC describe detail employees_value
