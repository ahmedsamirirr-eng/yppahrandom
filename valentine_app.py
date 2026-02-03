"""
Valentine's Day Streamlit App - "Will you be my Valentine?"
For Alaa (LoLo) 💖
"""

import streamlit as st
import random
from pathlib import Path

# Page config - must be first Streamlit command
st.set_page_config(
    page_title="Will you be my Valentine? 💕",
    page_icon="💖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for romantic theme
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&family=Dancing+Script:wght@700&display=swap');
    
    .stApp {
        background: linear-gradient(180deg, #ffebf0 0%, #ffd6e0 50%, #ffcce0 100%);
        background-attachment: fixed;
    }
    
    /* Center main content in viewport */
    .main .block-container {
        max-width: 720px;
        margin-left: auto;
        margin-right: auto;
        padding-left: 1rem;
        padding-right: 1rem;
        text-align: center;
    }
    
    .valentine-card {
        background: linear-gradient(145deg, #fff5f8 0%, #ffe8ee 100%);
        border-radius: 24px;
        padding: 2.5rem;
        box-shadow: 0 12px 40px rgba(255, 105, 135, 0.25), 0 4px 15px rgba(0,0,0,0.08);
        border: 2px solid rgba(255, 182, 193, 0.6);
        text-align: center;
        margin: 2rem auto;
        position: relative;
        overflow: hidden;
        width: 100%;
    }
    
    .valentine-card .subtitle,
    .valentine-card .main-question {
        text-align: center;
        margin-left: auto;
        margin-right: auto;
    }
    
    .valentine-card::before {
        content: "💕";
        position: absolute;
        top: 15px;
        left: 20px;
        font-size: 2rem;
        opacity: 0.7;
    }
    
    .valentine-card::after {
        content: "💕";
        position: absolute;
        top: 15px;
        right: 20px;
        font-size: 2rem;
        opacity: 0.7;
    }
    
    .main-question {
        font-family: 'Dancing Script', cursive;
        font-size: 2.8rem;
        font-weight: 700;
        color: #c41e3a;
        margin: 1rem auto;
        text-align: center;
        display: block;
        width: 100%;
        text-shadow: 1px 1px 2px rgba(196, 30, 58, 0.2);
    }
    
    .celebration-text {
        font-family: 'Dancing Script', cursive;
        font-size: 3.5rem;
        font-weight: 700;
        color: #c41e3a;
        animation: pulse 1s ease-in-out infinite alternate;
        text-align: center;
        display: block;
        margin: 0 auto;
        width: 100%;
    }
    
    .celebration-header {
        background: linear-gradient(145deg, #fff5f8 0%, #ffe8ee 100%);
        border-radius: 16px;
        padding: 1rem 2rem;
        box-shadow: 0 8px 25px rgba(255, 105, 135, 0.2);
        border: 2px solid rgba(255, 182, 193, 0.6);
        text-align: center;
        margin-bottom: 1rem;
        font-family: 'Dancing Script', cursive;
        font-size: 1.8rem;
        font-weight: 700;
        color: #c41e3a;
    }
    
    .celebration-header .hearts { font-size: 1.4rem; margin: 0 0.2rem; }
    
    @keyframes pulse {
        from { transform: scale(1); }
        to { transform: scale(1.05); }
    }
    
    .heart-float {
        font-size: 1.5rem;
        opacity: 0.6;
        margin: 0 0.2rem;
    }
    
    .gallery-title {
        font-family: 'Quicksand', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: #c41e3a;
        margin: 2rem 0 1rem;
        text-align: center;
    }
    
    .gallery-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1rem;
        margin: 1.5rem 0;
        padding: 1rem;
    }
    
    .gallery-item {
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 25px rgba(255, 105, 135, 0.2);
        border: 3px solid rgba(255, 182, 193, 0.5);
        aspect-ratio: 1;
        object-fit: cover;
    }
    
    .subtitle {
        font-family: 'Quicksand', sans-serif;
        font-size: 1.1rem;
        color: #8b2942;
        margin-bottom: 1.5rem;
        text-align: center;
        display: block;
        width: 100%;
    }
    
    div[data-testid="stHorizontalBlock"] > div {
        border-radius: 12px;
    }
    
    /* Smooth floating No button container */
    .no-btn-wrapper {
        position: relative;
        width: 100%;
        min-height: 52px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .no-btn-float {
        position: absolute;
        padding: 0.5rem 1.5rem;
        font-size: 1.1rem;
        border-radius: 12px;
        background: linear-gradient(145deg, #ffe8ee 0%, #ffd6e0 100%);
        border: 2px solid rgba(255, 182, 193, 0.8);
        color: #c41e3a;
        cursor: pointer;
        font-family: 'Quicksand', sans-serif;
        font-weight: 600;
        box-shadow: 0 4px 15px rgba(255, 105, 135, 0.2);
        animation: smoothFloat 8s ease-in-out infinite;
        white-space: nowrap;
        transition: transform 0.2s ease;
    }
    
    .no-btn-float:hover {
        transform: scale(1.05);
    }
    
    @keyframes smoothFloat {
        0%, 100% { left: 5%; top: 50%; transform: translateY(-50%); }
        25% { left: 35%; top: 50%; transform: translateY(-50%); }
        50% { left: 65%; top: 50%; transform: translateY(-50%); }
        75% { left: 25%; top: 50%; transform: translateY(-50%); }
    }
    
    .love-words {
        font-family: 'Dancing Script', cursive;
        font-size: 1.25rem;
        color: #8b2942;
        text-align: center;
        margin: 1rem auto;
        padding: 0.75rem 1rem;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 12px;
        line-height: 1.6;
        font-weight: 600;
        display: block;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "accepted" not in st.session_state:
    st.session_state.accepted = False

# Paths and media
SCRIPT_DIR = Path(__file__).resolve().parent
IMAGES_DIR = SCRIPT_DIR / "images"

# Local images from the images folder (our memories gallery)
def get_gallery_images():
    exts = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
    if not IMAGES_DIR.exists():
        return []
    paths = sorted(
        [f for f in IMAGES_DIR.iterdir() if f.is_file() and f.suffix.lower() in exts],
        key=lambda p: p.name,
    )
    return [str(p) for p in paths]

GALLERY_IMAGES = get_gallery_images()

# Giphy embeds for celebration - two lovely white bear stickers
BEAR_GIPHY_IDS = [
    "l0MYt5jPR6QX5pnqM",   # Milk & Mocha hugging bear couple (Giphy)
    "https://s3.getstickerpack.com/storage/uploads/sticker-pack/milk-amp-mocha/sticker_12.webp?36206fc85917f1de1805a4ac284e70af&d=200x200"  # Milk & Mocha bear couple sticker
]

# The Video ID for Amr Diab - Afelty El Le'ba
YOUTUBE_VIDEO_ID = "NrqGTgl3iFw"

st.markdown(f"""
<div style="display: flex; justify-content: center; margin: 20px 0;">
    <iframe 
        width="640" 
        height="360" 
        src="https://www.youtube.com/embed/{YOUTUBE_VIDEO_ID}?rel=0&modestbranding=1&autoplay=0" 
        title="YouTube video player" 
        frameborder="0" 
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
        allowfullscreen
        style="border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.3);"
    ></iframe>
</div>
""", unsafe_allow_html=True)

# Love words to show on the page
LOVE_WORDS = [
    "You are my sunshine, my only sunshine. ☀️💕",
    "I love you to the moon and back. 🌙❤️",
    "Every moment with you is a gift. 🎁",
    "You make my heart skip a beat. 💓",
    "Forever isn't long enough with you. 💖",
    "You are the love of my life. 🌹",
]

# ---- MAIN CONTENT ----
if not st.session_state.accepted:
    # Love words at top
    st.markdown(
        f'<p class="love-words">💝 {random.choice(LOVE_WORDS)} 💝</p>',
        unsafe_allow_html=True,
    )

    # Main card with question
    st.markdown('<div class="valentine-card">', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">💕 For someone very special 💕</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="main-question">Alaa (LoLo), will you be my Valentine?</p>',
        unsafe_allow_html=True,
    )
    st.markdown('<p class="subtitle">❤️ Choose your answer below ❤️</p>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Buttons: Yes (Streamlit), No (runs away crazily all over the area when she tries to catch it)
    btn_col1, btn_col2 = st.columns([1, 3])
    with btn_col1:
        yes_clicked = st.button("Yes 💖", use_container_width=True, type="primary")

    with btn_col2:
        # No button: runs away all over the screen when mouse gets near or on click
        st.components.v1.html(
            """
            <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@600&display=swap" rel="stylesheet">
            <div id="no-zone" style="position: relative; width: 100%; height: 320px; background: transparent;">
                <button type="button" id="no-btn" style="
                    position: absolute; padding: 0.5rem 1.5rem; font-size: 1.1rem; border-radius: 12px;
                    background: linear-gradient(145deg, #ffe8ee 0%, #ffd6e0 100%);
                    border: 2px solid rgba(255, 182, 193, 0.8); color: #c41e3a; cursor: pointer;
                    font-family: 'Quicksand', sans-serif; font-weight: 600;
                    box-shadow: 0 4px 15px rgba(255, 105, 135, 0.2); white-space: nowrap;
                    transition: left 0.15s ease-out, top 0.15s ease-out;
                ">No 🙈</button>
            </div>
            <script>
            (function() {
                var zone = document.getElementById('no-zone');
                var btn = document.getElementById('no-btn');
                var zoneRect = zone.getBoundingClientRect();
                var RUN_DISTANCE = 90;
                function getZoneBounds() {
                    var r = zone.getBoundingClientRect();
                    return { w: r.width, h: r.height, left: r.left, top: r.top };
                }
                function randomPos() {
                    var b = getZoneBounds();
                    var btnW = 100; var btnH = 44;
                    return {
                        left: Math.max(0, Math.random() * (b.w - btnW)),
                        top: Math.max(0, Math.random() * (b.h - btnH))
                    };
                }
                function moveBtn() {
                    var p = randomPos();
                    btn.style.left = p.left + 'px';
                    btn.style.top = p.top + 'px';
                }
                setTimeout(moveBtn, 50);
                zone.addEventListener('mousemove', function(e) {
                    var r = zone.getBoundingClientRect();
                    var bx = (parseFloat(btn.style.left) || 0) + 50;
                    var by = (parseFloat(btn.style.top) || 0) + 22;
                    var mx = e.clientX - r.left;
                    var my = e.clientY - r.top;
                    var dist = Math.sqrt((mx - bx) * (mx - bx) + (my - by) * (my - by));
                    if (dist < RUN_DISTANCE) moveBtn();
                });
                btn.addEventListener('click', function(e) {
                    e.preventDefault();
                    moveBtn();
                });
                btn.addEventListener('mouseenter', moveBtn);
            })();
            </script>
            """,
            height=330,
        )

    if yes_clicked:
        st.session_state.accepted = True
        st.rerun()

else:
    # ---- CELEBRATION ----
    # Love words
    st.markdown(
        f'<p class="love-words">💝 {random.choice(LOVE_WORDS)} 💝</p>',
        unsafe_allow_html=True,
    )
    # White bar header with celebratory text (not empty)
    st.markdown(
        '<div class="celebration-header">'
        '<span class="hearts">💖</span> She said yes! You\'re my Valentine! '
        '<span class="hearts">💖</span></div>',
        unsafe_allow_html=True,
    )

    # st.markdown('<div class="valentine-card">', unsafe_allow_html=True)
    st.markdown(
        '<p class="celebration-text">YAAAAAAAAH! 🎉💘</p>',
        unsafe_allow_html=True,
    )
    st.markdown("</div style='text-align:center;>", unsafe_allow_html=True)

    # st.markdown("<br>", unsafe_allow_html=True)

    # Centered vertical layout
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

    for bear in BEAR_GIPHY_IDS:
        if "giphy" in bear or bear.startswith("l0"):
            st.markdown(
                f'<iframe src="https://giphy.com/embed/{bear}" width="200" height="200" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>',
                unsafe_allow_html=True
            )
        else:
            st.image(bear, width=200)

    st.markdown("</div style='text-align:center;>", unsafe_allow_html=True)

    # ---- MEMORY GALLERY (images from local images folder) ----
    st.markdown('<p class="gallery-title">💝 Our Memories 💝</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subtitle" style="text-align: center;">Some moments I treasure with you</p>',
        unsafe_allow_html=True,
    )

    # Grid: use all images from images folder (3 columns per row)
    n_images = len(GALLERY_IMAGES)
    if n_images == 0:
        st.info("Add photos to the **images** folder to see them here. 💕")
    else:
        cols_per_row = 3
        for row_start in range(0, n_images, cols_per_row):
            cols = st.columns(cols_per_row)
            for j, col in enumerate(cols):
                with col:
                    idx = row_start + j
                    if idx < n_images:
                        # Display the image without caption
                        st.image(
                            GALLERY_IMAGES[idx],
                            use_container_width=True
                        )

                        # Custom caption with styled color
                        st.markdown(
                            f"<p style='color:#555555; text-align:center;'>Memory {idx + 1} 💕</p>",
                            unsafe_allow_html=True
                        )
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align: center; font-family: Dancing Script, cursive; font-size: 1.5rem; color: #c41e3a;">I love you, LoLo. Happy Valentine\'s Day! 💖</p>',
        unsafe_allow_html=True,
    )
