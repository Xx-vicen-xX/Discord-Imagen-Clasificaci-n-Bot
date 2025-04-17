Este es un proyecto web simple desarrollado con Flask que permite crear y visualizar entradas de un diario personal de programación. Cuenta con un diseño minimalista en HTML y CSS, y utiliza una base de datos local SQLite. También incluye una función básica de reconocimiento de voz para convertir audio en texto.

Estructura del proyecto
Backend (Python)
main.py: Aplicación principal de Flask.

Rutas:

/ – Muestra todas las entradas del diario

/card/<id> – Muestra una entrada específica

/create – Formulario para crear una nueva entrada

/form_create – Procesa el formulario y guarda en la base de datos

Utiliza SQLAlchemy para gestionar una base de datos SQLite.

speech.py: Captura la voz desde el micrófono y la convierte en texto usando la librería speech_recognition.

Frontend (HTML + CSS)
index.html: Página principal que lista todas las entradas.

card.html: Muestra el detalle de una entrada.

create_card.html: Contiene el formulario para agregar nuevas entradas.

style.css: Estilos del sitio, con tema oscuro y detalles en azul.

Dependencias
Pipfile y Pipfile.lock: Archivos para gestionar las dependencias con pipenv, incluyendo:

Flask

Flask_SQLAlchemy

SpeechRecognition

Cómo ejecutar el proyecto
Cloná el repositorio.

Instalá las dependencias con pipenv:

Cómo ejecutar el proyecto
Cloná el repositorio.

1.Instalá las dependencias con pipenv:
 pipenv install
   
2.Ejecutá la app:
pipenv run python main.py

3.Abrí el navegador y entra en:
http://127.0.0.1:5000/

4.Opcional: Reconocimiento de voz
Podés ejecutar speech.py para probar la función de voz a texto:
python speech.py
