# 🐱 Dexter Landing — Streamlit

Landing page de una sola página dedicada a **Dexter**, un gato naranja
súper peludo. Hecha con **Python + Streamlit**.

## Estructura

```
dexter-landing/
├── app.py             # App principal de Streamlit (landing completa)
├── requirements.txt   # Dependencias
└── README.md
```

## Cómo correrlo localmente

1. (Opcional) Crea un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Ejecuta la app:
   ```bash
   streamlit run app.py
   ```

4. Se abrirá automáticamente en tu navegador en
   `http://localhost:8501`.

## Personalización rápida

- **Fotos reales de Dexter**: en la sección "Galería" hay un
  `st.file_uploader` de ejemplo. Puedes reemplazar las tarjetas con
  emoji (`gallery_emojis`) por `st.image("ruta/a/tu/foto.jpg")`.
- **Colores**: todo el tema naranja está definido en el bloque
  `CUSTOM_CSS` dentro de `app.py` (variables como `#D9480F`,
  `#FFA94D`, `#FFD8A8`).
- **Textos**: las tarjetas de "Sobre Dexter" y los mensajes del CTA
  están directamente en `app.py`, listos para editar.
- **Formulario de contacto**: actualmente solo muestra un mensaje de
  éxito; puedes conectarlo a un servicio de email o a una base de
  datos según lo necesites.

## Referencia

Documentación oficial de Streamlit: https://docs.streamlit.io/
