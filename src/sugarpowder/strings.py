import unicodedata


def fix_mac_hangul(s: str) -> str:
    """
    macOS에서 생성된 파일명이나 문자열의 한글 자모 분리 현상을 수정한다.

    macOS는 유니코드 정규화 방식으로 NFD를 사용하여 한글을 자모 단위로 분리해 저장한다.
    이로 인해 다른 OS에서 깨진 문자열처럼 보이는 문제가 발생한다.
    NFC로 재정규화하여 완성형 한글로 복원한다.
    """
    return unicodedata.normalize("NFC", s)


def strip_invisible(s: str) -> str:
    """
    문자열에서 보이지 않는 유니코드 문자를 제거한다.

    zero-width space, BOM, left-to-right mark 등 유니코드 Cf(Format) 카테고리에
    해당하는 문자들을 제거한다. 복사-붙여넣기나 웹에서 가져온 텍스트에
    숨겨진 문자가 섞여 있을 때 유용하다.

    제거 대상 예시:
        U+200B  ZERO WIDTH SPACE
        U+200C  ZERO WIDTH NON-JOINER
        U+200D  ZERO WIDTH JOINER
        U+200E  LEFT-TO-RIGHT MARK
        U+200F  RIGHT-TO-LEFT MARK
        U+FEFF  ZERO WIDTH NO-BREAK SPACE (BOM)
        U+2060  WORD JOINER
    """
    return "".join(c for c in s if unicodedata.category(c) != "Cf")
