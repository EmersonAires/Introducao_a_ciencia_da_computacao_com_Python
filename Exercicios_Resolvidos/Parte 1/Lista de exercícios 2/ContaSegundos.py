Segundos = int(input("Por favor, entre com o número de segundos que deseja converter"))
Dias = Segundos // 86400
RestoSegundos = Segundos % 86400
Horas = RestoSegundos // 3600
RestoSegundos = RestoSegundos % 3600
Minutos = RestoSegundos // 60
RestoSegundos = RestoSegundos % 60
Segundos = RestoSegundos
print (Dias,"dias,",Horas,"horas,",Minutos,"minutos e",Segundos,"segundos.")