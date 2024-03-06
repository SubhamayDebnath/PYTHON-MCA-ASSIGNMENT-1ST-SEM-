country={1:'India',2:'Nepal',3:'Spain',4:'USA',5:'Japan'}
search=int(input("Enter:"))
if search in country:
    print(f"Search item is {search} : {country[search]}")
else:
    print(f"Search item {search} is not found")