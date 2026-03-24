def apply_discount(price, discount):
    if isinstance(price, int) == 1 or isinstance(price, float) == 1:
        if price <= 0:
            return "The price should be greater than 0"
        else:
            if isinstance(discount, int) == 1 or isinstance(discount, float) == 1:
                if discount < 0 or discount > 100:
                    return "The discount should be between 0 and 100"
                else:
                    discount = price * (discount / 100)
                    price = price - discount
                    return price

            else:
                return "The discount should be a number"
    else:
        return "The price should be a number"


print(apply_discount(100, 20))
