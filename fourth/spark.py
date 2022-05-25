from pyspark import SparkContext
import findspark
from pyspark.sql import SQLContext
from pyspark.sql.functions import col, expr

findspark.init()
sc = SparkContext("local[*]", "Simple App")

sqlContext = SQLContext(sc)
# .withColumn("year", expr("2022- num"))
df = sqlContext.read.json("books.json", multiLine=True)
# df.filter(col("author").startswith("F")).select("title", "author", "year").show() # q1


df.filter(col("language").startswith("English")).select("pages", "author") # q2
rdd = df.rdd
calc_amount = rdd.map(lambda row: (row.author, row.pages)) \
    .reduceByKey(lambda a, b: a + b) \
    .collect()

for author, sum_amount in calc_amount:
    print('%s : %s' % (author, sum_amount))
