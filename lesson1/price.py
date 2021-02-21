# def get_summ(one, two, delimiter = "&"):
#     one = str(one).upper()
#     two = str(two).upper()
#     result = f'{one} {delimiter} {two}'
#     return result
# r = get_summ('Learn', 'Python')
# print(r)

def format_price (price):
    price = int(price)
    result = f'Цена: {price} руб.'
    return result
p = format_price(56.24)
print(p)
