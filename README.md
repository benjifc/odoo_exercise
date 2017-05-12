# GESTIÓN DE INSTALACIONES DEPORTIVAS

Se desea crear un módulo para la gestión de instalaciones deportivas. El módulo permitirá al usuario final 
realizar la gestión completa de las instalaciones, así como las reservas a las mismas y los usuarios que 
pueden reservar pistas.
FLUJOS DEL SISTEMA
Nueva Reserva: 
Este flujo nos permitirá crear una solicitud de reserva a una pista deportiva en una fecha 
determinada. Para ello, tendremos un elemento de menú el cual nos abrirá un wizard 
sport.rent.wizard
 que 
tendremos que rellenar correctamente indicando Usuario que reserva la pista, fecha de inicio, duración y 
tipo de pista, en base a estos datos introducidos el sistema nos permitirá escoger solo aquellas pistas que 
no cuentan con otro alquiler creado para tal fecha y que puedan solaparse los horarios. Una vez todo 
correcto, el wizard finalizará con el alquiler (
sport.rent
) creado.
Generar cupones de usuario: 
Para dar de alta nuevos usuarios en el sistema, se usará un sistema de 
cupones. Para ello, necesitaremos un elemento de menú el cual abrirá el wizard 
user.coupon.generation.wizard
 este wizard contará solamente con un campo fecha de validez, que indicará 
la fecha en la que caducará el cupón. El wizard finalizará con el cupón (
user.coupon
) creado, puede usar 
librerías python para generar cadenas aleatorias.
Alta de nuevos usuarios: 
Para los usuarios del sistema se heredará el modelo 
res.partner 
el cual contará con
un campo que filtrará aquellos usuarios que puedan reservar pistas. La única forma que habrá de dar de alta
nuevos usuarios será a través del wizard  
new.user.wizard 
 el cual se abrirá a través de un elemento de menú
y que recibirá la información básica del usuario (nombre, telefono, email) además del cupón de registro. El 
wizard finalizará con el nuevo usuario creado. (El cupón debe de ser un cupón válido que este generado en 
el sistema, que no haya caducado aún, y que este sin usar.)
ENTIDADES (MODELOS) DEL SISTEMA
Instalación deportiva (
sport.installation
)
Nombre (Char)
Ubicación (Char)
Tipo de Pista (Many2one con el modelo ‘
installation.type’
)
Alquileres (One2many con el modelo ‘
sport.rent
’
)
Tipo de pista (
installation.type
)
Nombre (Char)
Instalaciones (One2many con el modelo 
‘
sport.installation’
)
Alquiler (
sport.rent
)
Fecha de inicio del alquiler (Datetime)
Fecha de fin del alquiler (Datetime)
Instalación (Many2one con el modelo 
‘
sport.installation’
)
Persona que reserva (Many2one con el modelo 
‘
res.partner’)
Usuario (
herencia de res.partner
)
Usuario de las instalaciones deportivas (Boolean)
Alquileres efectuados (One2many con el modelo 
sport.rent
)
Codigos Alta usuario (
user.coupon
)
Código (Char, tamaño 12)
Código usado (Boolean)
Fecha de validez (Date)
Wizards (Modelos transitorios)
Solicitud de reserva (
sport.rent.wizard
)
Fecha de inicio (Datetime)
Duración - Minutos (Integer)
Usuario que reserva (Many2one con el modelo ‘
res.partner
’
)
Tipo de pista (Many2one con el modelo 
‘
installation.type’
)
Pistas disponibles (Many2one con el modelo 
‘
sport.installation’)
Generar codigos alta (
user.coupon.generation.wizard
)
Fecha de validez (Date)
Alta de nuevos usuarios (
new.user.wizard
)
Código de Alta (Char, tamaño 12)
Nombre de usuario (Char)
Teléfono de contacto (Char)
Email de contacto (Char)
ENUNCIADO
Se pide el desarrollo de un módulo que cumpla los flujos expuestos anteriormente. Asegurate de cumplir 
con la nomenclatura expuesta anteriormente, y que los campos sean del tipo definido. Cada modelo deberá
llevar al menos una vista tree y form, valorándose el desarrollo de otros tipos de vista como calendar y 
graph.
Se valorará también cualquier elemento que de valor visual o de interacción con el usuario, además de la 
consistencia de los datos entre sí.
