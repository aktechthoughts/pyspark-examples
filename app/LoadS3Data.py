from __future__ import print_function
import os
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.types import *
import boto3

def init_aws_secret(spark):
    sc = spark.sparkContext
    
    accessKeyId = os.environ['AWS_ACCESS_KEY_ID']
    secretAccessKey = os.environ['AWS_SECRET_ACCESS_KEY']
    
    sc.hadoopConfiguration.set("fs.s3n.awsAccessKeyId", accessKeyId)
    sc.hadoopConfiguration.set("fs.s3n.awsSecretAccessKey", secretAccessKey)

  

def load_s3_data(spark):
    pass

if __name__ == "__main__":
    # $example on:init_session$
    spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
    # $example off:init_session$
    init_aws_secret(spark)
    load_s3_data(spark)
    
    spark.stop()
