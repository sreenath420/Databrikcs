# Databricks notebook source
# MAGIC %sql
# MAGIC describe history employees_value

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees_value

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees_value version as of 1

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees_value@v1

# COMMAND ----------

# MAGIC %sql
# MAGIC delete from employees_value

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees_value

# COMMAND ----------

# MAGIC %sql
# MAGIC restore table employees_value to version as of 2

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employees_value

# COMMAND ----------

# MAGIC %sql
# MAGIC describe history employees_value

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table employees_value

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table employee
