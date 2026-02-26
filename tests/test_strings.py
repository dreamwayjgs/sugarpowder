from sugarpowder.strings import fix_mac_hangul, strip_invisible


def test_fix_mac_hangul():
    decomposed = "\u1100\u1161"  # 'ㄱ' + 'ㅏ' (NFD)
    assert fix_mac_hangul(decomposed) == "가"


def test_fix_mac_hangul_already_composed():
    assert fix_mac_hangul("가나다") == "가나다"


def test_strip_invisible_zero_width_space():
    assert strip_invisible("hello\u200bworld") == "helloworld"


def test_strip_invisible_bom():
    assert strip_invisible("\ufeffhello") == "hello"


def test_strip_invisible_multiple():
    assert strip_invisible("\u200b\u200c\u200dhello\u2060") == "hello"


def test_strip_invisible_clean_string():
    assert strip_invisible("hello world") == "hello world"
