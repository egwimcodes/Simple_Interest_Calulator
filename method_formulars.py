
def simple_interest():
    p = int(input("Principal: "))
    r = float(input("RATE: "))
    t = int(input("TIME: "))
    si = (p * (r / 100) * t)
    print(round(si))


def principle():
    si = int(input("SIMPLE INTEREST: "))
    r = float(input("RATE: "))
    t = int(input("TIME: "))
    cal_si = ((r / 100) * t)
    p = (si / cal_si)
    print(p)


def rate():
    p = int(input("Principal: "))
    si = int(input("SIMPLE INTEREST: "))
    t = int(input("TIME: "))
    cal_si = (p * t)
    r = (si / cal_si) * 100
    print(r)


def time():
    p = int(input("Principal: "))
    si = int(input("SIMPLE INTEREST: "))
    r = float(input("RATE: "))
    cal_si = (p * (r / 100))  # principle * rate
    t = (si / cal_si)
    print(round(t))