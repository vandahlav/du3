# Domácí úkol 3 - vzdálenost ke kontejnerům na tříděný odpad
# Zadání 
Pro zvolenou množínu adresních bodů a množinu kontejnerů na tříděný odpad zjistěte průměrnou a maximální vzdálenost k nejbližšímu veřejnému kontejneru na tříděný odpad. Pro každý adresní bod tedy určete nejbližší veřejný kontejner na tříděný odpad a následně z těchto vzdáleností spočtěte průměr a maximum. Průměr a maximum vypište, pro maximum vypište i adresu, která má nejbližší veřejný kontejner nejdále.

# Zpracování 
Program nejprve načte pomocí definované funkce dva vstupní soubory (geojson). Funkce na jejich otevírání byla spolu s ošetřením případných nekorektních vstupů vytvořena v souboru "funkce.py", odkud je také importována. Následně jsou inicializovány potřebné proměnné, konstanta maximální vzdálenosti (10 km) a transformátor pro převední souřadnic.

Nejprve dojde k vyselektování pouze volně dostupných kontejnerů. Ty jsou uloženy do nového seznamu kontejnery_list. Poté program pomocí for cykl prochází soubor adres, které převádí do požadovaného souřadnicového systému, tedy z WGS-84 do S-JTSK. Rovněž dojde k uložení ulice a čísla popisného dané adresy do nových proměnných. 

Dalším krokem je výpočet nejkratší vzdálenosti z příslušné adresy ke kontejneru. Toho je docíleno pomocí podmínky if a výsledné nejkratší vzdálenosti jsou potom uloženy do nového seznamu. 

Následně dojde k zjištění, ze které adresy je nutné urazit nejdelší minimální vzdálenost k veřejnému kontejneru. Také je ošetřena právě tato minimální délka a to na 10 km. V případě, že bude nejbližší kontejner dále, program vypíše chybu a skončí. 

Na závěr je vypočítán medián vzdáleností (z minimálních vzdáleností uložených v seznamu) a průměrná vzdálenost. Tyto hodnoty jsou poté vypsány spolu s počtem načtených adres a kontejnerů v terminalu. 