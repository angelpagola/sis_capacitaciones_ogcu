DOCUMENT_TYPE_DNI = '01'
DOCUMENT_TYPE_CE = '03'
DOCUMENT_TYPE_PASAPORTE = '02'
DOCUMENT_TYPE_CEDULA_IDENTIDAD = '04'

DOCUMENTOS_EXISTENTES = [DOCUMENT_TYPE_DNI, DOCUMENT_TYPE_PASAPORTE, DOCUMENT_TYPE_CE, DOCUMENT_TYPE_CEDULA_IDENTIDAD]

DOCUMENT_TYPE_CHOICES = (
    (DOCUMENT_TYPE_DNI, 'DNI'),
    (DOCUMENT_TYPE_CE, 'CE'),
    (DOCUMENT_TYPE_PASAPORTE, 'Pasaporte'),
    (DOCUMENT_TYPE_CEDULA_IDENTIDAD, 'Cédula de identidad')
)

DOCUMENT_TYPE_CHOICES1 = (
    (DOCUMENT_TYPE_DNI, 'DNI'),
    (DOCUMENT_TYPE_CE, 'CE')
)

AREA_CHOICES = (
    (1, 'Urbano'),
    (2, 'Rural'),
)

REGION_GEOGRAFICA_CHOICES = (
    (1, "Costa"),
    (2, "Sierra"),
    (3, "Selva"),
    (4, "Lima Metropolitana"),
)


SEXO_FEMENINO = '2'
SEXO_MASCULINO = '1'

SEXO_CHOICES = (
    (SEXO_FEMENINO, 'Femenino'),
    (SEXO_MASCULINO, 'Masculino')
)

ESTADO_PROYECTO_REGISTRADO = 'registrado'
ESTADO_PROYECTO_VALIDADO = 'validado'
ESTADO_PROYECTO_OBSERVADO = 'observado'
ESTADO_PROYECTO_CANCELADO = 'cancelado'
ESTADO_PROYECTO_CULMINADO = 'culminado'
ESTADO_PROYECTO_POR_VALIDAR = 'por_validar'

ESTADO_PROYECTO_CHOICES = (
    (ESTADO_PROYECTO_REGISTRADO, 'Registrado'),
    (ESTADO_PROYECTO_VALIDADO, 'Validado'),
    (ESTADO_PROYECTO_CANCELADO, 'Cancelado'),
    (ESTADO_PROYECTO_CULMINADO, 'Culminado'),
    (ESTADO_PROYECTO_OBSERVADO, 'Observado'),
    (ESTADO_PROYECTO_POR_VALIDAR, 'Por validar')
)


ESTADO_REVISION_COMISION_CHOICES = (
    (ESTADO_PROYECTO_VALIDADO, 'Validado'),
    (ESTADO_PROYECTO_CANCELADO, 'Cancelado'),
    (ESTADO_PROYECTO_CULMINADO, 'Culminado'),
    (ESTADO_PROYECTO_OBSERVADO, 'Observado'),
    (ESTADO_PROYECTO_POR_VALIDAR, 'Por validar')
)


ESTADO_ASISTENCIA_PRESENTE = 'P'
ESTADO_ASISTENCIA_FALTA = 'F'

ESTADO_ASISTENCIA_CHOICES = (
    (ESTADO_ASISTENCIA_PRESENTE, 'P'),
    (ESTADO_ASISTENCIA_FALTA, 'F'),
)


TIPO_PERSONA_PARTICIPANTE = 'participante'
TIPO_PERSONA_CONSEJO_FACULTAD = 'consejo_facultad'
TIPO_PERSONA_CONSEJO_UNASAM = 'consejo_unasam'

TIPO_PERSONA_CHOICES = (
    (TIPO_PERSONA_PARTICIPANTE, 'Participante'),
    (TIPO_PERSONA_CONSEJO_FACULTAD, 'Miembro del CCEAD Facultad'),
    (TIPO_PERSONA_CONSEJO_UNASAM, 'Miembro del CCEAD UNASAM'),
)

TIPO_FIRMA_DIRECTOR = 'director'
TIPO_FIRMA_PRESIDENTE_CCEAD = 'presidente_ccead'
TIPO_FIRMA_VICERRECTOR_ACADEMICO = 'vicerrector_academico'
TIPO_FIRMA_COORDINADOR = 'coordinador'
TIPO_FIRMA_PONENTE = 'ponente'
TIPO_FIRMA_ORGANIZADOR = 'organizador'

TIPO_FIRMA_CHOICES = (
    (TIPO_FIRMA_DIRECTOR, 'DIRECTOR'),
    (TIPO_FIRMA_VICERRECTOR_ACADEMICO, 'VICERRECTOR ACADÉMICO'),
    (TIPO_FIRMA_PRESIDENTE_CCEAD, 'PRESIDENTE CCEAD'),
    (TIPO_FIRMA_COORDINADOR, 'COORDINADOR'),
    (TIPO_FIRMA_PONENTE, 'PONENTE'),
    (TIPO_FIRMA_ORGANIZADOR, 'ORGANIZADOR'),
)

CARGO_PRESIDENTE = 'presidente'
CARGO_TESORERO = 'miembro1'
CARGO_SECRETARIO = 'miembro2'

CARGO_MIEMBRO_CHOICES = (
    (CARGO_PRESIDENTE, 'Presidente'),
    (CARGO_TESORERO, 'Miembro 1'),
    (CARGO_SECRETARIO, 'Miembro 2'),
)

TIPO_MIEMBRO_FACULTAD = 'consejo_facultad'
TIPO_MIEMBRO_UNASAM = 'consejo_unasam'

TIPO_MIEMBRO_CHOICES = (
    (TIPO_MIEMBRO_FACULTAD, 'Miembro del CCEAD Facultad'),
    (TIPO_MIEMBRO_UNASAM, 'Miembro del CCEAD UNASAM'),
)

EMISION_CERTIFICADO_UNICO = 'certificado_unico'
EMISION_CERTIFICADO_MODULOS = 'certificado_por_modulo'
EMISION_CERTIFICADO_UNICO_Y_MODULOS = 'certificado_unico_y_modulos'

EMISION_CERTIFICADO_CHOICES = (
    (EMISION_CERTIFICADO_UNICO, 'Certificado único'),
    (EMISION_CERTIFICADO_MODULOS, 'Certificados por módulos'),
    (EMISION_CERTIFICADO_UNICO_Y_MODULOS, 'Certificado único y por módulos'),
)

TIPO_CERT_EMITIDO_UNICO = 'certificado_unico'
TIPO_CERT_EMITIDO_MODULO = 'certificado_por_modulo'

TIPO_CERT_EMITIDO_CHOICES = (
    (TIPO_CERT_EMITIDO_UNICO, 'Certificado único'),
    (TIPO_CERT_EMITIDO_MODULO, 'Certificado por módulo'),
)

AMBITO_UNASAM = 'unasam'
AMBITO_FACULTAD = 'facultad'

AMBITO_CHOICES = (
    (AMBITO_UNASAM, 'UNASAM'),
    (AMBITO_FACULTAD, 'Facultad'),
)

CARGO_PROYECTO_PONENTE = 'ponente'
CARGO_PROYECTO_ORGANIZADOR = 'organizador'
CARGO_PROYECTO_RESPONSABLE = 'responsable'

CARGO_PROYECTO_CHOICES = (
    (CARGO_PROYECTO_PONENTE, 'Ponente'),
    (CARGO_PROYECTO_ORGANIZADOR, 'Organizador'),
    (CARGO_PROYECTO_RESPONSABLE, 'Responsable'),
)

CARGO_CERT_EMITIDO_PONENTE = 'ponente'
CARGO_CERT_EMITIDO_ORGANIZADOR = 'organizador'
CARGO_CERT_EMITIDO_RESPONSABLE = 'responsable'
CARGO_CERT_EMITIDO_ASISTENTE = 'asistente'

CARGO_CERT_EMITIDO_CHOICES = (
    (CARGO_CERT_EMITIDO_PONENTE, 'Ponente'),
    (CARGO_CERT_EMITIDO_ORGANIZADOR, 'Organizador'),
    (CARGO_CERT_EMITIDO_RESPONSABLE, 'Responsable'),
    (CARGO_CERT_EMITIDO_ASISTENTE, 'Asistente'),
)

ESTADO_CERT_EMITIDO = 'emitido'
ESTADO_CERT_ANULADO = 'anulado'

ESTADO_CERT_CHOICES = (
    (ESTADO_CERT_EMITIDO, 'Emitido'),
    (ESTADO_CERT_ANULADO, 'Anulado'),
)

GRADO_DOCTORADO = 'doctorado'
GRADO_PHD = 'PhD'
GRADO_MAGISTER = 'magister'
GRADO_LICENCIADO_TITULO = 'licenciado_titulo'
GRADO_BACHILLER = 'bachiller'
GRADO_TECNICO = 'tecnico'
SIN_GRADO = 'sin_grado'

GRADO_CHOICES = (
    (GRADO_BACHILLER, 'BACHILLER'),
    (GRADO_LICENCIADO_TITULO, 'LICENCIADO/TÍTULO'),
    (GRADO_MAGISTER, 'MAGISTER'),
    (GRADO_DOCTORADO, 'DOCTORADO'),
    (GRADO_PHD, 'PhD (philosophie doctor)'),
    (GRADO_TECNICO, 'TÉCNICO'),
    (SIN_GRADO, 'SIN GRADO'),
)

ABREVIATURA_GRADO = (
    ('doctorado', 'Dr.'),
    ('PhD', 'PhD.'),
    ('magister', 'Mag.'),
    ('licenciado_titulo', 'Lic.'),
    ('bachiller', 'Bach.'),
    ('tecnico', 'Tec.'),
    ('sin_grado', ''),
)
