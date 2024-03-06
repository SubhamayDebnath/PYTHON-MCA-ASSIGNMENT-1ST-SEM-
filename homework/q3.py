country={1:'India',2:'Nepal',3:'Spain',4:'USA',5:'Japan'}
# country.pop(2)
# country.popitem()
key=int(input("Enter the key: "))
filteredCountry={}
for i in country:
    if i == key:
        continue
    else:
        filteredCountry[i]=country[i]
print(filteredCountry)
