from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

spark = SparkSession.builder.appName("MinTemperatures").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("customerID", IntegerType(), True),
    StructField("field1", IntegerType(), True),
    StructField("amount", FloatType(), True)])

# // Read the file as dataframe
df = spark.read.schema(schema).csv("customer-orders.csv")
df.printSchema()

customer_amounts = df.select("customerID", "amount")

total_spent = customer_amounts.groupBy("customerID").agg(func.round(func.sum("amount"), 2).alias("total"))

total_spent.printSchema()

total_spent.sort("total").show(total_spent.count())
    
spark.stop()

                                                  