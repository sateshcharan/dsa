def bubble_sort(elements, key):
    for i in range(len(elements)-1):
        for j in range(len(elements)-1-i):
            if elements[j][key] > elements[j + 1][key]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j+1] = temp

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

bubble_sort(elements, 'name')
print(elements)