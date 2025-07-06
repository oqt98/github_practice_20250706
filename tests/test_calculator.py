# テストファイルtest_calculator.pyの作成

from calculator.calculator import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3



# あえて失敗するテストを書く

from calculator.calculator import add

def test_add_fail():
    assert add(2, 2) == 4  # ← 本当は4だから失敗する！



# 条件分岐

from calculator.calculator import check_grade

def test_check_grade():
    assert check_grade(85) == "A"
    assert check_grade(75) == "B"
    assert check_grade(50) == "C"



# 関数ごとにテストを書く、エラーをあえて出すテスト（例外処理）test_calculator.py

from calculator.calculator import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(10, 0)
        assert False  # ここが通ったら失敗！
    except ValueError:
        assert True  # 例外が出れば成功
