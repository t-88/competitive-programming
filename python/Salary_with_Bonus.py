#https://www.beecrowd.com.br/judge/en/problems/view/1009


name = input("name: ")
salary = float(input("fixed salary: "))
total_sale = float(input("fixed total sale: "))


print("TOTAL: R$ %0.2f" % salary + 0.15 * total_sale)