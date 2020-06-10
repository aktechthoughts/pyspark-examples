import os
from pyspark.sql import SparkSession
from pyspark import  SparkContext, SparkConf


# Configure the environment
if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME'] = '/usr/spark-1.6.0-bin-hadoop2.6'


def init_aws_secret(conf):

    accessKeyId = os.environ['AWS_ACCESS_KEY_ID']
    secretAccessKey = os.environ['AWS_SECRET_ACCESS_KEY']

    conf.hadoopConfiguration.set("fs.s3n.awsAccessKeyId", accessKeyId)
    conf.hadoopConfiguration.set("fs.s3n.awsSecretAccessKey", secretAccessKey)
    pass

def load_s3_data(spark):
    pass


if __name__ == "__main__":
    conf = SparkConf().setAppName('LoadS3Data')
    sc = SparkContext(conf=conf)

    init_aws_secret(sc)
    load_s3_data(sc)

    sc.stop()
