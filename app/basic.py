masterAddr = "spark://0.0.0.0:7077"
import findspark
findspark.init()
from pyspark import SparkContext
sc = SparkContext(appName="WordCount", master=masterAddr)