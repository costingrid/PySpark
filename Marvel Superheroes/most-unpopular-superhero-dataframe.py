from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("MostPopularSuperhero").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True)])

names = spark.read.schema(schema).option("sep", " ").csv("file:///Users/costinbosoaga/work/BigDataCourse/SparkCourse"
                                                         "/Marvel-Names.txt")

lines = spark.read.text("file:///Users/costinbosoaga/work/BigDataCourse/SparkCourse/Marvel-Graph.txt")

# Small tweak vs. what's shown in the video: we trim each line of whitespace as that could
# throw off the counts.
connections = lines.withColumn("id", func.split(func.trim(func.col("value")), " ")[0]) \
    .withColumn("connections", func.size(func.split(func.trim(func.col("value")), " ")) - 1) \
    .groupBy("id").agg(func.sum("connections").alias("connections"))

minConnections = connections.agg(func.min("connections")).first()[0]

mostUnpopular = connections.filter(func.col("connections") == minConnections)

(mostUnpopular.join(names, names["id"] == mostUnpopular["id"], "inner")
 .select(names["id"], "name").show(mostUnpopular.count()))
