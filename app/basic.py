import os
from pyspark.sql import SparkSession
from pyspark import  SparkContext, SparkConf


# Configure the environment
if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME'] = '/usr/spark-1.6.0-bin-hadoop2.6'


if __name__ == "__main__":
    conf = SparkConf().setAppName('basic').setMaster('local[2]')
    sc = SparkContext(conf=conf)


    sc.stop()
