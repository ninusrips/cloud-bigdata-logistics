from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("LogisticsETL").getOrCreate()
df = spark.read.csv("s3a://ninusri/raw/orders.csv", header=True)
clean = df.dropna().dropDuplicates()
clean.write.mode("overwrite").parquet("s3a://ninusri/processed/orders/")
print("ETL completed")
