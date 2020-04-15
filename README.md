# ThunderX Smoke

A smoke test for the Cavium ThunderX system. Checks that Python and the most frequently utilized modules are set up and working properly.

## Usage

```bash
ssh <UNIQNAME>@cavium-thunderx.arc-ts.umich.edu

git clone <THIS_REPO>
cd thunderx-smoke

# Run a test on Python 3.7.4 with NumPy and SciPy modules 
/sw/dsi/aarch64/centos7/python/3.7.4/bin/python3 ./num-integration.py
```

## References

[NumPy Tutorial](https://cs231n.github.io/python-numpy-tutorial/)
