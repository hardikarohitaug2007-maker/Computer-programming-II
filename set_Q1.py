s1 = {'Math', 'Physics', 'Chemistry'}
s2 = {'Physics', 'Biology', 'Math'}

print("Common Subjects: ", s1 & s2)

print("Only First Student: ", s1 - s2)

print("Only Second Student: ", s2 - s1)

print("Total Unique Subjects: ", s1 | s2)
