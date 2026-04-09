# 🐾 Centro de Adopción de Perritos

Este proyecto es una plataforma web integral diseñada para digitalizar y facilitar el flujo de adopción de 
mascotas. El sistema permite gestionar desde el registro de nuevos caninos hasta la confirmación final de su 
adopción, utilizando un entorno seguro y visualmente amigable.

## Capturas del Proceso y Funcionamiento

### 1. Catálogo
Vista principal donde el administrador o usuario puede visualizar a los perritos disponibles. Se aprecia el uso 
de las tonalidades lilas y la disposición organizada de los elementos.
> ![Pantalla Principal](catalogo.png)

### 2. Registro y Formulario de Adopción
Esta es la vista del formulario para la agregar el nombre de la persona que quiere adoptar, el lugar a donde vive y el ID luego de a ver completado dichos campos ya se puede realizar la adopción.
> ![Formulario de Registro](formulario.png)

### 3. Historial de adopción
Y por ultimo se muestra la vista al historial de adopciones en donde se puede visualizar que perritos fueron adoptados por quien fue adoptado,la hora y la fecha de dicha adopción.
> ![Confirmación Final](historial.png)

## Stack Tecnológico
* Python 3.10+: Elegido por su sintaxis limpia y su excelente manejo de lógica de servidor.
  
* Flask: Se utilizó este micro-framework debido a su flexibilidad. Permite gestionar rutas dinámicas y renderizar plantillas de forma ligera sin la sobrecarga de frameworks más pesados.

* MySQL Server: Se optó por este motor relacional por su fiabilidad en el manejo de registros vinculados.

* HTML & CSS: HTML es el lenguaje que uso para crear las casillas de texto y los botones de mi sistema; es la base donde luego aplico mis colores pasteles con CSS y la lógica con Python.
  
* Visual Studio Code: Entorno de desarrollo principal, aprovechando sus extensiones de Python y terminal integrada.
  
* Linux (Ubuntu): Sistema operativo base, utilizado por su estabilidad y herramientas nativas para la gestión de servidores web y procesos de bases de datos.

## Instalación y Configuración Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/centro-adopcion.git](https://github.com/tu-usuario/centro-adopcion.git)
   cd centro-adopcion
