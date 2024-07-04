"""
ASCII码表
.字符串比较大小的依据--ASCII码表

.字符串比较大小
字符串是按位比较的，也就是一位一位的比较，只要有一位大，那么整体就大 
"""

# abc 比较 adb
print(f"abc < adb: {'abd' > 'abc'}")#True

# a 比较 ab
print(f"a < ab: {'ab' > 'a'}")#True

# a 比较 A
print(f"a > A: {'A' < 'a'}")#True

# key1 比较 key2
print(f"key1 > key2: {'key2' < 'key1'}") #False
