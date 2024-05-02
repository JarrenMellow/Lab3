import lab2.bmi as bmi 
def test_bmi_normal_weight():
    result = bmi.calculate_bmi(1.73,57)
    assert(result==0)

def test_bmi_over_weight():
    result = bmi.calculate_bmi(1.50,1800)
    assert(result==1)

def test_bmi_under_weight():
    result = bmi.calculate_bmi(1.70,30)
    assert(result==-1)
