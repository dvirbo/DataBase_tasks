from pyspark import SparkContext
import findspark
from pyspark.sql import SQLContext
from pyspark.sql.functions import col

findspark.init()
sc = SparkContext("local[*]", "Simple App")
sqlContext = SQLContext(sc)
my_year = 2022

# start q1:
df = sqlContext.read.json("books.json", multiLine=True)
ndf = df.filter(col("author").startswith("F")).select("title", "author", "year").withColumn("year", my_year - col(
    "year")).show()
# end q1


# start q2
df.filter(col("language").startswith("English")).select("pages", "author").groupBy("author").avg("pages").show()
# end q2
