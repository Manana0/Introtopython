products = {"candy": 10, "juice": 5, "pen": 50}
def check(product, num):
    for key, value in products.items():
        if key == product and value >= num:
            return True
            break
    return False 