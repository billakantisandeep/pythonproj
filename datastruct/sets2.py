s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = {3, 4, 5}

s4 = s1.intersection(s2)  # All the values in s2 that are in s1
s5 = s1.intersection(s2, s3)
s6 = s1.difference(
    s2
)  # Values that are there in s1 not s2 ( Running the difference method on s1 )
s7 = s2.difference(s1)
s8 = s2.difference(s1, s3)
s9 = s1.symmetric_difference(s2)

print(s4)
print(s5)
print(s6)
print(s7)
print(s8)  # Empty set since s2 values which are not in the s1 and s3
print(s9)   #Gives the values which are different in both the sets. 

# You can do intersection and get the values even if the sets are too big.
# Symetric difference
