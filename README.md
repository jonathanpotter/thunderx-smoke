# ThunderX Smoke

A smoke test for the Cavium ThunderX system. Checks that Python and the most frequently utilized modules are set up and working properly.

## Usage

```bash
ssh <UNIQNAME>@cavium-thunderx.arc-ts.umich.edu

git clone <THIS_REPO>
cd thunderx-smoke

# Run a test with Python 3.7.4 with NumPy and SciPy modules on login node.
/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3 ./num-integration.py

# Launch PySpark with Python 3.74 with `default` queue
pyspark --master yarn --queue default \
  --num-executors 10 \
  --conf "spark.pyspark.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3" \
  --conf "spark.pyspark.driver.python=/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3"

# Enter contents of num-integration.py file.

# Submit a test to Spark
spark-submit --master yarn --queue default \
  ../spark/examples/src/main/python/pi.py 10
```

## References

- [NumPy Tutorial](https://cs231n.github.io/python-numpy-tutorial/)
- [Basic Numerical Integration: the Trapezoid Rule](https://nbviewer.jupyter.org/github/ipython/ipython/blob/master/examples/IPython%20Kernel/Trapezoid%20Rule.ipynb)
