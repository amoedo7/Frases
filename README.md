# Frases

Experimento histórico en Python alrededor de una lista **BIP-39** y generación de combinaciones/estructuras de directorios.

## Estado

**Experimental / no productivo.** El código actual no es una wallet, no valida frases mnemónicas y no debe utilizarse como herramienta de recuperación de fondos.

## Qué hace el snapshot actual

`main.py` carga palabras desde `bip39.txt`, genera combinaciones de 12 palabras mediante `itertools.combinations` y construye una estructura de carpetas a partir de ellas.

La ruta de salida todavía contiene un placeholder:

```text
/path/to/your/github/repository
```

Por lo tanto el programa, tal como está versionado, es una prueba incompleta.

## Advertencia técnica

El espacio combinatorio de BIP-39 es enorme. Intentar materializar combinaciones masivas en disco no es una estrategia práctica y puede agotar almacenamiento/inodos muy rápidamente.

## Seguridad y uso responsable

- no introduzcas seeds reales ni frases que protejan fondos;
- no uses este proyecto para intentar acceder a wallets ajenas;
- no publiques frases mnemónicas, private keys o backups de wallets;
- para pruebas, usa únicamente datos sintéticos y desechables.

## Relación con DesarrollAMO

Se conserva como experimento de programación/criptografía de una etapa temprana. Si alguna idea útil se retoma, debería rediseñarse desde un objetivo legítimo y verificable en lugar de escalar este enfoque combinatorio.

---

**DesarrollAMO** · experimento preservado con límites y contexto claros.
