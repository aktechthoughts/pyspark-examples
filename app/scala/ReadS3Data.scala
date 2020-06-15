import org.apache.spark.sql.SaveMode
import org.apache.spark.sql.SparkSession

case class Record(key: Int, value: String)

object ReadS3Data {

  def main(args: Array[String]): Unit = {
    val spark = SparkSession
      .builder
      .appName("ReadS3Data")
      .config(sc.getConf)
      .getOrCreate()

    import spark.implicits._

    def bucket_name = sys.env("BUCKET_NAME")
    def aws_access_id = sys.env("AWS_ACCESS_KEY_ID")
    def aws_secret_key  = sys.env("AWS_SECRET_ACCESS_KEY")

    sc.hadoopConfiguration.set("fs.s3a.endpoint", bucket_name)
    sc.hadoopConfiguration.set("fs.s3a.access.key",aws_access_id)
    sc.hadoopConfiguration.set("fs.s3a.secret.key",aws_secret_key)


    val df = spark.read.option("sep", "\t").csv("s3a://amazon-reviews-pds/tsv/amazon_reviews_us_Home_v1_00.tsv.gz")
    
    df.createOrReplaceTempView("records")

    println("Result of SELECT *:")
    spark.sql("SELECT * FROM records").collect().foreach(println)

    val count = spark.sql("SELECT COUNT(*) FROM records").collect().head.getLong(0)
    println(s"COUNT(*): $count")

    spark.stop()
  }
}
