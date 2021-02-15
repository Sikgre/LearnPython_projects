# phones = ['iPhone Xs', 'Xiaomi Mi8', 'Samsung Galaxy S10']
# print(phones)
# print(len(phones))
# phones.append('Iphone 6')
# phones.append('Iphone 6')
# print(phones)
# print(len(phones))
# print(phones.count('Iphone 6'))
# print(phones.count('Samsung'))
# print(phones[2])
# print(phones[2:4])
# print(phones[-3])
# print(phones.index('Iphone 6'))
# phones.sort()
# print(phones)
# del phones[3]
# print(phones)
# print('Samsung' in phones)
# print('Samsung Galaxy S10' in phones)
# phones.remove('Iphone 6')
# print(phones)


# figures = [3, 5, 7, 9, 10.5]
# print(figures)
# figures.append('Python')
# print(len(figures))
# print(figures[0])
# print(figures[-1])
# print(figures[1:4])
# figures.remove('Python')
# print(figures)

# product = {
#     "name": "Iphone Xs", 
#     "stock": 24, 
#     "price": 65000.0
# }
# print(product)
# print(len(product))

# product['stock']=10
# print(product)

# product['memory']=64
# print(product)

# print(product['name'])
# print(product.get('name'))
# print(product.get('name', 'discount'))
# print(product.get('discount'))
# print(product.get('discount', 10))

# del product['stock']
# print(product)

# product['recommend'] = phones
# print(product)

# product = {
#     "name": "Iphone Xs", 
#     "stock": 24, 
#     "price": 65000.0,
#     "recommend": phones
# }

# print(product["recommend"][1])
# product['recommend'].append('Iphone 6')
# print(product)

# stock = [
#     {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 
#      'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
#     {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
#     {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
# ]

# print(stock)

# print(stock[2])
# stock[2]["price"] = stock[2]["price"] - 8000
# print(stock[2]["price"] - 30000.5)
# print(stock[0]["recomended"][1])
# print(type(stock))
# print(type(stock[0]))

weather = {
    "city": "Москва",
    "temperature": 20
}

print(weather)
print(weather['city'])
weather['temperature'] = weather['temperature'] - 5
print(weather)
print(weather.get('country'))
print(weather.get('country', 'Россия'))
print(len(weather))

weather['date'] = '27.05.2019'
print(len(weather))


