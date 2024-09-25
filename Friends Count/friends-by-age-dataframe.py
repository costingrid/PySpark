from pyspark.sql import SparkSession
from pyspark.sql import functions as func

spark = SparkSession.builder.appName("SparkSQL").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

people = spark.read.option("header", "true").option("inferSchema", "true")\
    .csv("file:///Users/costinbosoaga/work/BigDataCourse/SparkCourse/fakefriends-header.csv")
    
people.groupBy("age").agg(func.round(func.avg("friends"), 2)).sort("age").show()

spark.stop()

