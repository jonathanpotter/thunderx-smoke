# Do a word count on Complete Works of Shakespeare

from pyspark import SparkContext

sc = SparkContext(appName = "WordCountExample")

# Create an RDD in PySpark from large text file in HDFS
rdd = sc.textFile("/data/complete-works-of-shakespeare.txt")

# Create function to make it all lower-case and split the lines into words,
# creating a new RDD with each element being a word.
def Func(lines):
    lines = lines.lower()
    lines = lines.split()
    return lines

rdd_flat  = rdd.flatMap(Func)

# Do a word count using a map-reduce like function.
# Map each word with a count of 1 like a key-value pair where the value is 1.
rdd_mapped = rdd_flat.map(lambda x: (x,1))
# Then group each count by key.
rdd_grouped = rdd_mapped.groupByKey()
# Take the sum of each word, then swap the key value pair order,
# then sort by value instead of key.
rdd_frequency = rdd_grouped.mapValues(sum).map(lambda x: (x[1],x[0])).sortByKey(False)

# Print the 10 most frequent words.
print("The 10 most frequent words: {0}".format(rdd_frequency.take(10)))
