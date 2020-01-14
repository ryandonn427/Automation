import os
from datetime import datetime

stats = os.stat(('zen_of_python.txt'))
print(datetime.fromtimestamp(stats.st_atime))

print(os.path.getsize('zen_of_python.txt'))
print(os.path.getmtime('zen_of_python.txt'))
print(os.path.getatime('zen_of_python.txt'))
