option_items = ["1","2","3","4","5","0"]

def paragraf():
    print("_" * 20)

def show():
    print('Options')
    print('1)m to cm')
    print('2)m to km')
    print('3)m to ft')
    print('4)kg to pound')
    print('5)°C to °F')
    print('0)Exit')

def m_cm(m):
    cm = 100
    print(f"{m} = {m * cm} cm")

def m_km(m):
    km = 0.001
    print(f"{m} = {m * km} km")

def m_ft(m):
    ft = 3.28084
    print(f"{m} = {round(m * ft, 1)} ft")

def kg_lb(kg):
    lb = 2.20462
    print(f"{kg} = {round(kg * lb, 1)} lb")

def c_f():
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9 / 5) + 32
    print(f"{c}°C = {f}°F")


def leave():
    print('goodbye')

while True:
    show()

    paragraf()

    option = str(input("Enter chose option: "))
    paragraf()

    if option not in option_items:
        print("Error: invalid option")
        paragraf()
        continue

    match option:
        case "1":
            m = float(input("Enter the m number to cm : "))
            m_cm(m)
            paragraf()
        case "2":
            m = float(input("Enter the m number to km : "))
            m_km(m)
            paragraf()
        case "3":
            m = float(input("Enter the m number to ft : "))
            m_ft(m)
            paragraf()
        case "4":
            kg = float(input("Enter the kg number to lb : "))
            kg_lb(kg)
            paragraf()
        case "5":
            c_f()
            paragraf()
        case "0":
            leave()
            paragraf()
            break

