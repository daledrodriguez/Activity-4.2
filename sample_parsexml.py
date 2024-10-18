import xml.etree.cElementTree as et
path = r"/home/devasc/Desktop/sample-1.xml"
tree = et.parse(path)

root = tree.getroot()

Job_Title = []
Company_Name = []
Category = []
City = []

for title in root.iter('job_title'):
   Job_Title.append(title.text)


for company in root.iter('company_name'):
   Company_Name.append(company.text)


for categories in root.iter('category'):
   Category.append(categories.text)


for cities in root.iter('city'):
   City.append(cities.text)


print(Job_Title)
print(Company_Name)
print(Category)
print(City)

















































