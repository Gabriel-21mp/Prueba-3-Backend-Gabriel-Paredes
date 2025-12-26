# 🛒 Prueba N°4 – Tienda Online + API REST

[cite_start]**Asignatura:** Programación Back End [cite: 2]  
**Carrera:** Ingeniería en Programación e Informática  
**Institución:** INACAP  
**Estudiante:** Gabriel Paredes Medina

---

## 📌 Descripción General
[cite_start]Este proyecto corresponde a la **Evaluación Sumativa 4** de la asignatura Programación Back End[cite: 1]. [cite_start]Consiste en la extensión de una tienda online desarrollada previamente, incorporando una **API REST**, un **reporte dinámico protegido**, y el **despliegue (deploy)** del sistema en un entorno de producción real[cite: 11, 12, 17].

[cite_start]El sistema permite la gestión completa de productos, insumos y pedidos, cumpliendo con todos los requisitos de la rúbrica oficial[cite: 19].

## 🧱 Stack Tecnológico
* [cite_start]**Backend:** Django 5.x [cite: 6]
* [cite_start]**API REST:** Django REST Framework (DRF) [cite: 7, 16]
* [cite_start]**Base de Datos:** PostgreSQL (Producción) / SQLite (Desarrollo) [cite: 37, 67]
* [cite_start]**Archivos Estáticos:** WhiteNoise [cite: 67]
* [cite_start]**Imágenes / Media:** Cloudinary [cite: 67]
* [cite_start]**Deploy:** Render [cite: 33]

## 🌐 Deploy en Producción
La aplicación se encuentra operativa y accesible al público en el siguiente enlace:  
[cite_start]👉 **[https://prueba-gabriel.onrender.com/](https://prueba-gabriel.onrender.com/)** [cite: 39]

## 🔐 Credenciales de Prueba (Administración)
[cite_start]Para acceder al panel administrativo y a las vistas protegidas: [cite: 73]

| Rol | Usuario | Contraseña |
| :--- | :--- | :--- |
| **Administrador** | `admin` | `admin` |

* [cite_start]**URL Admin:** `/admin/` [cite: 40]

---

## 📊 Reporte Dinámico (Vista Protegida)
* [cite_start]**Ruta:** `/reporte/` [cite: 67]
* [cite_start]**Acceso:** Restringido a usuarios autenticados (Staff/Admin)[cite: 28].
* **Características:**
    * [cite_start]Consultas reales mediante el **ORM de Django**[cite: 27].
    * [cite_start]Visualización de datos mediante **tablas y gráficos dinámicos** (Chart.js)[cite: 30].
    * [cite_start]Métricas de pedidos agrupados por estado[cite: 22].

## 🔌 API REST – Django REST Framework
[cite_start]Se han implementado tres APIs siguiendo las restricciones de la rúbrica: [cite: 43]

### 📦 API 1 – CRUD de Insumos
[cite_start]**Endpoint:** `/api/insumos/` [cite: 46]
[cite_start]Permite la gestión completa de materias primas (Crear, Listar, Ver detalle, Modificar y Eliminar)[cite: 47].

### 🧾 API 2 – Pedidos con Restricciones
[cite_start]**Endpoint:** `/api/pedidos/` [cite: 49]
* [cite_start]✅ **Permitido:** Crear (POST) y Modificar (PUT/PATCH)[cite: 50].
* [cite_start]❌ **Bloqueado:** Listado general (GET) y Eliminación (DELETE)[cite: 52, 53].

### 🔍 API 3 – Filtro Avanzado de Pedidos
[cite_start]**Endpoint:** `/api/pedidos/filtrar/` [cite: 55]
[cite_start]Soporta los siguientes parámetros de consulta: [cite: 56]
* [cite_start]`desde` / `hasta`: Rango de fechas (YYYY-MM-DD)[cite: 57].
* [cite_start]`estado`: Filtro por estado del pedido[cite: 58].
* [cite_start]`limit`: Cantidad máxima de resultados[cite: 59].

---

## ⚙️ Configuración de Producción
[cite_start]El sistema cumple con los estándares de seguridad para deploy: [cite: 67]
* `DEBUG = False`
* `ALLOWED_HOSTS` configurado para el dominio de Render.
* Manejo de variables de entorno para datos sensibles.
* Servidor de archivos estáticos configurado.

## ✅ Cumplimiento de Rúbrica
- [x] [cite_start]Continuidad del proyecto anterior [cite: 67]
- [x] [cite_start]Repositorio GitHub público [cite: 67]
- [x] [cite_start]Vista de reporte protegida con Gráficos [cite: 67]
- [x] [cite_start]API CRUD Insumos [cite: 67]
- [x] [cite_start]API Pedidos con restricciones (no list/delete) [cite: 67]
- [x] [cite_start]API de filtros avanzados con validación [cite: 67]
- [x] [cite_start]Deploy funcional con URL pública [cite: 67]
