from __future__ import print_function

from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import DecisionTreeRegressor

from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator

if __name__ == "__main__":

    # Create a SparkSession (Note, the config section is only for Windows!)
    spark = SparkSession.builder.appName("RealEstateRegression").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")

    # Load up our data and convert it to the format MLLib expects.
    data = spark.read.option("header", "true").option("inferSchema", "true") \
        .csv("realestate.csv")

    assembler = VectorAssembler(inputCols=["HouseAge", "DistanceToMRT", "NumberConvenienceStores"]
                                , outputCol="features")
    df = assembler.transform(data).select("features", "PriceOfUnitArea")

    # Let's split our data into training data and testing data
    trainingData, testData = df.randomSplit([0.7, 0.3])

    # Now create our decision tree model
    dt = DecisionTreeRegressor(featuresCol="features", labelCol="PriceOfUnitArea")

    # Train the model using our training data
    model = dt.fit(trainingData)

    # Now see if we can predict values in our test data.
    # Generate predictions using our linear regression model for all features in our
    # test dataframe:
    fullPredictions = model.transform(testData).cache()

    # Extract the predictions and the "known" correct labels.
    predictions = fullPredictions.select("prediction").rdd.map(lambda x: x[0])
    labels = fullPredictions.select("PriceOfUnitArea").rdd.map(lambda x: x[0])

    # Zip them together
    predictionAndLabel = predictions.zip(labels).collect()

    # Print out the predicted and actual values for each point
    for prediction in predictionAndLabel:
      print(prediction)


    # Stop the session
    spark.stop()
