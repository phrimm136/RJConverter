import os


def test_conversion():
    if "tmp" in os.listdir("./"):
        os.system("rm -r ./tmp")
    required = ["【骨伝導風】道草屋 たびらこ-一緒にはみがき【耳かき&はみがき】",
                "【不健全はみがき】道草屋 すずしろ-はなびの日【ゆっくり按摩】",
                "【爪切り】道草屋 すずしろ日帰り-雨宿り【鼓膜マッサージ】",
                "not_convertable"]
    os.makedirs("./tmp")
    os.makedirs("./tmp/RJ171695")
    os.makedirs("./tmp/rj184314")
    os.makedirs("./tmp/RJ228778 - すずしろ ")
    os.makedirs("./tmp/not_convertable")
    os.system("python ./src/converter.py ./tmp")
    result = os.listdir("./tmp")
    if required[0] not in result:
        os.system("rm -r ./tmp")
        raise RuntimeError("RJ code (UPPER) should be converted, but it was not.")
    elif required[1] not in result:
        os.system("rm -r ./tmp")
        raise RuntimeError("rj code (lower) should be converted, but it was not.")
    elif required[2] not in result:
        os.system("rm -r ./tmp")
        raise RuntimeError("Cannot parse RJ code from messy directory path")
    elif required[3] not in result:
        os.system("rm -r ./tmp")
        raise RuntimeError("Non Rj code should not be converted, but it was.")
    else:
        os.system("rm -r ./tmp")
        print("Conversion test completed.")
