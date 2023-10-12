prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}
aanbieding = prijzen["vanille"] * 0.8
reclame_tekst = f"Vandaag in de aanbieding: vanille-ijs, 1 liter - slechts €  {aanbieding}"
reclame_tekst2 = reclame_tekst.upper()
reclame_tekst3 = reclame_tekst2.split()
print(reclame_tekst3)
for el in reclame_tekst3:
    el = el.lower()
    if len(el) >= 5:
        print(el.upper())
    else:
        print(el)


    
   
            
   



  

    



