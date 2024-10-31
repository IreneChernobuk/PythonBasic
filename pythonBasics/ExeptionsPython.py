ItemsInCart = 0
# 2 items will be added to cart
if ItemsInCart != 2:
    # raise Exception("Products Cart count not matching")
    pass

assert (ItemsInCart == 0)
# try , catch

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
    # print("Somehow I reached  this block because there is failure in try block")
finally:
    print("cleaning up resources")
