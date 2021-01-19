def funcao_raizes (a, b, c):

    #Discriminante

    Delta = (b**2) - 4*a*c 

    import math

    if Delta > 0: 
            x1 = (-b + math.sqrt(Delta))/(2*a)
            x2 = (-b - math.sqrt(Delta))/(2*a)
            if x1 >= x2:
                print("as raízes da equação são",x1,"e",x2)
            else:
                print("as raízes da equação são",x2,"e",x1)
    elif Delta == 0: 
            x1 = (-b)/(2*a)
            print("a raiz desta equação é",x1)
        
    else:
            print("esta equação não possui raízes reais")