import argparse
import io
import csv



def parseFile(fileIn):
    file = open(fileIn, "rb")

    sig = file.read(0x05)
    length = file.read(0x02)

    file.seek(0x06, io.SEEK_CUR)
    stringNumber = int.from_bytes(file.read(0x02), byteorder="big")

    print(fileIn)
    print("Strings : {0:x}".format(stringNumber)) 

    i = 0
    strings = []

    while i < stringNumber:
        size = int.from_bytes(file.read(0x02), byteorder="big")
        string = file.read(size)
        strings.append([string.decode("utf8").replace("\n", "").replace("\t", "\\t"), ""])
        i += 1

    strings.append(["TEXT TO TRANSLATE IS ABOVE THIS LINE", ""])
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