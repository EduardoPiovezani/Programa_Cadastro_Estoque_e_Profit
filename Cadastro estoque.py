# Dicionário para armazenar produtos e estoque
products = {}

# Função de cadastro do produto e estoque
def add_product_storage(products):
    '''
    Função criada para adicionar produtos e seus respectivos valores a biblioteca products.
    Retorna a mensagem de que o produto doi cadastrado com sucesso no dicionario.

    '''
    product = input('Add a product: ')
    quantity = int(input('Add the stock quantity: '))
    cost = float(input('Enter the product cost: '))
    sell_price = float(input('Enter the selling price of the product: '))

    products[product] = {
        'quantity': quantity,
        'cost': cost,
        'sell_price': sell_price
    }
    print(f'Product "{product}" added successfully!')

# Função para calcular o lucro do produto
def profit_calculate(products, product_name):
    '''
    Função que recebe a lista de produtos como parametro e recebe um input do usuario para consulta.
    Retorna o lucro por unidade e o lucro total do produto informado, para o usuario.
    '''
    if product_name in products:
        cost = products[product_name]['cost']
        sell_price = products[product_name]['sell_price']
        quantity = products[product_name]['quantity']
        profit_u = sell_price - cost
        profit_total = profit_u * quantity
        print(f'The product "{product_name}" has a profit of R${profit_u} per unit and R${profit_total} in total profit!')

# Menu de opções
while True:
    try:
        user_choice = int(input('\nChoose an option: \n 1 - Add Product \n 2 - Calculate Profit \n 3 - Exit\n'))

        if user_choice == 1:
            add_product_storage(products)
        elif user_choice == 2:
            product_name = input('Enter the name of the product you want to calculate profit for: ')
            profit_calculate(products, product_name)
        elif user_choice == 3:
            print('Exiting the program')
            break
        else:
            print('Please enter a valid option')

    except ValueError:
        print('Error: Invalid input')
