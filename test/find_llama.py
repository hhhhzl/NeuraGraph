import os
import llama_index


# Assuming the conda environment is activated, we can use the sys module to find the installation path
import sys

# Finding the path for 'llama-index' package
package_name = "llama_index"
paths = [p for p in sys.path if package_name in p]

# Displaying the found paths
print(paths)
print(llama_index.__file__)