# NAME: DELE-OSEDELE PRAISE MODELEOLA
# MATRIC NUMBER: 240502041
# COURSE OF STUDY: COMPUTER SCIENCE

# Create an array
scores = [45, 60, 75, 80, 90]

# 1. Traversal
print("Original Array:", scores)

# 2. Insertion
scores.insert(2, 70)
print("After Insertion:", scores)

# 3. Deletion
scores.remove(75)
print("After Deletion:", scores)

# 4. Searching
if 80 in scores:
    print("80 found at index:", scores.index(80))
else:
    print("Element not found")

# 5. Updating
scores[1] = 65
print("After Updating:", scores)

# 6. Sorting (Ascending)
scores.sort()
print("Ascending Order:", scores)

# 7. Sorting (Descending)
scores.sort(reverse=True)
print("Descending Order:", scores)

# 8. Accessing
print("Element at index 2:", scores[2])