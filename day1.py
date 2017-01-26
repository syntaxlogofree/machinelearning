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

x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)

print x
print y
print "I said: %r" % x
print "I also said: '%s'." % y

# %r is best for debugging, raw data of the variable, the others are used for displaying to users.

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "string 1",
    "string 2",
    "string 3",
    "string 4"
)

# use %s to print Chinese

months = "Jan\nFeb\nMarch"

print months

print """
Jan
Feb
March
"""

# \n or three quotes = <br/>
