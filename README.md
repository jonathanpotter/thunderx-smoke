# ThunderX Smoke

A smoke test for the Cavium ThunderX system. Checks that Python and the most frequently utilized modules are set up and working properly.

## Usage

```bash
ssh <UNIQNAME>@cavium-thunderx.arc-ts.umich.edu

git clone <THIS_REPO>
cd thunderx-smoke

# Test Spark with 100 partitions. Job takes about 1 minute.
spark-submit --master yarn --queue workshop \
  --num-executors 10 \
  --conf "spark.pyspark.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  --conf "spark.pyspark.driver.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  /usr/lib/spark/examples/src/main/python/pi.py 100

# Test NumPy with simple mod.
spark-submit --master yarn --queue workshop \
  --num-executors 20 \
  --conf "spark.pyspark.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  --conf "spark.pyspark.driver.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  ./numpy-test.py

# Test SciPy with a numeric integration.
# This test does not run on the datanodes; only on the login node. Needs improvement.
spark-submit --master yarn --queue workshop \
  --num-executors 5 \
  --conf "spark.pyspark.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  --conf "spark.pyspark.driver.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  ./numeric-integration.py

# Test word count
spark-submit --master yarn --queue workshop \
  --num-executors 40 \
  --conf "spark.pyspark.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  --conf "spark.pyspark.driver.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  ./word-count.py
```

## Configuration

Note that Python2 is the default installation on the cluster for use by system tools. Users must specify Python3 if they want to use the latest modules such as NumPy. Otherwise, these tests and their jobs will likely fail.

## References

- [NumPy Tutorial](https://cs231n.github.io/python-numpy-tutorial/)
- [Basic Numerical Integration: the Trapezoid Rule](https://nbviewer.jupyter.org/github/ipython/ipython/blob/master/examples/IPython%20Kernel/Trapezoid%20Rule.ipynb)
