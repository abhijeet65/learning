
dict={
    "Amazon":301,
    "Flipkart":12,
    "Akkamai":48,
    "Ninjas":1002,
    "Dexter":90,
    "DirectI":80
};

zipp1=zip(dict.values(),dict.keys())
print(sorted(zipp1))
#print(zipp1)
zipp2=zip(dict.keys(),dict.values())
print(sorted(zipp2))

