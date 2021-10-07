productList = [[0, 'TShirt','Apparels',500], [1, 'Trousers','Apparels',600], [2, 'Scarf','Apparels',250],
               [3, 'Smartphone','Electronics',20000],[4, 'iPad','Electronics',30000],[5, 'Laptop','Electronics',50000],
               [6,'Eggs','Eatables',5], [7,'Chocolate','Eatables',10],[8,'Juice','Eatables',100],
               [9,'Milk','Eatables',45]]
costComponent=[]
apparels_cost=0
electronics_cost=0
eatables_cost=0
discounted_taxed_apparels_cost=0
discounted_taxed_electronics_cost=0
discounted_taxed_eatables_cost=0
total_cost_including_tax=0
total_tax=0
total_cost_after_coupon_discount=0


def show_menu():
    print('============================================================================================')
    print('                                        MY BAZAAR                                           ')
    print('============================================================================================')
    print('Hello! Welcome to my grocery store!')
    print('Following are the products available in the shop:')
    print('                                                                                            ')
    print("--------------------------------------------------------------------------------------------")
    print('      CODE        |         DESCRIPTION        |       CATEGORY       |      COST(Rs)       ')
    print("--------------------------------------------------------------------------------------------")
    print('        0         | Tshirt                     | Apparels             | 500                 ')
    print('        1         | Trousers                   | Apparels             | 600                 ')
    print('        2         | Scarf                      | Apparels             | 250                 ')
    print('        3         | Smartphone                 | Electronics          | 20,000              ')
    print('        4         | iPad                       | Electronics          | 30,000              ')
    print('        5         | Laptop                     | Electronics          | 50,000              ')
    print('        6         | Eggs                       | Eatables             | 5                   ')
    print('        7         | Chocolate                  | Eatables             | 10                  ')
    print('        8         | Juice                      | Eatables             | 100                 ')
    print('        9         | Milk                       | Eatables             | 45                  ')
    print("--------------------------------------------------------------------------------------------")


def get_regular_input():
    print("--------------------------------------------------------------------------------------------")
    print('ENTER ITEMS YOU WISH TO BUY')
    print("--------------------------------------------------------------------------------------------")
    itemcode = input('Enter the item codes (space-separated):')
    itemcode = itemcode.split()
    i=0
    for i in range(len(itemcode)):
        itemcode[i] = int(itemcode[i])
        if itemcode[i] not in range(0, 10):
            print("Invalid")
            itemcode.pop(i)
    quantities = []
    for j in range(0, 10):
        n = itemcode.count(j)
        quantities.append(n)
    return quantities
    print()


def get_bulk_input():
    quantities=[0,0,0,0,0,0,0,0,0,0]
    print("--------------------------------------------------------------------------------------------")
    print('ENTER ITEM AND QUANTITIES')
    print("--------------------------------------------------------------------------------------------")
    while True:
        x= input('Enter code and quantity (leave blank to stop) : ')
        if x=='':
            print('Your order has been finalized.')
            print()

            break

        x = x.split()

        for i in range(len(x)):
            x[i] = int(x[i])

        if x[0] in list(range(0,10)):
            if x[1] > 0:
                quantities[x[0]]=quantities[x[0]]+x[1]
                print('You added '+ str(x[1])+' '+ str(productList[x[0]][1]))
                print()
            else:
                print('Invalid quantity. Try again')
                print()


        elif x[0] not in list(range(0, 10)):
            if x[1] > 0:
                print('Invalid code. Try again')
                print()

            else:
                print('Invalid code and quantity. Try again')
                print()
    print(x)
    print(quantities)
    return(quantities)


def print_order_details(quantities):
    print("--------------------------------------------------------------------------------------------")
    print('ORDER DETAILS')
    print("--------------------------------------------------------------------------------------------\n")
    print()
    costComponent=[]
    n=1
    for i in range(0, 10):
        costComponent1 = (quantities[i] * productList[i][3])
        costComponent.append(costComponent1)
        if quantities[i] == 0:
            continue
        print("[" + str(n) + "] " + productList[i][1] + " x " + str(quantities[i]) + " = Rs " + str(productList[i][3]) + " * " + str(quantities[i]) + " = Rs " + str(quantities[i] * productList[i][3]))
        n=n+1
    print()



def calculate_category_wise_cost(quantities):
    print(quantities)
    global apparels_cost
    global electronics_cost
    global eatables_cost
    print("--------------------------------------------------------------------------------------------")
    print('CATEGORY-WISE COST')
    print("--------------------------------------------------------------------------------------------")
    for i in range(0, 10):
        costComponent1 = (quantities[i] * productList[i][3])

        if i>=0 and i<3:
            apparels_cost = apparels_cost + costComponent1
        if i>=3 and i<6:
            electronics_cost = electronics_cost + costComponent1
        if i>=6 and i<10:
            eatables_cost = eatables_cost + costComponent1
    print()
    print('Apparels = ' + str(apparels_cost))
    print('Electronics = ' + str(electronics_cost))
    print('Eatables = ' + str(eatables_cost))
    print(apparels_cost, electronics_cost, eatables_cost)
    return(apparels_cost, electronics_cost, eatables_cost)



def get_discount(cost, discount):
    return int(cost * discount)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    print("--------------------------------------------------------------------------------------------")
    print('DISCOUNTS')
    print("--------------------------------------------------------------------------------------------")
    if apparels_cost >= 2000:
        discounted_apparels_cost = apparels_cost - get_discount(apparels_cost,0.1)
        I=get_discount(apparels_cost,0.1)
        print('[APPAREL] Rs ' + str(apparels_cost) + ' - Rs ' + str(get_discount(apparels_cost,0.1)) + ' = Rs ' + str(discounted_apparels_cost))
    else:
        I=0
        discounted_apparels_cost = apparels_cost
    if electronics_cost >= 25000:
        J=get_discount(electronics_cost,0.1)
        discounted_electronics_cost = electronics_cost - get_discount(electronics_cost,0.1)

        print('[ELECTRONICS] Rs ' + str(electronics_cost) + ' - Rs ' + str(get_discount(electronics_cost,0.1)) + ' = Rs ' + str(discounted_electronics_cost))
    else:
        J=0
        discounted_electronics_cost = electronics_cost
    if int(eatables_cost) >= 500:
        K=get_discount(eatables_cost,0.1)
        discounted_eatables_cost = eatables_cost - get_discount(eatables_cost,0.1)
        print('[EATABLES] Rs ' + str(eatables_cost) + ' - Rs ' + str(get_discount(eatables_cost,0.1)) + ' = Rs ' + str(discounted_eatables_cost))
    else:
        K=0
        discounted_eatables_cost = eatables_cost
    print()
    print('TOTAL DISCOUNT = Rs ' + str(I+J+K))
    print('TOTAL COST = Rs ' + str(discounted_apparels_cost+discounted_electronics_cost+discounted_eatables_cost))
    print()
    print(discounted_apparels_cost,discounted_electronics_cost,discounted_eatables_cost)
    return(discounted_apparels_cost,discounted_electronics_cost,discounted_eatables_cost)


def get_tax(cost, tax):
    return int(cost * tax)


def calculate_tax(discounted_apparels_cost,discounted_electronics_cost,discounted_eatables_cost):
    global discounted_taxed_apparels_cost
    global discounted_taxed_electronics_cost
    global discounted_taxed_eatables_cost
    global total_cost_including_tax
    global total_tax
    print("--------------------------------------------------------------------------------------------")
    print('TAX')
    print("--------------------------------------------------------------------------------------------")
    if discounted_apparels_cost!=0:
        print('[APPAREL] Rs ' + str(discounted_apparels_cost) + ' * ' + str(0.1) + ' = Rs ' + str(get_tax(discounted_apparels_cost,0.1)))
        discounted_taxed_apparels_cost= discounted_apparels_cost+get_tax(discounted_apparels_cost, 0.1)
    if discounted_electronics_cost!=0:
        print('[ELECTRONICS] Rs ' + str(discounted_electronics_cost) + ' * ' + str(0.15) + ' = Rs ' + str(get_tax(discounted_electronics_cost,0.15)))
        discounted_taxed_electronics_cost = discounted_electronics_cost + get_tax(discounted_electronics_cost,0.15)
    if discounted_eatables_cost!=0:
        print('[EATABLES] Rs ' + str(discounted_eatables_cost) + ' * ' + str(0.05) + ' = Rs ' + str(get_tax(discounted_eatables_cost,0.05)))
        discounted_taxed_eatables_cost = discounted_eatables_cost + get_tax(discounted_eatables_cost,0.05)
    print('                                                                                                                                ')
    print('TOTAL TAX = Rs ' + str((get_tax(discounted_apparels_cost,0.1)) + (get_tax(discounted_electronics_cost,0.15)) + (get_tax(discounted_eatables_cost,0.05))))
    print('TOTAL COST = Rs ' + str(discounted_taxed_apparels_cost+discounted_taxed_electronics_cost+discounted_taxed_eatables_cost))
    total_tax= (get_tax(discounted_apparels_cost,0.1)) + (get_tax(discounted_electronics_cost,0.15)) + (get_tax(discounted_eatables_cost,0.05))
    total_cost_including_tax= discounted_taxed_apparels_cost+discounted_taxed_electronics_cost+discounted_taxed_eatables_cost
    print()
    return(total_cost_including_tax, total_tax)


def apply_coupon_code(total_cost_including_tax):
    global total_cost_after_coupon_discount
    print("--------------------------------------------------------------------------------------------")
    print('COUPON CODE')
    print("--------------------------------------------------------------------------------------------")
    print('HELLE25 and CHILL50 are the 2 valid coupon codes')
    while True:
        c = input('Enter coupon code (else leave blank):')
        if c == '' :
            total_coupon_discount=0
            print('No coupon code applied')
            print()
            break

        elif (c == 'HELLE25'):
            if total_cost_including_tax >= 25000 and total_cost_including_tax <= 50000 :
                total_coupon_discount= min(5000,total_cost_including_tax*0.25)
                print('[HELLE25] min(5000, Rs '+ str(total_cost_including_tax)+(' * 0.25) = Rs '+ str(total_coupon_discount)))
                break
            else:
                print('Coupon not applicable')

        elif (c == 'CHILL50'):
            if total_cost_including_tax >= 50000:
                total_coupon_discount = min(10000, total_cost_including_tax * 0.5)
                print('[CHILL50] min(10000, Rs ' + str(total_cost_including_tax) + (
                            ' * 0.5) = Rs ' + str(total_coupon_discount)))
                break
            else:
                print('Coupon not applicable')
                print()
        elif c!='HELLE25'and c!='CHILL50':
            print('Invalid coupon code. Try again.')
            print()

    total_cost_after_coupon_discount=total_cost_including_tax - total_coupon_discount
    print('TOTAL COUPON DISCOUNT = Rs '+ str(total_coupon_discount))
    print('TOTAL COST = Rs '+ str(total_cost_after_coupon_discount))
    print()
    return(total_cost_after_coupon_discount, total_coupon_discount)



def main():
    show_menu()
    print()
    quantities = []
    while True:
        i = input('Would you like to buy in bulk? (y or Y / n or N):')
        if (i == 'n') or (i == 'N'):
            quantities = get_regular_input()
            break
        elif (i == 'Y') or (i == 'y'):
            quantities = get_bulk_input()
            break
    print()
    q=print_order_details(quantities)
    r=calculate_category_wise_cost(quantities)
    s=calculate_discounted_prices(r[0],r[1],r[2])
    t=calculate_tax(s[0],s[1],s[2])
    apply_coupon_code(total_cost_including_tax)
    print()
    print('Thank you for visiting!')



if __name__ == '__main__':
    main()




