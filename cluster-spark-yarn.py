# Test of NumPy on Spark Cluster
# From https://docs.anaconda.com/anaconda-cluster/howto/spark-yarn/
# cluster-spark-yarn.py
from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster('yarn-client')
conf.setAppName('spark-yarn')
sc = SparkContext(conf=conf)


def mod(x):
    import numpy as np
    return (x, np.mod(x, 2))

# Create an RDD of numbers 0-999
# Function take() returns a list
rdd = sc.parallelize(range(1000000)).map(mod).take(10)
print(rdd)
