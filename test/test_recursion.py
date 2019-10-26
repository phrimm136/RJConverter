import os


def test_recursion():
    if "tmp" in os.listdir("./"):
        os.system("rm -r ./tmp")
    required = ["【骨伝導風】道草屋 たびらこ-一緒にはみがき【耳かき&はみがき】/not_convertable",
                "not_convertable/【不健全はみがき】道草屋 すずしろ-はなびの日【ゆっくり按摩】",
                "耳かき専門店 癒し処～琥福屋～/耳かき専門店 癒し処～琥福屋～"]
    os.makedirs("./tmp")
    os.makedirs("./tmp/RJ171695/not_convertable")
    os.makedirs("./tmp/not_convertable/rj184314"
                "./tmp/RJ253919/rj253919")
    os.system("python ./src/converter.py -r ./tmp")
    result = [x[0].lstrip("../tmp/") for x in os.walk("./tmp")]
    if required[0] not in result:
        os.system("rm -r ./tmp")
        raise RuntimeError("RJ code (UPPER) should be converted, but it was not.\n" +
                           required[0])
    elif required[1] not in result:
        os.system("rm -r ./tmp")
        raise RuntimeError("rj code (lower) should be converted, but it was not.\n" +
                           required[1])
    elif required[2] not in result:
        os.system("rm -r ./tmp")
        raise RuntimeError("Recursive conversion is not valid.\n" +
                           required[2])
    else:
        os.system("rm -r ./tmp")
        print("Recursion test completed.")
