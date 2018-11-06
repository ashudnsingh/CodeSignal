def higherVersion(ver1, ver2):
    return list(map(int,ver1.split("."))) > list(map(int,ver2.split(".")))
