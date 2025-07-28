'''1) diferencia de Porcentaje entre este curso actual y
    a)El mas RAPIDO de OTROS cursos
    b)El mas LENTO de OTROS cursos
    c)El PROMEDIO de los cursos
    
   2) Porcentaje de material inservible que se reduce en:
      a) El promedio d elos cursos
      b) El curso actual
      
   3)  Ver 10 horas de este curso a cuantas horas de otros cursos equivale?
'''

'''
------|----|----|--|----|--------|----8----9----10
     1,5  2,5  3,5 4    5        7
        
    otros= 5 hs crudo = 4 hs cn edicion
    sete = 3,5 hs crudo = 1,5 hs cn edicion
    
'''
curso = 1.5;
minimo = 2.5;
maximo = 7;
elPromedio = 4;
crudoOtros = 5;
crudoCurso = 3.5;

#1) Calcular y mostrar diferencias y promedios
diferenciaMinimo = minimo-curso;
promedioMenor = 100-((curso * 100) / minimo);

print(f"La diferrencia Horaria entre el curso y el minimo de otro es: {diferenciaMinimo} Horas, lo que seria un promedio de: {promedioMenor} % mas rapido");

diferenciaMAximo = maximo-curso;
promedioMayor = 100-((curso * 100) / maximo);
print(f"La diferrencia Horaria entre el curso y el Maximo de otro es: {diferenciaMAximo} Horas, lo que seria un promedio de: {promedioMayor} % mas rapido");

diferenciaPromedio = elPromedio-curso;
promediador = 100-((curso * 100) / elPromedio);
print(f"La diferrencia Horaria entre el curso y el Promedio de otro es: {diferenciaPromedio} Horas, lo que seria un promedio de: {promediador} % mas rapido");


#2) Calcular y mostrar promedio del crudo

promedioCrudo = 100 - elPromedio * 1000 // crudoOtros/10;
print("\n" +f"Se reduce un promedio de: {promedioCrudo} % el video en promedio de otros cursos");

promedioCrudo = 100 - curso * 1000 // crudoCurso/10;
print(f"Se reduce un promedio de: {promedioCrudo} % el video de este curso" + "\n");

#3) 10hs de curso

curso = 10
#26.6
otros = curso + (curso * (promediador / 100));
print(f"Ver 10 horas de este curso equivale a: {otros} Horas de otros cursos (en promedio)" + "\n");

