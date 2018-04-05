class workwithfile:
    'This is Workwithfile class'

    def __init__(self, namefile):
        self.namefile = namefile

    def readfile(self):
        try:
            with open(self.namefile, "rb") as r:
                byte = r.read(1)
                k = 0
                while byte:
                    try:
                        byte = r.read(1).decode("utf-8")
                    except:
                        continue
                    print(byte, end="")
                    k += 1
        except FileNotFoundError:
            print("[x] File: '" + str(self.namefile) + "' is not defined!")
            raise SystemExit
        else:
            print("\n[+] Number of bytes in the '" + str(self.namefile) + "': " + str(k))

    def writefile(self):
        try:
            with open(self.namefile, 'ab') as file:
                text = input("Write the text: ")
                file.write(text.encode("utf-8"))
        except FileNotFoundError:
            print("[x] File: '" + str(self.namefile) + "' is not defined!")
            raise SystemExit
        else:
            print("[+] File: " + str(self.namefile) + " successfully overwritten!")

def main():
    namef = input("File name: ")
    wwfile = workwithfile(namef)
    wwfile.writefile()
    wwfile.readfile()
if __name__ == "__main__":
    main()