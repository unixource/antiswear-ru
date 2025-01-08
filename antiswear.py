# https://github.com/unixource/antiswear-ru v.01 

bpss = [
        ("iu", "ю"),
        ("yu", "ю"),
        ("ia", "я"),
        ("yo", "е"),
        ("ё", "е"),
        ("x", "х"),
        ("y", "у"),
        ("e", "е"),
        ("h", "х"),
        ("u", "у"),
        ("i", "и"),
        ("6", "б"),
        ("/\\", "л"),
        ("p", "п"),
        ("z", "з"),
        ("3", "з"),
        ("d", "д"),
        ("a", "а"),
        ("o", "о"),
        ("0", "о"),
        ("-", ""),
        ("_", "")
        ]

prefixes = "хуё хуи хуй хую хуя пизд блят бляд сук пидар пидор еба".split()
short = "бля нах".split()

def replaceBypasses(word: str) -> str:
    for old, new in bpss:
        word = word.replace(old, new)
    before = ""
    output = ""
    for letter in word:
        if letter != before:
            before = letter
            output += letter
    return word

def check(text: str) -> bool:
    for word in text.split():
        word = word.lower()
        word = replaceBypasses(word)
        for prefix in prefixes:
            if (prefix in word or
                word in ["бля", "нах"]): return True
    return False
        
def test() -> None:
    print("-- ANTISWEAR --")
    while True:
        print(">", check(input("Text: ")))

if __name__ == "__main__":
    test()
