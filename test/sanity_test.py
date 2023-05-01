import os.path

def test_sanity():
    path: str = '../mada_reports'
    result: bool = os.path.exists(path)
    assert result == True
    result1: bool = os.path.isdir(path)
    assert result1 == True
    result2: int = len(os.listdir(path))
    assert result2 >= 1

