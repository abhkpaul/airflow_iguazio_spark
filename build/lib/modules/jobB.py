from mlrun import get_or_create_ctx
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
import random
import string
import math

def main():
    print("param : ")
    context = get_or_create_ctx("pyspark")
    spark = SparkSession.builder.master("local").appName("SparkJobB").getOrCreate()

    start = 0
    end = 10000
    Range = range(start, end + 1)

    rdd = spark.sparkContext.parallelize(Range).map(lambda x: (x, clustered(x, end),
                                                               scattered(x, end),
                                                               randomised(x, end),
                                                               randomString(50),
                                                               padSingleChar("x", 4000)))

    df = rdd.toDF()\
        .withColumnRenamed("_1", "ID")\
        .withColumnRenamed("_2", "CLUSTERED")\
        .withColumnRenamed("_3", "SCATTERED")\
        .withColumnRenamed("_4", "RANDOMISED")\
        .withColumnRenamed("_5", "RANDOM_STRING")\
        .withColumnRenamed("_6", "PADDING")

    df.printSchema()
    df.show()

    print(df.count())

    df.write.mode("overwrite").parquet("sparksimulation/dummyData.parquet")

    return df

def randomString(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def clustered(x,numRows):
    return math.floor(x -1)/numRows

def scattered(x,numRows):
    return abs((x -1 % numRows))* 1.0

def randomised(seed,numRows):
    random.seed(seed)
    return abs(random.randint(0, numRows) % numRows) * 1.0

def padString(x,chars,length):
    n = int(math.log10(x) + 1)
    result_str = ''.join(random.choice(chars) for i in range(length-n)) + str(x)
    return result_str

def padSingleChar(chars,length):
    result_str = ''.join(chars for i in range(length))
    return result_str

def println(lst):
    for ll in lst:
      print(ll[0])

if __name__ == '__main__': main()