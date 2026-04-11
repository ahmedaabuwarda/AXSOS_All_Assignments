# 1
x = [ [5,2,3], [10,8,9] ]

students = [ {'first_name': 'Michael', 'last_name' : 'Jordan'}, 
            {'first_name' : 'John', 'last_name' : 'Rosales'}]

sports_directory = { 'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'], 
                    'soccer' : ['Messi', 'Ronaldo', 'Rooney']}

z = [ {'x': 10, 'y': 20} ]

for i in range(len(x)):
    for j in range(len(x[i])):
        if (x[i][j] == 10):
            x[i][j] = 15

print(x)
students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"

print(sports_directory)

for i in range(len(z)):
    for k, v in z[i].items():
        if (v == 20):
            z[i][k] = 30

print(z)

# 2
students = [ {'first_name': 'Michael', 'last_name' : 'Jordan'}, 
            {'first_name' : 'John', 'last_name' : 'Rosales'}, 
            {'first_name' : 'Mark', 'last_name' : 'Guillen'}, 
            {'first_name' : 'KB', 'last_name' : 'Tonel'} ]

def iterateDictionary(list):
    for i in list:
        for k, v in i.items():
            print(k, "-", v, end=", ")
        print()

iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# 3
def iterateDictionary2(key_name, list):
    for i in list:
        print(i[key_name])


iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for k, v in some_dict.items():
        print(len(v), k)
        for e in v:
            print(e)

printInfo(dojo)