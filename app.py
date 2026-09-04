import streamlit as st

# ------------------------------------------------------------
# Configuración de la página
# ------------------------------------------------------------
st.set_page_config(
    page_title="Dexter 🐱 | El gato naranja más peludo",
    page_icon="🐱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ------------------------------------------------------------
# Estilos personalizados (tema naranja / gato peludo)
# ------------------------------------------------------------
CUSTOM_CSS = """
<style>
    /* Fondo general */
    .stApp {
        background: linear-gradient(180deg, #FFF4E6 0%, #FFE8CC 100%);
    }

    /* Ocultar el menú y footer por defecto de Streamlit */
    #MainMenu, footer, header {visibility: hidden;}

    /* Contenedor hero */
    .hero {
        text-align: center;
        padding: 3rem 1rem 2rem 1rem;
    }

    .hero-emoji {
        font-size: 6rem;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-12px); }
        100% { transform: translateY(0px); }
    }

    .hero-title {
        font-size: 3.2rem;
        font-weight: 900;
        color: #D9480F;
        margin-bottom: 0.2rem;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 1.3rem;
        color: #A85A1E;
        font-weight: 500;
        margin-bottom: 1.5rem;
    }

    .badge-row {
        display: flex;
        justify-content: center;
        gap: 0.6rem;
        flex-wrap: wrap;
        margin-bottom: 1rem;
    }

    .badge {
        background-color: #FFD8A8;
        color: #D9480F;
        padding: 0.35rem 0.9rem;
        border-radius: 999px;
        font-size: 0.9rem;
        font-weight: 700;
        border: 2px solid #FFA94D;
    }

    /* Tarjetas */
    .card {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 1.6rem;
        box-shadow: 0 8px 20px rgba(217, 72, 15, 0.12);
        border: 3px solid #FFD8A8;
        height: 100%;
        transition: transform 0.2s ease;
    }

    .card:hover {
        transform: translateY(-6px);
    }

    .card-emoji {
        font-size: 2.6rem;
        margin-bottom: 0.5rem;
    }

    .card-title {
        font-size: 1.25rem;
        font-weight: 800;
        color: #D9480F;
        margin-bottom: 0.4rem;
    }

    .card-text {
        color: #7A4A20;
        font-size: 0.98rem;
        line-height: 1.5;
    }

    /* Sección título */
    .section-title {
        text-align: center;
        font-size: 2.1rem;
        font-weight: 800;
        color: #D9480F;
        margin: 2.5rem 0 0.3rem 0;
    }

    .section-sub {
        text-align: center;
        color: #A85A1E;
        margin-bottom: 2rem;
    }

    /* Caja de la "foto" de Dexter hecha con CSS */
    .dexter-portrait {
        width: 260px;
        height: 260px;
        margin: 0 auto 1.5rem auto;
        border-radius: 50%;
        background: radial-gradient(circle at 35% 30%, #FFB870, #E8590C 75%);
        border: 8px solid #FFFFFF;
        box-shadow: 0 10px 30px rgba(217, 72, 15, 0.25);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 8rem;
    }

    /* Barra de "esponjosidad" */
    .fluff-label {
        display: flex;
        justify-content: space-between;
        color: #A85A1E;
        font-weight: 700;
        font-size: 0.9rem;
        margin-bottom: 0.2rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2.5rem 1rem 1.5rem 1rem;
        color: #A85A1E;
        font-size: 0.9rem;
    }

    .cta-box {
        background: linear-gradient(135deg, #FFA94D, #FF922B);
        border-radius: 24px;
        padding: 2.5rem 2rem;
        text-align: center;
        margin-top: 2.5rem;
        color: white;
        box-shadow: 0 12px 28px rgba(217, 72, 15, 0.25);
    }

    .cta-box h2 {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    .stButton>button {
        background-color: #D9480F;
        color: white;
        border-radius: 999px;
        padding: 0.6rem 1.8rem;
        font-weight: 700;
        border: none;
    }

    .stButton>button:hover {
        background-color: #A83E10;
        color: white;
    }
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ------------------------------------------------------------
# HERO
# ------------------------------------------------------------
st.markdown(
    """
    <div class="hero">
        <div class="hero-emoji">🐈‍⬛🧡</div>
        <div class="hero-title">Dexter</div>
        <div class="hero-subtitle">El gato naranja más peludo del barrio 🧡</div>
        <div class="badge-row">
            <span class="badge">🧡 100% Naranja</span>
            <span class="badge">🐾 Súper Peludo</span>
            <span class="badge">😻 Ronroneo Garantizado</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# "Retrato" de Dexter hecho con CSS/emoji
st.markdown(
    """
    <div class="dexter-portrait">🐱</div>
    """,
    unsafe_allow_html=True,
)

col_a, col_b, col_c = st.columns(3)
with col_a:
    st.markdown('<div class="fluff-label"><span>Pelaje</span><span>98%</span></div>', unsafe_allow_html=True)
    st.progress(98)
with col_b:
    st.markdown('<div class="fluff-label"><span>Ternura</span><span>100%</span></div>', unsafe_allow_html=True)
    st.progress(100)
with col_c:
    st.markdown('<div class="fluff-label"><span>Energía para siestas</span><span>95%</span></div>', unsafe_allow_html=True)
    st.progress(95)

# ------------------------------------------------------------
# SOBRE DEXTER
# ------------------------------------------------------------
st.markdown('<div class="section-title">Sobre Dexter</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Todo lo que necesitas saber sobre este bola de pelo naranja</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        """
        <div class="card">
            <div class="card-emoji">🧡</div>
            <div class="card-title">Pelaje Naranja</div>
            <div class="card-text">
                Dexter luce un hermoso pelaje anaranjado tipo jengibre, suave,
                denso y con vetas más claras alrededor del hocico y la pancita.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        """
        <div class="card">
            <div class="card-emoji">🐾</div>
            <div class="card-title">Súper Esponjoso</div>
            <div class="card-text">
                Su cola es como un plumero y su cuerpo parece una nube naranja.
                Cepillarlo es casi un deporte diario.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
with c3:
    st.markdown(
        """
        <div class="card">
            <div class="card-emoji">😴</div>
            <div class="card-title">Experto en Siestas</div>
            <div class="card-text">
                Dexter duerme donde le da la gana: cajas, camas, teclados...
                si hay sol, ahí estará él.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ------------------------------------------------------------
# GALERÍA (placeholders listos para tus fotos reales)
# ------------------------------------------------------------
st.markdown('<div class="section-title">Galería de Dexter</div>', unsafe_allow_html=True)
st.markdown('<div class="section-sub">Reemplaza estos espacios con tus propias fotos de Dexter 📸</div>', unsafe_allow_html=True)

g1, g2, g3, g4 = st.columns(4)
gallery_emojis = ["🧡", "😺", "🐾", "😽"]
gallery_captions = ["Estirándose al sol", "Modo curioso", "Huellitas por doquier", "Cara de bueno"]

for col, emoji, caption in zip([g1, g2, g3, g4], gallery_emojis, gallery_captions):
    with col:
        st.markdown(
            f"""
            <div class="card" style="text-align:center;">
                <div style="font-size:3.5rem;">{emoji}</div>
                <div class="card-text" style="margin-top:0.5rem;">{caption}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.file_uploader(
    "📷 Sube una foto real de Dexter (opcional)",
    type=["png", "jpg", "jpeg"],
    help="Esto no se guarda en ningún lado, solo se muestra en la vista previa.",
)

# ------------------------------------------------------------
# CTA / Contacto
# ------------------------------------------------------------
st.markdown(
    """
    <div class="cta-box">
        <h2>¿Quieres conocer más a Dexter? 🧡</h2>
        <p>Déjanos tu correo y te enviaremos fotos y videos de sus aventuras felinas.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("contacto_form", clear_on_submit=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        email = st.text_input("Tu correo electrónico", placeholder="tucorreo@ejemplo.com", label_visibility="collapsed")
    with col2:
        enviado = st.form_submit_button("¡Quiero fotos! 🐱")

    if enviado:
        if email and "@" in email:
            st.success(f"¡Gracias! Enviaremos fotos de Dexter a **{email}** 🧡🐾")
        else:
            st.error("Por favor ingresa un correo válido.")

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown(
    """
    <div class="footer">
        Hecho con 🧡 y mucho pelo naranja usando <b>Streamlit</b> · Dexter © 2026
    </div>
    """,
    unsafe_allow_html=True,
)
