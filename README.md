🛒 Prueba N°4 – Tienda Online + API REST

Asignatura: Programación Back End
Carrera: Ingeniería en Programación e Informática
Institución: INACAP
Estudiante: Gabriel Paredes Medina

📌 Descripción General

Este proyecto corresponde a la Prueba N°4 de la asignatura Programación Back End, la cual consiste en extender una tienda online desarrollada previamente (Prueba N°3), incorporando una API REST, un reporte dinámico protegido, y la preparación del sistema para producción y despliegue en la nube.

El sistema permite la gestión completa de productos, insumos y pedidos, combinando vistas tradicionales de Django con endpoints REST, cumpliendo con todos los requisitos indicados en la rúbrica de evaluación.

🧱 Stack Tecnológico

Backend: Django 5.2.6

API REST: Django REST Framework (DRF)

Base de Datos:

PostgreSQL (producción – Render)

SQLite (fallback / desarrollo)

Archivos Estáticos: WhiteNoise

Imágenes / Media: Cloudinary

Deploy: Render

🌐 Deploy en Producción

URL del sistema:
👉 https://prueba-gabriel.onrender.com/

El sistema se encuentra desplegado en producción, con configuración adecuada para entorno real (DEBUG=False, manejo de estáticos y media).

🔐 Usuario de Prueba (Administración)
Rol	Usuario	Contraseña
Administrador	admin	admin

Acceso al panel administrativo:

/admin/

🛍️ Funcionalidades de la Tienda
Funcionalidades para el Cliente

Visualización de catálogo de productos

Filtro por nombre y categoría

Vista de detalle de producto

Creación de pedidos desde la web

Adjuntar imagen de referencia en pedidos

Seguimiento de pedidos mediante token único

Ruta de seguimiento:

/seguimiento/<token>/

📊 Reporte Dinámico (Vista Protegida)

Ruta:

/reporte/


Acceso: solo usuarios autenticados con rol staff / admin

Características del reporte:

Consulta real a la base de datos usando el ORM de Django

Tabla con pedidos agrupados por estado

Gráfico dinámico generado con Chart.js

Información actualizada en tiempo real según los datos existentes

Este reporte cumple con el requisito de vista protegida + datos reales + visualización gráfica.

🔌 API REST – Django REST Framework
📦 API 1 – CRUD Completo de Insumos

Endpoint base:

/api/insumos/

Método	Endpoint	Descripción
GET	/api/insumos/	Listar insumos
POST	/api/insumos/	Crear insumo
GET	/api/insumos/{id}/	Obtener detalle
PUT / PATCH	/api/insumos/{id}/	Actualizar
DELETE	/api/insumos/{id}/	Eliminar

CRUD completo implementado mediante ModelViewSet.

🧾 API 2 – Pedidos con Restricciones

Endpoint base:

/api/pedidos/

Método	Estado
POST	✅ Permitido
PUT / PATCH	✅ Permitido
GET (listar)	❌ Bloqueado
DELETE	❌ Bloqueado

Las operaciones GET (listado) y DELETE están bloqueadas explícitamente retornando HTTP 405, cumpliendo con la rúbrica.

🔍 API 3 – Filtro Avanzado de Pedidos

Endpoint:

/api/pedidos/filtrar/


Parámetros soportados:

estado → estado del pedido

desde → fecha inicio (YYYY-MM-DD)

hasta → fecha término (YYYY-MM-DD)

limit → límite de resultados (1 a 200)

Ejemplos de uso:

/api/pedidos/filtrar/?estado=ENTREGADO
/api/pedidos/filtrar/?desde=2025-12-01&hasta=2025-12-31&limit=10


Este endpoint permite consultar pedidos sin exponer el listado general, cumpliendo el requerimiento de filtros avanzados.

⚙️ Configuración de Producción

El sistema está configurado para producción con:

DEBUG = False

ALLOWED_HOSTS configurado correctamente

Archivos estáticos servidos con WhiteNoise

Archivos multimedia gestionados con Cloudinary

Variables sensibles manejadas mediante variables de entorno

Base de datos operativa en entorno productivo

🗂️ Estructura General del Proyecto
PRUEBA_3_PAREDES_GABRIEL/
│
├── appTienda/
│   ├── api/
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── admin.py
│
├── templates/
│   ├── catalogo.html
│   ├── detalle_producto.html
│   ├── solicitud.html
│   ├── seguimiento.html
│   └── reporte.html
│
├── static/
├── manage.py
├── requirements.txt
└── README.md

✅ Cumplimiento de Rúbrica

✔ Uso de Django y Django REST Framework

✔ CRUD completo para Insumos

✔ API de Pedidos con restricciones de métodos

✔ Endpoint de filtros avanzados

✔ Reporte dinámico con ORM + Chart.js

✔ Vista protegida (solo admin / staff)

✔ Configuración lista para producción

✔ Deploy funcional en la nube
