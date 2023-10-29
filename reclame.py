from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
   korting_bedrag = prijs * korting
   nieuwe_prijs = prijs - korting_bedrag
   return f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs: 2f} euro voor {nieuwe_prijs: 2f} euro."
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten,btw_percentage):
   totaal_inkomsten = sum(inkomsten)
   btw = btw_percentage / 100.0
   btw_bedrag = totaal_inkomsten * btw
   totaal_met_btw = totaal_inkomsten + btw_bedrag
   return f"Het totaal van alle inkomsten van deze week is {totaal_met_btw:.2f} euro, waarover {btw_bedrag:.2f} euro btw betaald dient te worden"
inkomsten = [220, 430, 125, 160, 205, 90, 345]
btw_percentage = 9 
resultaat = inkomsten_totaal(inkomsten, btw_percentage)
print(resultaat)

def laag_en_hoog(mijn_lijst):
   laagste = min(mijn_lijst)
   hoogste = max(mijn_lijst)
   return[laagste, hoogste]
mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
resultaat = laag_en_hoog(mijn_lijst)
print(resultaat)

def gemiddelde(mijn_lijst):
    som = sum(mijn_lijst)
    gemiddelde = som / 7
    gemiddelde_str = "De gemiddelde inkomsten deze week zijn {:.2f} euro.".format(gemiddelde)
    return gemiddelde_str

inkomsten_per_dag = [220, 430, 125, 160, 205, 90, 345]
gemiddelde_inkomsten = gemiddelde(inkomsten_per_dag)
print(gemiddelde_inkomsten)

# In het bestand 'reclame.py'

def hoog_en_laag(invoer_lijst):
    hoogste_waarde = max(invoer_lijst)
    laagste_waarde = min(invoer_lijst)
    return [hoogste_waarde, laagste_waarde]

def meervoudig(invoer_lijst):
    if len(invoer_lijst) < 5 or len(invoer_lijst) > 10:
        raise ValueError()
    
    resultaat = laag_en_hoog(invoer_lijst)
    return resultaat

invoer_lijst = [10, 5, 3, 2, 1, 2, 9]
laagste_en_hoogste = meervoudig(invoer_lijst)

print("Laagste waarde:", laagste_en_hoogste[0])
print("Hoogste waarde:", laagste_en_hoogste[1])

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer
invoer_lijst_2 = [10, 5, 3, 2, 1, 2, 9]
resultaat = combinatie(invoer_lijst_2)
print(resultaat)





   



   

    