from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()#tweetsDF.select(F.explode(tweetsDF.results).alias('user')).select('user.*').show(truncate=False)

# spark is from the previous example.
sc = spark.sparkContext

# A JSON dataset is pointed to by path.
# The path can be either a single text file or a directory storing text files
path = "/app/data/Tweets.json"
tweetsDF = spark.read.json(path)

# The inferred schema can be visualized using the printSchema() method
# tweetsDF.printSchema()
# root
#  |-- age: long (nullable = true)
#  |-- name: string (nullable = true)

# Creates a temporary view using the DataFrame
tweetsDF.createOrReplaceTempView("tweets")

# SQL statements can be run by using the sql methods provided by spark
tweetUsersDF = spark.sql("SELECT id,created_at,user.name,user.screen_name,retweeted_status.quoted_status.user.location,text FROM tweets")
tweetUsersDF.show()

# tweetsDF.select(F.explode(tweetsDF.results).alias('user')).select('user.*').show(truncate=False)
# +------+{
# |  name|
# +------+
# |Justin|
# +------+

# Alternatively, a DataFrame can be created for a JSON dataset represented by
# an RDD[String] storing one JSON object per string
#jsonStrings = ['{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}']
#othertweetsRDD = sc.parallelize(jsonStrings)
#othertweets = spark.read.json(othertweetsRDD)
#othertweets.show()
# +---------------+----+
# |        address|name|
# +---------------+----+
# |[Columbus,Ohio]| Yin|
# +---------------+----+
# spark is from the previous example.
#sc = spark.sparkContext

# A JSON dataset is pointed to by path.
# The path can be either a single text file or a directory storing text files
#path = "examples/src/main/resources/tweets.json"
#tweetsDF = spark.read.json(path)

# The inferred schema can be visualized using the printSchema() method
#tweetsDF.printSchema()
# root
#  |-- age: long (nullable = true)
#  |-- name: string (nullable = true)

# Creates a temporary view using the DataFrame
#tweetsDF.createOrReplaceTempView("tweets")

# SQL statements can be run by using the sql methods provided by spark
#teenagerNamesDF = spark.sql("SELECT name FROM tweets WHERE age BETWEEN 13 AND 19")
#teenagerNamesDF.show()
# +------+
# |  name|
# +------+
# |Justin|
# +------+

# Alternatively, a DataFrame can be created for a JSON dataset represented by
# an RDD[String] storing one JSON object per string
#jsonStrings = ['{"name":"Yin","address":{"city":"Columbus","state":"Ohio"}}']
#othertweetsRDD = sc.parallelize(jsonStrings)
#othertweets = spark.read.json(othertweetsRDD)
#othertweets.show()
# +---------------+----+
# |        address|name|
# +---------------+----+
# |[Columbus,Ohio]| Yin|
# +---------------+----+
