# 🛒 Prueba N°4 – Tienda Online + API REST

**Asignatura:** Programación Back End  
**Carrera:** Ingeniería en Programación e Informática  
**Institución:** INACAP  
**Estudiante:** Gabriel Paredes Medina

---

## 📌 Descripción General
Este proyecto corresponde a la **Evaluación Sumativa 4** de la asignatura Programación Back End. Consiste en la extensión de una tienda online desarrollada previamente, incorporando una **API REST**, un **reporte dinámico protegido**, y el **despliegue (deploy)** del sistema en un entorno de producción real.

El sistema permite la gestión completa de productos, insumos y pedidos, cumpliendo con todos los requisitos de la rúbrica oficial.

## 🧱 Stack Tecnológico
* **Backend:** Django 5.x
* **API REST:** Django REST Framework (DRF)
* **Base de Datos:** PostgreSQL (Producción) / SQLite (Desarrollo)
* **Archivos Estáticos:** WhiteNoise
* **Imágenes / Media:** Cloudinary
* **Deploy:** Render

## 🌐 Deploy en Producción
La aplicación se encuentra operativa y accesible al público en el siguiente enlace:  
👉 **[https://prueba-gabriel.onrender.com/](https://prueba-gabriel.onrender.com/)**

## 🔐 Credenciales de Prueba (Administración)
Para acceder al panel administrativo y a las vistas protegidas:

| Rol | Usuario | Contraseña |
| :--- | :--- | :--- |
| **Administrador** | `admin` | `admin` |

* **URL Admin:** `/admin/`

---

## 📊 Reporte Dinámico (Vista Protegida)
* **Ruta:** `/reporte/`
* **Acceso:** Restringido a usuarios autenticados (Staff/Admin).
* **Características:**
    * Consultas reales mediante el **ORM de Django**.
    * Visualización de datos mediante **tablas y gráficos dinámicos** (Chart.js).
    * Métricas de pedidos agrupados por estado.

## 🔌 API REST – Django REST Framework
Se han implementado tres APIs siguiendo las restricciones de la rúbrica:

### 📦 API 1 – CRUD de Insumos
**Endpoint:** `/api/insumos/`
Permite la gestión completa de materias primas (Crear, Listar, Ver detalle, Modificar y Eliminar).
para poder eliminar o editar es necesario escribir el id del producto "/api/insumos/(ID)"

### 🧾 API 2 – Pedidos con Restricciones
**Endpoint:** `/api/pedidos/`
* ✅ **Permitido:** Crear (POST) y Modificar (PUT/PATCH).
* ❌ **Bloqueado:** Listado general (GET) y Eliminación (DELETE).

### 🔍 API 3 – Filtro Avanzado de Pedidos
**Endpoint:** `/api/pedidos/filtrar/`
Soporta los siguientes parámetros de consulta:
* `desde` / `hasta`: Rango de fechas (YYYY-MM-DD).
* `estado`: Filtro por estado del pedido.
* `limit`: Cantidad máxima de resultados.

---

## ⚙️ Configuración de Producción
El sistema cumple con los estándares de seguridad para deploy:
* `DEBUG = False`
* `ALLOWED_HOSTS` configurado para el dominio de Render.
* Manejo de variables de entorno para datos sensibles.
* Servidor de archivos estáticos configurado adecuadamente.

## ✅ Cumplimiento de Rúbrica
- [x] Continuidad del proyecto anterior.
- [x] Repositorio GitHub público.
- [x] Vista de reporte protegida con Gráficos (Chart.js).
- [x] API CRUD Insumos funcional.
- [x] API Pedidos con restricciones de métodos (No GET colección / No DELETE).
- [x] API de filtros avanzados con validación de parámetros.
- [x] Deploy funcional con URL pública y archivos estáticos.
