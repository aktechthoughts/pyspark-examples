import sys
from pyspark.sql import SparkSession

if __name__ == "__main__":
    #if len(sys.argv) != 2:
    #    print("Usage: wordcount <file>", file=sys.stderr)
    #    sys.exit(-1)

    spark = SparkSession\
        .builder \
    	.appName("Python Spark SQL basic example") \
	.config("spark.some.config.option", "some-value") \
	.getOrCreate()

    # spark is an existing SparkSession
    df = spark.read.json("/app/examples/src/main/resources/people.json") 
    # Displays the content of the DataFrame to stdout
    df.show()
