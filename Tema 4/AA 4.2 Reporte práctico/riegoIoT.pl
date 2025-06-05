% Estado de sensores
humedad_suelo(baja).
temperatura(35).
hora(20).
pronostico_lluvia(false).

% Regla: ¿Es una hora adecuada para regar?
hora_adecuada :- hora(H), (H < 10 ; H > 18).

% Regla principal: ¿Cuándo se debe activar el sistema de riego?
activar_riego :- 
    humedad_suelo(baja), 
    pronostico_lluvia(false), 
    hora_adecuada.

% Diagnóstico del sistema
estado_riego('Activado') :- activar_riego.
estado_riego('No activado') :- \+ activar_riego.

% Regla para alerta de temperatura extrema
alerta_calor :- 
    temperatura(T), 
    T >= 32.

% Mensaje de alerta si se activa el riego con calor extremo
recomendacion :-
    activar_riego,
    alerta_calor, !,
    writeln('Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo.').

recomendacion :-
    writeln('Sin recomendaciones especiales para el riego.').