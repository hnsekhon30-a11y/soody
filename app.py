import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Open Me 💌", layout="centered")

components.html(
"""
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background: #f8cdd1;
  margin: 0;
  overflow: hidden;
  font-family: Arial, sans-serif;
}

/* Full-page glitter */
.glitter {
  position: fixed;
  inset: 0;
  background:
    radial-gradient(circle, rgba(255,255,255,0.7) 1px, transparent 1px),
    radial-gradient(circle, rgba(255,105,180,0.8) 1px, transparent 1px);
  background-size: 35px 35px;
  animation: sparkle 2.5s linear infinite;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.6s;
}

@keyframes sparkle {
  from { background-position: 0 0, 20px 20px; }
  to   { background-position: 35px 35px, 55px 55px; }
}

/* Center wrapper */
.center {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Envelope */
.envelope {
  width: 300px;
  height: 200px;
  background: #ff9aa2;
  border-radius: 12px;
  cursor: pointer;
  position: relative;
}

.envelope::before {
  content: "";
  position: absolute;
  top: 0;
  border-left: 150px solid transparent;
  border-right: 150px solid transparent;
  border-top: 100px solid #ff6f91;
  transform-origin: top;
  transition: transform 0.8s;
}

.envelope.open::before {
  transform: rotateX(180deg);
}

.open-text {
  color: white;
  font-size: 22px;
  font-weight: bold;
  text-align: center;
  margin-top: 80px;
}

/* Question card */
.card {
  display: none;
  background: #fff0f5;
  padding: 40px;
  border-radius: 28px;
  text-align: center;
  width: 400px;
  box-shadow: 0 0 40px rgba(255,105,180,0.7);
  animation: fadeUp 1s ease forwards;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(50px); }
  to   { opacity: 1; transform: translateY(0); }
}

#yes {
  background: #ff3b6c;
  color: white;
  border: none;
  padding: 15px 36px;
  border-radius: 30px;
  font-size: 18px;
  cursor: pointer;
  transition: transform 0.3s;
}

#yes:hover {
  transform: scale(1.25);
}

#no {
  position: absolute;
  background: #ffd1dc;
  border: none;
  padding: 10px 25px;
  border-radius: 20px;
  cursor: pointer;
}

.buttons {
  margin-top: 30px;
  position: relative;
  height: 80px;
}

.small {
  font-size: 12px;
  color: #c2185b;
  margin-top: 15px;
}
</style>
</head>

<body>

<div class="glitter" id="glitter"></div>

<div class="center">

  <div id="envelope" class="envelope" onclick="openEnvelope()">
    <div class="open-text">Open Me 💌</div>
  </div>

  <div id="card" class="card">
    <div style="font-size:42px;">👩🏻👨🏻💖</div>
    <h2>Soody, would you make me the happiest person and be my Valentine? 🥺💗</h2>

    <div class="buttons">
      <button id="yes" onclick="accept()">Yes</button>
      <button id="no">No</button>
    </div>

    <div class="small">The “No” button is feeling shy 😈</div>
  </div>

</div>

<script>
function openEnvelope() {
  document.getElementById("envelope").classList.add("open");

  setTimeout(() => {
    document.getElementById("envelope").style.display = "none";
    document.getElementById("glitter").style.opacity = "1";
  }, 600);

  setTimeout(() => {
    document.getElementById("card").style.display = "block";
  }, 1600);
}

const noBtn = document.getElementById("no");

noBtn.addEventListener("mouseover", () => {
  const x = Math.random() * 260;
  const y = Math.random() * 40;
  noBtn.style.left = x + "px";
  noBtn.style.top = y + "px";
});

function accept() {
  document.getElementById("card").innerHTML = `
    <h2 style="font-size:34px;">Officially my favourite YES ever 💖✨</h2>
    <p>No refunds. You’re my Valentine now 💌</p>
  `;
}
</script>

</body>
</html>
""",
height=750,
)

