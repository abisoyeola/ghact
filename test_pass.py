def ver_password(x, y):
    return x == y


def test_verify():
    assert ver_password("idris", "idris") == True