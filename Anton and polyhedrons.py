polyhedrons = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}

number_polyhedrons = int(input())

list_polyhedrons = []
for i in range(number_polyhedrons):
    list_polyhedrons.append(input())

faces = 0
for i in range(len(list_polyhedrons)):
    faces += polyhedrons[list_polyhedrons[i]]

print(faces)
print('hello')
