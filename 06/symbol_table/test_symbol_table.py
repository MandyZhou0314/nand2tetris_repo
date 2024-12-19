from symbol_table import Symbol_table

def test_get():
    st = Symbol_table()
    assert st.get("R0") == 0
    assert st.get("KBD") == 24576
    st.add("sum", 16)
    assert st.get("sum") == 16