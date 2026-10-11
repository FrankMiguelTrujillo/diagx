# Despliegue de Diagx en AWS

## Estado
- [x] Cuenta de AWS creada (Free Plan: 6 meses, sin cobros sorpresa)
- [ ] MFA activado en el usuario raíz
- [ ] Alerta de presupuesto (Budget)
- [ ] Usuario IAM para el trabajo diario (no usar el raíz)
- [ ] EC2 con Docker y Docker Compose
- [ ] Desplegar API + Postgres + Redis con docker-compose.yml
- [ ] Secretos reales (no usar diagx123 en producción)

## Arquitectura inicial
Una sola instancia EC2 corriendo los tres servicios con Docker Compose.
Es lo más simple y barato para aprender. RDS y ECS quedan para más adelante.

## Notas
- Nunca subir claves de AWS ni el archivo .env al repositorio.
- Apagar o eliminar recursos que no se estén usando.