def run ():
    my_diccionary = {
        "llave1" : 1,
        "llave2" : 2,
        "llave3" : 3,
    }
    # print(my_diccionary["llave1"])
    # print(my_diccionary["llave2"])
    # print(my_diccionary["llave3"])

    poblation_country = {
        "argentina" : 4000000,
        "brasil" : 50000000,
        "colombia" : 35000000,
    }

    #print(poblacion_paises["argentina"])

    # for country in poblation_country.keys():
    #     print(country)

    # for country in poblation_country.values():
    #     print(country)
    for country, poblation in poblation_country.items():
        print(country + " have " + str(poblation) + " population") 




if __name__ == "__main__":
    run()
