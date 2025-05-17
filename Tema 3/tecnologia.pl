:- dynamic actividad_inusual/1.
:- dynamic acceso_fallido/1.
:- dynamic instalacion_no_autorizada/1.
:- dynamic tiene_antivirus/1.
:- dynamic correo_fraudulento/1.
:- dynamic encriptacion_archivos/0.
:- dynamic conexiones_no_autorizadas/0.
:- dynamic alertas_ids/0.
:- dynamic backup_disponible/1.

% Reglas de inferencia
sistema_comprometido(Sistema) :-
    actividad_inusual(Sistema),
    acceso_fallido(Sistema).

sistema_comprometido(_) :-
    conexiones_no_autorizadas,
    alertas_ids.

nivel_amenaza(Sistema, bajo) :-
    tiene_antivirus(verdadero),
    backup_disponible(verdadero),
    \+ sistema_comprometido(Sistema).

nivel_amenaza(Sistema, medio) :-
    tiene_antivirus(verdadero),
    backup_disponible(falso),
    sistema_comprometido(Sistema).

nivel_amenaza(Sistema, alto) :-
    sistema_comprometido(Sistema),
    tiene_antivirus(falso).

nivel_amenaza(Sistema, critico) :-
    tipo_ataque(Sistema, ransomware),
    backup_disponible(falso).

tipo_ataque(Sistema, malware) :-
    instalacion_no_autorizada(Sistema).

tipo_ataque(Sistema, phishing) :-
    correo_fraudulento(Sistema).

tipo_ataque(_, ransomware) :-
    encriptacion_archivos.

% Recomendaciones adicionales
recomendacion(Sistema, 'Instala un software antivirus y realiza un análisis completo.') :-
    tipo_ataque(Sistema, malware).

recomendacion(Sistema, 'Cambia tus contraseñas de inmediato y habilita la autenticación en dos pasos.') :-
    tipo_ataque(Sistema, phishing).

recomendacion(_, 'Desconecta el sistema de la red y recupera los archivos desde la copia de seguridad.') :-
    tipo_ataque(_, ransomware).

% Interacción con el usuario con preguntas claras
preguntar(Sistema) :-
    hacer_pregunta('¿Tu computadora se comporta de forma extraña o hace cosas que no has ordenado? (si/no)', Resp1),
    (Resp1 == si -> assert(actividad_inusual(Sistema)); true),

    hacer_pregunta('¿Has notado que alguien intenta acceder muchas veces sin éxito? (si/no)', Resp2),
    (Resp2 == si -> assert(acceso_fallido(Sistema)); true),

    hacer_pregunta('¿Se instaló algún programa que tú no autorizaste? (si/no)', Resp3),
    (Resp3 == si -> assert(instalacion_no_autorizada(Sistema)); true),

    hacer_pregunta('¿Tu computadora tiene un antivirus activo? (si/no)', Resp4),
    (Resp4 == no -> assert(tiene_antivirus(falso)); assert(tiene_antivirus(verdadero))),

    hacer_pregunta('¿Has recibido correos sospechosos que te piden hacer clic en enlaces o dar información? (si/no)', Resp5),
    (Resp5 == si -> assert(correo_fraudulento(Sistema)); true),

    hacer_pregunta('¿Tus archivos aparecen bloqueados o con nombres extraños y no puedes abrirlos? (si/no)', Resp6),
    (Resp6 == si -> assert(encriptacion_archivos); true),

    hacer_pregunta('¿Tu equipo se conecta a sitios o direcciones que tú no reconoces? (si/no)', Resp7),
    (Resp7 == si -> assert(conexiones_no_autorizadas); true),

    hacer_pregunta('¿Tu antivirus o sistema lanza alertas frecuentes de seguridad? (si/no)', Resp8),
    (Resp8 == si -> assert(alertas_ids); true),

    hacer_pregunta('¿Tienes una copia de seguridad reciente de tus archivos importantes? (si/no)', Resp9),
    (Resp9 == si -> assert(backup_disponible(verdadero)); assert(backup_disponible(falso))),

    nl, diagnosticar(Sistema).

hacer_pregunta(Pregunta, Respuesta) :-
    write(Pregunta), nl,
    read(Resp),
    (Resp == si; Resp == no),
    Respuesta = Resp.

diagnosticar(Sistema) :-
    (sistema_comprometido(Sistema) ->
        write('El sistema parece estar comprometido.'), nl;
        write('No se detectaron signos de intrusión grave.'), nl),
    (nivel_amenaza(Sistema, Nivel) ->
        format('Nivel de amenaza: ~w~n', [Nivel]),
        recomendacion(Sistema, Recomendacion),
        format('Recomendación: ~w~n', [Recomendacion]);
        true),
    (tipo_ataque(Sistema, Tipo) ->
        format('Tipo de ataque detectado: ~w~n', [Tipo]);
        true).