# Despliegue de Diagx en AWS

## Estado
- [x] Cuenta de AWS creada
- [x] MFA activado en el usuario raiz
- [x] Alerta de presupuesto (Budget)
- [x] Usuario IAM para el trabajo diario (no usar el raiz)
- [x] EC2 con Docker y Docker Compose
- [x] Desplegar API + Postgres + Redis con docker-compose.yml
- [x] Secretos reales (contraseña de Postgres en .env del servidor)
- [x] Postgres y Redis accesibles solo desde localhost
- [x] Script de deploy (deploy.sh)
- [ ] IP fija (Elastic IP)
- [ ] Deploy automático desde GitHub Actions

## Arquitectura actual
Una instancia EC2 t4g.small (Ubuntu, ARM) en us-east-1, corriendo la API,
Postgres y Redis con Docker Compose. Solo estan abiertos los puertos
22 (SSH, solo desde mi IP) y 8000 (API).

## Notas
- Nunca subir claves de AWS, la llave .pem ni el archivo .env al repositorio.
- Detener la instancia cuando no se este usando.
