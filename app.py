import streamlit as st

# ====== CONFIG ======
TOTAL = 3
titles = ["haloo syg, Apri ada kejutan nih ☺️", "kira kira apaa yaa 🤭", "satu kali lagi… ✨"]
button_labels = ["klik yaa", "sabarr klik lagi", "terakhir! 😍"]
messages = ["uda makan kan? 🥰", "tetep dijaga terus ya kesehatannyaa"]
FINAL_TEXT = "FROM ME TO U 🤍"

st.set_page_config(page_title="Untuk Kamu", page_icon="🤍", layout="centered")

# ====== STATE ======
if "clicks" not in st.session_state:
    st.session_state.clicks = 0
if "revealed" not in st.session_state:
    st.session_state.revealed = False

# ====== STYLE ======
st.markdown("""
<style>
.biglove{
  text-align:center; font-size:4rem; font-weight:900;
  background:linear-gradient(90deg,#ff4b4b,#ff7ab6);
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  margin: 28px 0 8px 0;
}
.title{ text-align:center; font-size:2rem; font-weight:700; }
.msg{ text-align:center; font-size:1.1rem; color:#444; }

/* surat */
.letter {
  max-width: 720px; margin: 8px auto 0 auto; padding: 16px 20px;
  background: #fff; color:#333; border-radius: 14px;
  box-shadow: 0 8px 24px rgba(255,75,145,.08);
  line-height: 1.7; font-size: 1rem;
}
.letter p { margin: 0 0 10px 0; }

/* fade-in */
.fadein { animation: fadein 1.2s ease-in both; }
@keyframes fadein { from {opacity:0; transform: translateY(6px);} to {opacity:1; transform:none;} }

/* animasi love */
@keyframes fall {
  0% {transform: translateY(-10%) rotate(0deg); opacity:1;}
  100% {transform: translateY(110vh) rotate(360deg); opacity:0;}
}
.love-container {
  position: fixed; inset: 0; pointer-events: none; overflow: hidden;
}
.love {
  position: absolute; top: -10px; font-size: 24px;
  color: #ff4b91; animation: fall linear forwards;
}
</style>
""", unsafe_allow_html=True)

# ====== PLACEHOLDER ======
title_ph = st.empty()
btn_ph = st.empty()
msg_ph = st.empty()
love_ph = st.empty()

# ====== LOGIC ======
if not st.session_state.revealed:
    idx = min(st.session_state.clicks, TOTAL - 1)
    title_ph.markdown(f'<div class="title">{titles[idx]}</div>', unsafe_allow_html=True)

    if btn_ph.button(button_labels[idx], use_container_width=True, key=f"btn_{idx}"):
        st.session_state.clicks += 1
        if st.session_state.clicks >= TOTAL:
            st.session_state.revealed = True
        st.rerun()

    if 0 < st.session_state.clicks < TOTAL:
        msg_ph.info(messages[st.session_state.clicks - 1])

else:
    # sudah reveal
    title_ph.empty(); btn_ph.empty(); msg_ph.empty()
    st.markdown(f'<div class="biglove">{FINAL_TEXT}</div>', unsafe_allow_html=True)

    # kalimat tambahan (surat) — sudah termasuk fade-in
    st.markdown(
        """
        <div class="letter fadein">
          <p>Hm, sampai kapanpun, apri gaakan pernah bosen buat bilang ini ke kamu,
          klo kmu butuh apri bilang ke apri yaa, dan jg cerita kmu itu selalu yg apri nantikan.</p>

          <p>apri sebenernya ga nyangka hubungan kita bakalan jadi sejauh ini, jauh kan ya wkwk,
          wkwk belum belum, iya belum ada setahun wkwk.</p>

          <p>Semakin kmu mengenal apri, semakin banyak hal-hal yang mungkin kmu suka asek.
          Cuma jujur apri ga percaya diri soal itu, karna terkadang apri sulit mengekspreksikan sesuatu.
          Itu yang ngebuat orang lain nganggap apri membosankan, dan bahkan jadi pilihan kedua dan bahkan ga dipilih sama sekali.
          Itu yang terjadi di masa lalu apri.</p>

          <p>Makanya apri bilang ke kamu, klo kamu tertarik sama yang lain, langsung bilang ke apri ya.
          Karna apri gamau kmu meletakkan apri di posisi itu. Ya bukan berarti apri bilang gini apri curiga ke kamu. Engga kok.
          Tenang kalo soal sifat sifat yg gabaik apri rasainnya cuma sebentar. Karna apri langsung cari solusinya dan ngertiin setiap kejadian yang terjadi.</p>

          <p>Rasa takut itu wajar ya. Apri disini takut dan khawatir sama perasaan kmu.
          Iya takut perasaan kmu jadi perlahan terasa membosankan dan menghilangkan rasa bosan itu ke cewe lain.
          Kalau itu terjadi dan memang kmu tertarik sama cewe lain, kmu sama dia aja ya.</p>

          <p>Dan yg lain, klo perasaan kmu perlahan memudar, dan kmu mau sendiri, bilang ke apri ya.</p>

          <p>Tapi dari apri sendiri, apri seneng klo kamu terus mempertahankan perasaan kmu ke apri selama mungkin.
          Dan ya cuma apri pilihan kmu, apri seneng.</p>

          <p>Dan ya apri ga melarang apapun yg memang mau kmu lakuin. Dan apri ga maksa kmu buat ngejaga perasaan apri.
          Tapi apri seneng klo kmu bisa.</p>

          <p>Suatu saat, kalau apri ada nyakitin perasaan kmu atau hal lain yg ngebuat kmu sedih atau marah,
          tolong bilang ke apri ya.</p>

          <p>Intinya apapun itu tolong bilang ke apri ya.</p>

          <p>Makasi ya atas segala hal yang kamu kasi ke apri. 🤍</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # animasi love jatuh
    hearts_html = """
    <div class="love-container">
      """ + "\n".join([
        f'<div class="love" style="left:{i*5}%; animation-duration:{2+i%3}s;">❤️</div>'
        for i in range(24)
      ]) + """
    </div>
    <script>
      const loves = document.querySelectorAll('.love');
      loves.forEach((el,i)=>{
        el.style.left = Math.random()*100+'%';
        el.style.fontSize = (20+Math.random()*34)+'px';
        el.style.animationDuration = (2+Math.random()*3.5)+'s';
        el.style.animationDelay = (Math.random()*2)+'s';
        el.style.color = ['#ff4b91','#ff7ab6','#ff4b4b','#ff77ff'][Math.floor(Math.random()*4)];
      });
    </script>
    """
    love_ph.markdown(hearts_html, unsafe_allow_html=True)
