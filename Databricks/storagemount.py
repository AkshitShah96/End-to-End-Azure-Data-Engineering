# Databricks notebook source
dbutils.fs.ls("abfss://bronze@project1adlsgen2storage.dfs.core.windows.net/")

# COMMAND ----------

# MAGIC %sql
# MAGIC create schema if not exists bronze
# MAGIC managed location 'abfss://bronze@project1adlsgen2storage.dfs.core.windows.net/';
# MAGIC
# MAGIC create schema if not exists silver
# MAGIC managed location 'abfss://silver@project1adlsgen2storage.dfs.core.windows.net/';
# MAGIC
# MAGIC create schema if not exists gold
# MAGIC managed location 'abfss://gold@project1adlsgen2storage.dfs.core.windows.net/';

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG project_1_databricks_workspace_1;
# MAGIC USE SCHEMA bronze;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE EXTERNAL VOLUME if not EXISTS project_1_databricks_workspace_1.bronze.volume_bronze_salesLT
# MAGIC LOCATION 'abfss://bronze@project1adlsgen2storage.dfs.core.windows.net/SalesLT';
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE external volume if not exists project_1_databricks_workspace_1.silver.volume_silver_salesLT
# MAGIC LOCATION 'abfss://silver@project1adlsgen2storage.dfs.core.windows.net/SalesLT';

# COMMAND ----------

# MAGIC %sql
# MAGIC -- drop volume project_1_databricks_workspace_1.gold.volume_gold_salesLT;
# MAGIC CREATE EXTERNAL VOLUME if not EXISTS project_1_databricks_workspace_1.gold.volume_gold_salesLT
# MAGIC LOCATION 'abfss://gold@project1adlsgen2storage.dfs.core.windows.net/SalesLT';

# COMMAND ----------

dbutils.fs.ls('/Volumes/project_1_databricks_workspace_1/bronze/volume_bronze_salesLT')

# COMMAND ----------

# MAGIC %md
# MAGIC **Transformations Starts Here**

# COMMAND ----------

volume_path = '/Volumes/project_1_databricks_workspace_1';
bronze_volume_path = '/bronze/volume_bronze_salesLT/';
silver_volume_path = '/silver/volume_silver_salesLT/';
gold_volume_path = '/gold/volume_gold_salesLT/';