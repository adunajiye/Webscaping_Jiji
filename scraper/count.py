"""
  This module is use to check duplicete url 
  link path from the `car_links.txt` file.
  So, to prevent data redundancy.
"""


# load unique values from file if any duplicate data
with open('./docs/car_links.txt', 'r') as f:
  d = set([x.strip() for x in f.readlines()])
  print(len(d))

# write the unique values back to the file
with open('./docs/car_links.txt', 'w') as f:
  for a in list(d):
    f.write(f'{a}\n')



# Property Categories
with open('./docs/property_links.txt','r') as find_links:
  property =set([x.strip() for x in find_links.readlines()])
  print(len(property))

with open('./docs/property_links.txt','w') as writelinks:
  for y in list(property):
    writelinks.write(f'{y}\n')

print("Done")