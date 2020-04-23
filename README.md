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

# Submit a test to Spark
# Job will run and then terminate in about 1 minute.
# Note that the job actually runs locally is not in the cluster.
spark-submit --master yarn --queue default \
  --num-executors 5 \
  ./num-integration.py

# Test word count
spark-submit --master yarn --queue workshop \
  --num-executors 40 \
  --conf "spark.pyspark.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  --conf "spark.pyspark.driver.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  ./word-count.py
```

## References

- [NumPy Tutorial](https://cs231n.github.io/python-numpy-tutorial/)
- [Basic Numerical Integration: the Trapezoid Rule](https://nbviewer.jupyter.org/github/ipython/ipython/blob/master/examples/IPython%20Kernel/Trapezoid%20Rule.ipynb)
