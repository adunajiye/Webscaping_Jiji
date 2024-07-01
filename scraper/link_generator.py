
"""
This generate links to each page of the website.
"""

with open('./docs/car_links.txt', 'r') as f:
    data = set([x.split('/')[1] for x in f.readlines()])

with open('./docs/links.txt', 'w') as f:
    for i in data:
        f.write(f'{i}\n')

# property Category

with open('./docs/property_links.txt','r') as readfiles:
    data = set([x.split('/')[1] for x in readfiles.readlines()])

with open('./docs/property_links.txt', 'w') as f:
    for i in data:
        f.write(f'{i}\n')

print(data)
