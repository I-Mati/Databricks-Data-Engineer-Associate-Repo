# Databricks notebook source
# MAGIC %md
# MAGIC ## Python

# COMMAND ----------

print("Hello World!")

# COMMAND ----------

# MAGIC %run ./Another-Folder/Another-Notebook

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls './databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

files = dbutils.fs.ls('databricks-datasets')
print(files)

# COMMAND ----------

display(files)

# COMMAND ----------

# MAGIC %md
# MAGIC ## SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello World from SQL"
# MAGIC
