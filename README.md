# PRUEBA 3 – Framework de Backend  
**Proyecto Django – Catálogo y Pedidos**

## 📌 Descripción del proyecto
Este proyecto corresponde a una aplicación web desarrollada con **Django**, cuyo objetivo es gestionar un **catálogo de productos** y permitir la **creación y seguimiento de pedidos** de forma simple y clara, cumpliendo los requerimientos de la asignatura.

El sistema permite:
- Visualizar productos organizados por categorías.
- Filtrar productos por nombre y categoría.
- Solicitar un producto mediante un formulario.
- Generar un pedido con un **token único de seguimiento**.
- Consultar el estado del pedido mediante una URL con token.
- Administrar productos, insumos y pedidos desde Django Admin.

---

## 🛠️ Tecnologías utilizadas
- Python 3
- Django
- SQLite
- HTML (templates de Django)

---

## 📂 Estructura general del proyecto
- **Catálogo público** de productos.
- **Formulario de solicitud de pedido**.
- **Seguimiento del pedido** mediante token.
- **Panel de administración** para gestionar categorías, productos, insumos y pedidos.

---

## 🚀 Instrucciones para ejecutar el proyecto

### 1️⃣ Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd PRUEBA_3_PAREDES_GABRIEL

2️⃣ Crear y activar entorno virtual
python -m venv .venv


En Windows:

.venv\Scripts\activate


En macOS / Linux:

source .venv/bin/activate

3️⃣ Instalar dependencias
pip install -r requirements.txt

4️⃣ Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

5️⃣ Crear superusuario (opcional)
python manage.py createsuperuser

6️⃣ Ejecutar el servidor
python manage.py runserver


Acceder desde el navegador:

Sitio web: http://127.0.0.1:8000/

Administración: http://127.0.0.1:8000/admin/

🧪 Datos de prueba

El sistema permite cargar datos de prueba desde el panel de administración, tales como:

Categorías

Productos (con imágenes)

Insumos

Pedidos

Esto permite evaluar tanto el flujo público como la gestión interna del sistema.

📝 Observaciones

El sistema no utiliza autenticación para clientes.

El seguimiento de pedidos se realiza mediante un token único generado automáticamente.

El enfoque del proyecto es mantener una solución clara, funcional y sin sobreingeniería.
