spark = {
    'name': 'spark',
    'type': 'kupe',
    'color': 'red',
    'position': 1,
}
nexia = {
    'name': 'nexia',
    'type': 'sedan',
    'color': 'red',
    'position': 2,
}

captiva = {
    'name': 'captiva',
    'type': 'sedan',
    'color': 'red',
    'position': 3,
}

ssd = [spark,nexia,captiva]

x = 1
for c in ssd:
    print(str(x) + ' ' + c['name'])
    x += 1

