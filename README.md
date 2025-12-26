# Prueba N°4 – Tienda + API (Django + DRF)

## Stack
- Django 5.2.6
- Django REST Framework
- PostgreSQL (Render) / SQLite (fallback)
- Deploy: Render
- Media: Cloudinary
- Static: WhiteNoise

## Deploy
URL: https://prueba-gabriel.onrender.com/

## Usuario Admin
- usuario: admin
- contraseña: admin

## Endpoints API (DRF)

### API 1 – CRUD Insumos
- GET /api/insumos/ (listar)
- POST /api/insumos/ (crear)
- GET /api/insumos/{id}/ (detalle)
- PUT/PATCH /api/insumos/{id}/ (actualizar)
- DELETE /api/insumos/{id}/ (eliminar)

### API 2 – Pedidos (sin listado ni delete)
- POST /api/pedidos/ (crear)
- PUT/PATCH /api/pedidos/{id}/ (editar)
- GET /api/pedidos/ → 405 Method Not Allowed (listado bloqueado)
- DELETE /api/pedidos/{id}/ → 405 Method Not Allowed (eliminación bloqueada)

### API 3 – Filtros de pedidos
- GET /api/pedidos/filtrar/?limit=10
- GET /api/pedidos/filtrar/?estado=ENTREGADO
- GET /api/pedidos/filtrar/?desde=YYYY-MM-DD&hasta=YYYY-MM-DD&limit=50
- Estados válidos: SOLICITADO, APROBADO, EN_PROCESO, REALIZADO, ENTREGADO, FINALIZADO, CANCELADO

## Reporte (vista protegida staff)
Ruta: /reporte/
- Requiere login admin/staff
- Muestra tabla de pedidos por estado y gráfico Chart.js
