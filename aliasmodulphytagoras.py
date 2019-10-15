import modulphytagoras as mphy

def main():
    a = 5
    b = 12
    sisimiringC = mphy.sisimiringC(a,b)
    print("PHYTAGORAS")
    print("Sisi Miring C: ",sisimiringC)

    c = 13
    sisitegakA = mphy.sisitegakA(b,c)
    print("Sisi Tegak A: ",sisitegakA)

    sisimendatarB = mphy.sisimendatarB(a,c)
    print("Sisi Mendatar B: ",sisimendatarB)

if __name__ == "__main__":
    main()
