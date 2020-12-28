bookPrice = 24.95
discount = .60
shippingPriceRest = .75
shippingPriceFirst = 3.00
totalUnits = 60

bookDiscountAmount = bookPrice * discount * totalUnits
shipping = shippingPriceRest * 59 + shippingPriceFirst

result = bookDiscountAmount + shipping
print('The Total price is: ' + str(result))