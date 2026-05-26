# Databricks notebook source
volume_path = '/Volumes/project_1_databricks_workspace_1';
bronze_volume_path = volume_path + '/bronze/volume_bronze_saleslt/';
silver_volume_path = volume_path +  '/silver/volume_silver_saleslt/';
gold_volume_path = volume_path + '/gold/volume_gold_saleslt/';

# COMMAND ----------

# df = spark.read.format("parquet").load(bronze_volume_path + 'Address/Address.parquet')

# COMMAND ----------

# display(df)

# COMMAND ----------

# from pyspark.sql.functions import from_utc_timestamp, date_format
# from pyspark.sql.types import TimestampType

# df = df.withColumn("ModifiedDate",date_format(from_utc_timestamp(df["ModifiedDate"].cast(TimestampType()),"UTC"),"yyyy-MM-dd"))

# display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC **Transfoming all the tables**

# COMMAND ----------

from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

all_tables =[]
for table in dbutils.fs.ls(bronze_volume_path):
    all_tables.append(table.name.split("/")[0])
# print(all_tables)

for table in all_tables:
    df = spark.read.format("parquet").load(bronze_volume_path + table + "/" + table + ".parquet")
    all_columns = df.columns
    for column in all_columns:
        if "Date" in column or "date" in column:
            df = df.withColumn(column,date_format(from_utc_timestamp(df[column].cast(TimestampType()), "UTC"),"yyyy-MM-dd"))
    # display(df)
    df.write.mode("overwrite").format("delta").save(silver_volume_path + table + "/")