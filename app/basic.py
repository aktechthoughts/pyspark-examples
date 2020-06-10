from pyspark.sql import SparkSession

def init_aws_secret(spark):
    sc = spark.sparkContext
    
    accessKeyId = os.environ['AWS_ACCESS_KEY_ID']
    secretAccessKey = os.environ['AWS_SECRET_ACCESS_KEY']
    
    sc.hadoopConfiguration.set("fs.s3n.awsAccessKeyId", accessKeyId)
    sc.hadoopConfiguration.set("fs.s3n.awsSecretAccessKey", secretAccessKey)

  

def load_s3_data(spark):
    pass

if __name__ == "__main__":
    init_aws_secret(spark)
    load_s3_data(spark)
    
    spark.stop()
