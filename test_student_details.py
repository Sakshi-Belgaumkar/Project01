from student_details import check_result

def test_distinction():
    assert check_result(80) == "Distinction"

def test_pass():
    assert check_result(50) == "Pass"

def test_fail():
    assert check_result(30) == "Fail"
