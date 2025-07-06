from calculator.logic import judge_score

def test_judge_score():
    assert judge_score(80) == "Pass"
    assert judge_score(59) == "Fail"
