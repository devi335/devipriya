def linearSearchProduct(productList, targetProduct):
  indices= []

for index, product in enumerate(productList):
  if product == targetProduct:
    indices.append(index)

  return indices


#Example usuage:
products = ["shoes", "boot", "loafter", "shoes", "sandal",
"shoes"]
target = "shoes"
target2='apple'
result = linearSearchProduct(product, target)
print(result)
