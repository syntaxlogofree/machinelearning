# -*- coding: utf-8 -*-

print "first line of python"

# try comment

print "try math", 3 + 7 / 6
print 87 / 3 - 2 * (7 - 3)
print 5 > - 8
print  (8.55 / 3.77) % 2

# use undercore for variable naming

a = 100
b = "this is string"

print "a" + "b"
# print a + b <-- syntax error
print a, b

# formatters: %s, %r, %d

name = "john"
age = 35

print "make up a sentence %s, and %d" % (name, age)
