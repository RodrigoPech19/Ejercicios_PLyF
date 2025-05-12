%Hechos observados
actividad_inusual(alicia, pc1).
acceso_fallido(alicia, repetido).
instalacion_no_autorizada(spyware, pc1).
correo_fraudulento(alicia, pc1).
encriptacion_archivos(pc1).
conexiones_externas_no_autorizadas(pc1).
alertas_ids(pc1).
tiene_antivirus(pc1, falso).
backup_disponible(pc1, falso).

%Reglas de inferencia

%Sistema comprometido por actividad inusual y accesos fallidos
sistema_comprometido(S) :- actividad_inusual(_, S), acceso_fallido(_, repetido).

%Sistema comprometido por conexiones no autorizadas y alertas IDS
sistema_comprometido(S) :- conexiones_externas_no_autorizadas(S), alertas_ids(S).

%Nivel de amenaza alto si sistema comprometido y no tiene antivirus
nivel_amenaza(S, alto) :- sistema_comprometido(S), tiene_antivirus(S, falso).

%Tipo de ataque: Malware por instalación no autorizada
tipo_ataque(S, malware) :- instalacion_no_autorizada(_, S).

%Tipo de ataque: Phishing por correo fraudulento
tipo_ataque(S, phishing) :- correo_fraudulento(_, S).

%Tipo de ataque: Ransomware por encriptación de archivos
tipo_ataque(S, ransomware) :- encriptacion_archivos(S).

%Nivel de amenaza crítico si ransomware y sin backup
nivel_amenaza(S, critico) :- tipo_ataque(S, ransomware), backup_disponible(S, falso).

%Acciones recomendadas según el tipo de ataque
accion_recomendada(S, analizar_sistema) :- tipo_ataque(S, malware).
accion_recomendada(S, cambiar_credenciales) :- tipo_ataque(S, phishing).
accion_recomendada(S, aislar_sistema) :- tipo_ataque(S, ransomware).
