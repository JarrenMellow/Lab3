import lab2.Lab2 as lab2


def test_find_min_max():
    result = []
    input_array = [14,25,654,12]
    result = lab2.find_min_max(input_array)
    assert(result) == (654,12)
    


def test_calc_average():
    input_array = [5,7,12,4]
    test_array= 7.0
    result = []
    result = lab2.calc_average(input_array)
    assert(result==test_array)

def test_calc_median_temp():
    input_array = [12,543,10,20,70]
    test_array = 20.0
    result=[]
    result = lab2.calc_median_temperature(input_array)
    assert(result==test_array)
    



