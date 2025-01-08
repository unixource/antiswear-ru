# https://github.com/unixource/antiswear-ru v.1 main 

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

prefixes = "хуе хуи хуй хую хуя пизд пезд блят бляд сук пидар пидор еб бзд долбаеб пидр педр хул залуп спизд спизж пизж".split()
stdprefixes = "ни а о вы до за из изъ ис на недо надъ не о об объ от отъ по под подъ пере пре пред предъ при про раз рас разъ съ со су через черес чрез черезъ вз взъ довы без бес".split()
short = "бля нах".split()

list = stdprefixes.copy()
for first in list:
    for second in list:
        stdprefixes.append(first+second)

for p in prefixes.copy():
    for stdp in stdprefixes:
        prefixes.append(stdp+p)

def replaceBypasses(word: str) -> str:
    for old, new in bpss:
        word = word.replace(old, new)
    before = ""
    output = ""
    for letter in word:
        if letter != before:
            output += letter
            before = letter
    return output

def check(text: str) -> bool:
    for word in text.split():
        word = word.lower()
        word = replaceBypasses(word)
        for prefix in prefixes:
            if (word.startswith(prefix) or
                word in short): return True
    return False
        
def test() -> None:
    print("-- ANTISWEAR --")
    while True:
        print(">", check(input("Text: ")))

if __name__ == "__main__":
    test()
