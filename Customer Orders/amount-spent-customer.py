from pyspark import SparkConf, SparkContext
from operator import add

conf = SparkConf().setMaster("local").setAppName("FriendsByAge")
sc = SparkContext(conf=conf)
sc.setLogLevel("ERROR")


def parseLine(line):
    fields = line.split(',')
    customer_id = int(fields[0])
    amount = float(fields[2])
    return customer_id, amount


lines = sc.textFile("file:///Users/costinbosoaga/work/BigDataCourse/SparkCourse/customer-orders.csv")
rdd = lines.map(parseLine)
totals = rdd.reduceByKey(add)
amounts_sorted = totals.map(lambda x: (x[1], x[0])).sortByKey()

results = amounts_sorted.collect()
for result in results:
    print(result)
