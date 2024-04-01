set={'do','i','have','common','elements','wrt','anotherSet'}
anotherSet={'i','may','contain','elements','pertaining','to','set'}
if set.intersection(anotherSet) == {}:
    print("both the sets are unique wrt each other")
else:
    print("both sets have some elements in common : ",set.intersection(anotherSet))