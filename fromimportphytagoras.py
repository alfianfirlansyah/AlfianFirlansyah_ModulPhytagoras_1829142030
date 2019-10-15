from modulphytagoras import sisimiringC

def main():
    a = float(input("Masukkan a= "))
    b = float(input("Masukkan b= "))

    sisimiring = sisimiringC(a,b)

    print("PHYTAGORAS")
    print("Sisi Tegak A: ",a)
    print("Sisi Mendatar: ", b)
    print("Sisi Miring: ", sisimiring)

if __name__ == "__main__":
    main()
