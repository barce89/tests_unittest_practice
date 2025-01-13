# tenenos que agregar como segundo parametro un descuento





descuento = 10

def calculate(products,des_off):
    total = 0

    for product in products:
        total +=product['price']
    
    descuento =(des_off/100)*total
    print(f'este es el print del descuento{descuento}')
    print(f'este es el print del total antes del descuento{total}')
    total = total-(abs(descuento))
    print(f'este es el print del total despues del descuento{total}')
    return total


def test_calculate():
    # print('prueba')
    assert calculate([],0)==0


def calculate_with_single_list():
    list_products = [
        {
            'name':'Book of the deads',
            'price':45
        }
    ]
    print(f'este es el print de con una single list {calculate(list_products,10)}')
    assert calculate(list_products,10) == 40.5


def calculate_with_a_lot_values():
    list_products = [
        {
            'name':'Book of the deads',
            'price':56
        },
        {
            'name':'the lorf of the rings',
            'price':44
        }
        ,
        {
            'name':'harry potter',
            'price':30
        }

    ]
    # print(calculate(list_products))
    assert calculate(list_products,10) == 117





if __name__=="__main__":
    test_calculate()
    calculate_with_single_list()
    calculate_with_a_lot_values()