from code import Code


def test_addr():
    c = Code()
    assert c.addr(4) == "0000000000000100"
    assert c.addr(9) == "0000000000001001"

def test_comp():
    c = Code()
    assert c.comp("D+1") == "0011111"
    assert c.comp("D&M") == "1000000"
    assert c.comp("D-A") == "0010011"
    
def test_dest():
    c = Code()
    assert c.dest("MD") == "011"
    assert c.dest("AMD") == "111"
    
def test_jump():
    c = Code()
    assert c.jump("JGT") == "001"
    assert c.jump("JNE") == "101"