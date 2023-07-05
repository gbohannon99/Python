#This program will tell you what version of Python you are using

import sys

version = sys.version_info

version_major = version.major
version_minor = version.minor

print(f"You are using Python {version_major}.{version_minor}"+)


