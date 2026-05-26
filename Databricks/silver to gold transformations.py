# Databricks notebook source
volume_path = '/Volumes/project_1_databricks_workspace_1';
silver_volume_path = volume_path +  '/silver/volume_silver_saleslt/';
gold_volume_path = volume_path + '/gold/volume_gold_saleslt/';

# COMMAND ----------

# df = spark.read.format("delta").load(silver_volume_path+"Address/")
# display(df)
# column_names = df.columns

# for old_column_name in column_names:
#     new_column_name = "".join(["_"+char if char.isupper() and not old_column_name[i-1].isupper() else char for i,char in enumerate(old_column_name)]).lstrip("_")
#     df = df.withColumnRenamed(old_column_name,new_column_name)

# display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC **Transforming all the tables**

# COMMAND ----------

all_tables = []
for table in dbutils.fs.ls(silver_volume_path):
    all_tables.append(table.name.split("/")[0])
# print(all_tables)

# COMMAND ----------

for table in all_tables:
    df = spark.read.format("delta").load(silver_volume_path + table + "/")
    column_names = df.columns

    for old_column_name in column_names:
        new_column_name = "".join(["_"+char if char.isupper() and not old_column_name[i-1].isupper() else char for i,char in enumerate(old_column_name)]).lstrip("_")
        df = df.withColumnRenamed(old_column_name,new_column_name)
    df.write.mode("overwrite").format("delta").save(gold_volume_path + table + "/")

# COMMAND ----------


# display(df)