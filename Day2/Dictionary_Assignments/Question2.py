"""
2) create a dictionary with pairs
	soap:100
	deo:300
	perfume:400

	now accept a product name from user (in any case, so you have to handle "ignore case") and display its price. Also , if the product is not present in the dictionary display the error message " product not available "
	Note:  you should not get "KeyError:" in the program.
"""

mydict={'soap':100,'deo':300,'perfume':400}
print(mydict)

product= input("Enter the name of the product to get the price : ")
product=product.casefold()
isvailable=False
for i in mydict.keys():
    if product==i:
        isvailable=True
        print(mydict[i])
        break

if not(isvailable):
    print("product not available")
