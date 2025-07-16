def su_hesabı(kilo):
    e_hesap = kilo*0.04
    k_hesap = kilo*0.03
    while True:
        cinsiyet = input("Lütfen cinsiyetinizi giriniz (Kadın/Erkek): ").lower()
        

        if cinsiyet=="kadın":
                print("*"*25)
                print("Cinsiyetiniz : ",cinsiyet)
                print(e_hesap,"Litre su içmelisinizz")
                print("*"*25)
                break

        elif cinsiyet=="erkek":
                print("*"*25)
                print("Cinsiyetiniz : ",cinsiyet)
                print(k_hesap,"Litre su içmelisiniz.")
                print("*"*25)
                break

        elif not cinsiyet:
                print("Lütfen cinsiyetinizi belirtiniz.")
                

        else:
                print("Yanlış cinsiyet girdiniz")
                
kilo_al = int(input("Lütfen Kilonuzu Giriniz : "))
su_hesabı(kilo_al)
