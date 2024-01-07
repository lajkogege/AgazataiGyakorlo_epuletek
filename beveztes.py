def elso_feldata():
    jatekos_neve:str=str(input("Kérem a játékos nevét: "))
    szerepkor:str=str(input("Kérem a szerepkört: "))

    print(f"I/A:")
    print(f"\tJátkos neve: {jatekos_neve}")
    print(f"\tszereokör:{szerepkor}")

    print("I/B:")
    if szerepkor == "varázsló":
        print(f"Üdvözlünk {jatekos_neve}, 2 életed van!")
    elif szerepkor== "harcos":
        print(f"Üdvözlünk {jatekos_neve}, 10 életed van!")
    else:
        print(f"Üdvözlünk {jatekos_neve}, 8 életed van!")

