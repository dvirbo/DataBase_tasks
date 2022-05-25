from pyspark import SparkContext
import findspark
from pyspark.sql import SQLContext
from pyspark.sql.functions import col, expr

findspark.init()
sc = SparkContext("local[*]", "Simple App")
sqlContext = SQLContext(sc)
my_year = 2022

df = sqlContext.read.json("books.json", multiLine=True)
ndf = df.filter(col("author").startswith("F")).select("title", "author", "year").show()  # q1
'''
rdd = ndf.rdd
sub = rdd.reduce(lambda row: my_year - row.year).collect()
finish = sqlContext.createDataFrame(sub).show()
'''



''' # q2
df.filter(col("language").startswith("English")).select("pages", "author") 
rdd = df.rdd
calc_amount = rdd.map(lambda row: (row.author, row.pages)) \
    .reduceByKey(lambda a, b: a + b) \
    .collect()

for author, sum_amount in calc_amount:
    print('%s : %s' % (author, sum_amount))

'''
