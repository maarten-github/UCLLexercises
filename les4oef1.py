"""
oefening voor les 4 deel 1
de eerste functie vraagt het nummer van een maand en geeft het aantal dagen
de tweede functie geeft vanaf de naam van een maand, het aantal dagen sinds nieuwjaar tot het einde van die maand
de derde functie geeft vanaf de naam van de maand, het aantal dagen vanaf het einde van die maand tot het einde van het jaar
de vierde functie geeft vanaf de nummers van 2 maanden, het aantal dagen tussen het einde van de eerste en het einde van de tweede maand
"""

maanden=["januari","februari","maart","april","mei","juni","juli","augustus","september","oktober","november","december"]
y=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_days_of_the_month(m):
    if 0<m<len(y):
        d=y[m-1]
        print ("het aantal dagen in "+(maanden[m-1])+" is " + str(d))
    else:
        print ("het aantal dagen in uw maand is")
        print (0)
get_days_of_the_month(7)



def get_days_of_the_beginning_year(m):
    if m in maanden:
        p = int(maanden.index(m))
        s=sum(y[0:p+1])
        print ("het aantal dagen sinds nieuwjaar tot en met het einde van "+(m)+" is " + str(s) )
    else:
       print (" u heeft geen maand ingegeven")
get_days_of_the_beginning_year("december")

def days_untill_start_year(m):
    if m in maanden:
        p = int(maanden.index(m))
        s=sum(y[p:p+12])
        print ("het aantal dagen vanaf begin " +(m)+ " tot het einde van het jaar is "+ str(s))
    else:
        print ("u heeft geen maand ingegeven")
days_untill_start_year("auto")


def days_between_months(m,n):
    if m<n and 0<m<=len(y)+1 and 0<n<=len(y)+1:
        x=sum(y[m-1:n-1])
        print ("het aantal dagen na " +(maanden[m-1]) + ", en tot en met het einde van " +(maanden[n-1]) +" is " + str(x))
    else:
        print ("o")
days_between_months(2,3)


