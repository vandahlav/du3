# Domácí úkol 3 - vzdálenost ke kontejnerům na tříděný odpad
# Použití (vstupní data a výstupy)
Jako vstupní data program načítá dva soubory GeJSON. Prvním je soubor adresy.geojson, kde jsou obsaženy adresy se souřadnicemi v souřadnicovém systému WGS-84. Druhým je soubor s názvem kontejnery.geojson. V něm jsou uložena data kontejnerů na tříděný odpad. Souřadnicovým systémem je zde S-JTSK. U vstupních dat pro adresy je v atributu addr:street uloženo jméno ulice a v atributu addr:housenumber číslo popisné. Stejně tak je i u souboru kontejnery uloženo v atributu PRISTUP, zda se jedná o veřejný (volně) kontejner a v atributu STATIONNAME je adresa příslušného kontjeneru.

Výstupem programu je výpis informací o počtu načtených adresních bodů a kontejnerů. Dále dojde k vypsání průměrné nejkratší vzdálenosti k veřejnému kontejneru na tříděný odpad, adresy, která to má k nejbližšímu kontejneru nejdále (včetně hodnoty dané vzdálenosti) a nakonec mediánu vzdáleností. 

# Zpracování 
Program nejprve načte pomocí definované funkce dva vstupní soubory (geojson). Funkce na jejich otevírání byla spolu s ošetřením případných nekorektních vstupů vytvořena v souboru "funkce.py", odkud je také importována. Následně jsou inicializovány potřebné proměnné, konstanta maximální vzdálenosti (10 km) a transformátor pro převední souřadnic.

Nejprve dojde k vyselektování pouze volně dostupných kontejnerů. Ty jsou uloženy do nového seznamu kontejnery_list. Poté program pomocí for cykl prochází soubor adres, které převádí do požadovaného souřadnicového systému, tedy z WGS-84 do S-JTSK. Rovněž dojde k uložení ulice a čísla popisného dané adresy do nových proměnných. 

Dalším krokem je výpočet nejkratší vzdálenosti z příslušné adresy ke kontejneru. Toho je docíleno pomocí podmínky if a výsledné nejkratší vzdálenosti jsou potom uloženy do nového seznamu. 

Následně dojde k zjištění, ze které adresy je nutné urazit nejdelší minimální vzdálenost k veřejnému kontejneru. Také je ošetřena právě tato minimální délka a to na 10 km. V případě, že bude nejbližší kontejner dále, program vypíše chybu a skončí. 

Na závěr je vypočítán medián vzdáleností (z minimálních vzdáleností uložených v seznamu) a průměrná vzdálenost. Tyto hodnoty jsou poté vypsány spolu s počtem načtených adres a kontejnerů v terminalu. 