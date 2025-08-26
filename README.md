# EVA-1-DJANGO - Taller Mecánico

## Descripción
Proyecto de evaluación N°1 de Django con temática de taller mecánico.  
El proyecto contiene tres apps separadas: `mecanico`, `vehiculo` y `procedimiento`.  
Cada app tiene sus modelos, vistas CRUD y administración en Django Admin.

---

## Funcionalidades
- CRUD completo para **Mecánicos**, **Vehículos** y **Procedimientos**.  
- Validación de **patente única** en Vehículos.  
- Relación entre Procedimientos, Mecánicos y Vehículos mediante **ForeignKey**.  
- Django Admin configurado con `list_display`, `search_fields` y `list_filter`.  

---

## Requisitos
- Python 3.10+  
- Django 5+  

---

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Aruxan/EVA-1-DJANGO.git
cd EVA-1-DJANGO