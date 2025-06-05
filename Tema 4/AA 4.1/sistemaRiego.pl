:- set_prolog_flag(encoding, utf8).

% Hechos base por parcela

% Humedad del suelo por parcela
humedad_suelo(parcela1, baja).
humedad_suelo(parcela2, media).
humedad_suelo(parcela3, baja).

% Temperatura por parcela (grados Celsius)
temperatura(parcela1, 35).
temperatura(parcela2, 30).
temperatura(parcela3, 33).

% Pronóstico de lluvia por parcela
pronostico_lluvia(parcela1, false).
pronostico_lluvia(parcela2, false).
pronostico_lluvia(parcela3, true).

% Hora general del sistema
hora(20).

% Reglas generales

% Regla: ¿Es una hora adecuada para regar?
hora_adecuada :-
    hora(H),
    (H < 10 ; H > 18).  % Antes de las 10 AM o después de las 6 PM

% Reglas por parcela

% Activación de riego por parcela
activar_riego(Parcela) :-
    humedad_suelo(Parcela, baja),
    pronostico_lluvia(Parcela, false),
    hora_adecuada.

% Estado del riego por parcela
estado_riego(Parcela, 'Activado') :-
    activar_riego(Parcela).

estado_riego(Parcela, 'No activado') :-
    \+ activar_riego(Parcela).

% Alerta por temperatura alta por parcela
alerta_calor(Parcela) :-
    temperatura(Parcela, T),
    T >= 32.

% Recomendaciones por parcela
recomendacion(Parcela) :-
    activar_riego(Parcela),
    alerta_calor(Parcela), !,
    format('Alerta en ~w: Riego activado con temperatura alta. Considere riego nocturno o por goteo.~n', [Parcela]).

recomendacion(Parcela) :-
    format('~w: Sin recomendaciones especiales para el riego.~n', [Parcela]).


% Nueva funcionalidad: mostrar información de la parcela

diagnostico_parcela(Parcela) :-
    humedad_suelo(Parcela, Humedad),
    temperatura(Parcela, Temp),
    pronostico_lluvia(Parcela, Lluvia),
    hora(Hora),
    estado_riego(Parcela, Estado),
    format('--- Información de ~w ---~n', [Parcela]),
    format('Humedad del suelo     : ~w~n', [Humedad]),
    format('Temperatura           : ~w °C~n', [Temp]),
    format('Pronóstico de lluvia  : ~w~n', [Lluvia]),
    format('Hora actual           : ~w hrs~n', [Hora]),
    format('Estado del riego      : ~w~n', [Estado]),
    recomendacion(Parcela).
