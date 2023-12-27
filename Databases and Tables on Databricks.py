# Databricks notebook source
# MAGIC %sql
# MAGIC create table managed_default
# MAGIC (width int,length int,height int)
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC insert into managed_default
# MAGIC values(3 int,2 int,1 int)

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended managed_default

# COMMAND ----------

# MAGIC %sql
# MAGIC create table external_default
# MAGIC (width int,length int,height int)
# MAGIC location 'dbfs:/user/hive/warehouse/external_default';
# MAGIC
# MAGIC insert into external_default
# MAGIC values(3,2,1)

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended external_default

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema new_default

# COMMAND ----------

# MAGIC %sql
# MAGIC describe database extended new_default

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC use new_default;
# MAGIC
# MAGIC create table internal_new_default
# MAGIC (width int,length int,height int);
# MAGIC
# MAGIC insert into internal_new_default
# MAGIC values(3,2,1);
# MAGIC
# MAGIC create table external_new_default
# MAGIC (width int,length int,height int)
# MAGIC location 'dbfs:/FileStore/external_new_default/';
# MAGIC
# MAGIC insert into external_new_default
# MAGIC values(3,2,1)

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended internal_new_default

# COMMAND ----------

# MAGIC %sql
# MAGIC describe extended external_new_default

# COMMAND ----------


