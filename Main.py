import Bil

looping = True #för att avsluta programmet
volvo_svart = bil.Bil("Volvo", "Svart", 5)
volvo_vit = bil.Bil("Volvo", "Vit", 2)
ferrari_red = bil.Bil ("Ferrari", "röd" 4)

while looping:
    print("---------------------------------------------------------")
    print("\n-:BilAutomat:-\n")

    #Avsluta program
    go = input("\n Vill du avsluta programmet? j/n ")

    if(go == "j"):
        break