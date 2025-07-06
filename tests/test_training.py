# ０より大きい関数のテスト
from calculator.training import is_positive # ←importのあとにis_positiveを定義

def test_is_positive():
    assert is_positive(2) == True # ２より大きい、０、ー１の場合のテスト
    assert is_positive(10) == True
    assert is_positive(-1) == False

