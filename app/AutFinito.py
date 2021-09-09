from flask import flash
import re

#########################################################################

def automato(seq):
    estado_final = {"3"}
    aceitavel={"a","b"}
    estado ="1"
    dic_trans={("1","a"):"2",("1","b"):"4",
            ("2","a"):"2",("2","b"):"3",
            ("3","a"):"3",("3","b"):"3",
            ("4","a"):"2",("4","b"):"5",
            ("5","a"):"3",("5","b"):"5"}

    #while True :
    #seq=input("insira uma sequencia: ")

    for i in seq:
        if (i not in aceitavel):
            return(flash("ERRO, insira apenas a's e b's"))
        estado=dic_trans[(estado,i)]
    if(estado not in estado_final):
        return(flash("Sequencia não aceite"))
    else:
        return(flash("Sequencia aceite!"))

#########################################################################

def automata(sequen):
    #estado_final = {"3"}
    aceita={"1","0"}
    #estado ="1"

    stack = []
    stack.append("$")

    #le 0 e apaga
    #0011
    #011
    #11
    
    for i in sequen:
        if i not in aceita:
            return (flash("ERRO, insira apenas 1's e 0's"))
        if i == '0':
            stack.append('x')
            sequen = sequen[1:]
            #print (sequencia)
        if i == '1':
            break
    #so le 1
    #se 0 break
    for i in sequen:
        if i not in aceita:
            return (flash("ERRO, insira apenas 1's e 0's"))
        if i == '1':
            if stack.pop() == '$':
               return (flash('Sequencia não aceite'))
                
        if i == '0':
            return (flash('Sequencia não aceite'))
        #print(stack)
    
    if stack.pop() == '$':
        return( flash('Sequencia aceite!'))
    else: return(flash('Sequencia não aceite'))

#########################################################################

def password(codigo):
    
    regex = r"^(?=(.*[0-9]))((?=.*[A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z]))^.{8,}$"

    #codigo = input("Insira uma palavra com cinco caracteres, começada por a e acabada com s:")
    if re.match(regex,codigo):
        #return flash("Aceite")
        return "1"
    else :
        #return flash("Password should have 1 lowercase letter, 1 uppercase letter, 1 number, and be at least 8 characters long ")
        return "0"
def mail(codigo):
    
    regex = r"^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6})*$"

    #codigo = input("Insira uma palavra com cinco caracteres, começada por a e acabada com s:")
    if re.match(regex,codigo):
        #return flash("Aceite")
        return "1"
    else :
        #return flash(" ERROR, EMAIL REJEITADO")
        return "0"