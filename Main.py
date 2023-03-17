import Bil

looping = True #för att avsluta programmet
volvo_svart = Bil.Bil("Volvo", "Svart", 5)
volvo_vit = Bil.Bil("Volvo", "Vit", 2)
ferrari_red = Bil.Bil("Ferrari", "röd", 4)

billista = [volvo_svart, volvo_vit, ferrari_red]

while looping:
    print("---------------------------------------------------------")
    print("\n-:BilAutomat:-\n")

    i = 0
    #skriver ut lista med bilar
    for bil in billista:
        print(str(i+1)+" : " +bil.fabrikat + " : " +bil.color+ ", antal i lager: " + str(bil.lager) + " st")
        i += i

    Bil_nr = input("\nMata in siffra för vald bil: ")
    Bil_nr_int = int(Bil_nr)

    #print ("bil nr= " + Bil_nr)

    lager_int = billista[Bil_nr_int-1].get_lager()


    if lager_int > 0
    print("\n Här kommer en:" + billista[Bil_nr_int-1].fabrikat)

        #minskar lagret
        nytt_lagersaldo_int = lager_int - 1
        nytt_lager_saldo_string = str(nytt_lagersaldo_int)
        #minskar bil objektets lager 
        billista[Bil_nr_int-1].set_lager(nytt_lagersaldo_int)
    
    print("\nLager saldo: " +str( billista[Bil_nr_int-1].get_lager()))
    
else:
    print("\nSynd, du blir utan bil!\n")

    #Avsluta program
    go = input("\n Vill du avsluta programmet? j/n ")

    if(go == "j"):
        break