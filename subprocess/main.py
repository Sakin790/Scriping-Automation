"""
subprocess.run()

subprocess.Popen()

subprocess.call()

"""

import subprocess

result = subprocess.run(["ls","-l"], capture_output=True, text=True)
print(result.stdout)
"""
capture_output=True captures stdout and stderr.
text=True means output is returned as a string (not bytes)
"""