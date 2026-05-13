def yil_kabisa_yilmi(yil):
    if yil % 4 == 0:
        if yil % 100 == 0:
            if yil % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

yil = int(input("Yilni kiriting: "))
if yil_kabisa_yilmi(yil):
    print("Yil kabisa yil ekan.")
else:
    print("Yil kabisa yil emas.")
