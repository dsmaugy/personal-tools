# print("123", end='')
# print("\b\b", end='')

import time
import random
import sys

print("a", end='')
for i in range(100):
    print(f"\b{chr(random.randrange(33, 127))}", end='')
    sys.stdout.flush()
    time.sleep(0.01)

print("\bb", end='')
