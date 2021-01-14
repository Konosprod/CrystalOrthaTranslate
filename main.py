import argparse
import io
import csv

def parseFile(fileIn):
    file = open(fileIn, "rb")

    sig = file.read(0x05)
    length = file.read(0x02)

    data = io.BytesIO(file.read(int.from_bytes(length, byteorder="big")))

    data.seek(0x06)
    stringNumber = int.from_bytes(data.read(0x02), byteorder="big")

    print(fileIn)
    print("Strings : {0:x}".format(stringNumber)) 

    i = 0
    strings = []

    while i < stringNumber:
        size = int.from_bytes(data.read(0x02), byteorder="big")
        string = data.read(size)
        strings.append([string.decode("utf8").replace("\n", "").replace("\t", "\\t"), ""])
        i += 1

    fileOut = open(fileIn+".csv", "w", newline="")

    writer = csv.writer(fileOut)
    writer.writerows(strings)

    fileOut.close()
    file.close()
    print("-----------------------------")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("file")

    args = parser.parse_args()

    parseFile(args.file)