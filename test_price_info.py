import price_info

def test_total_cost_of_shopping():
    print(dict.values(price_info.price_list))
    price_info.price_list["orange"] = 2
    print(dict.values(price_info.price_list))
    print(dict.values(price_info.quantity_list))
    price_info.quantity_list["orange"] = 10
    print(dict.values(price_info.quantity_list))
    result = []
    result = price_info.total_cost_shopping()
    assert(result==59.75)



def test_cost_of_fruit():
   result = price_info.cost_of_fruits('apple',20)
   assert(result==24)

   















    


