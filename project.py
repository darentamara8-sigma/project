import streamlit as st

st.set_page_config(
    page_title="My Profile",
    page_icon="👤",
    layout="centered"
)

# Custom styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #eef2ff, #fdf2f8);
    }

    .profile-card {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        margin-top: 20px;
    }

    .profile-title {
        color: #6366f1;
        text-align: center;
    }

    .profile-text {
        font-size: 18px;
        line-height: 1.8;
    }
</style>
""", unsafe_allow_html=True)

st.title("👤 My Profile")
st.write("Tell me a little about yourself!")

st.divider()

# Input form
name = st.text_input("👋 Name")
age = st.number_input("🎂 Age", min_value=1, max_value=120, step=1)
school = st.text_input("🏫 School")
subject = st.text_input("📚 Favorite subject")
hobby = st.text_input("🎨 Favorite hobby")

if st.button("✨ Create My Profile", use_container_width=True):
    if name and school and subject and hobby:
        st.markdown(f"""
        <div class="profile-card">
            <h2 class="profile-title">🌟 Hello, {name}!</h2>
            <div class="profile-text">
                👋 My name is <b>{name}</b>.<br>
                🎂 I am <b>{age}</b> years old.<br>
                🏫 I go to <b>{school}</b>.<br>
                📚 My favorite subject is <b>{subject}</b>.<br>
                🎨 I enjoy <b>{hobby}</b>.
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Please fill in all the fields first! 😊")
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Neon Calculator",
    page_icon="🧮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# PAGE BACKGROUND
# ---------------------------------------------------------

st.markdown("""
<style>

    /* Remove Streamlit default spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 900px;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Background */
    .stApp {
        background:
            radial-gradient(circle at 20% 20%, #14213d 0%, transparent 35%),
            radial-gradient(circle at 80% 80%, #24103d 0%, transparent 35%),
            linear-gradient(135deg, #050509, #0a0a12 50%, #050509);
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.markdown(
    '<div style="text-align:center;margin-bottom:18px;">'
    '<div style="font-size:42px;font-weight:900;letter-spacing:3px;color:#fff;'
    'text-shadow:0 0 5px #00eaff,0 0 15px #00eaff,0 0 30px #0077ff;">'
    '🧮 NEON CALCULATOR'
    '</div></div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# CALCULATOR
# ---------------------------------------------------------

calculator_html = r"""
<!DOCTYPE html>
<html>

<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

* {
    box-sizing: border-box;
    font-family: Arial, Helvetica, sans-serif;
    user-select: none;
}

body {
    margin: 0;
    padding: 10px;
    background: transparent;
}

.calculator {

    width: 100%;
    max-width: 620px;

    margin: auto;

    padding: 22px;

    border-radius: 30px;

    background:
        linear-gradient(
            145deg,
            rgba(25,25,40,0.98),
            rgba(5,5,12,0.98)
        );

    border: 1px solid rgba(0, 234, 255, 0.25);

    box-shadow:
        0 0 20px rgba(0,234,255,0.12),
        0 0 60px rgba(90,0,255,0.12),
        inset 0 0 30px rgba(255,255,255,0.02);

    position: relative;

    overflow: hidden;
}


/* Neon line around calculator */

.calculator::before {

    content: "";

    position: absolute;

    top: -2px;
    left: -2px;
    right: -2px;
    height: 3px;

    background:
        linear-gradient(
            90deg,
            #00eaff,
            #0077ff,
            #a000ff,
            #ff00aa,
            #00eaff
        );

    background-size: 300% 100%;

    animation: neonLine 4s linear infinite;

}

@keyframes neonLine {

    0% {
        background-position: 0%;
    }

    100% {
        background-position: 300%;
    }

}


/* Brand */

.brand {

    display: flex;

    align-items: center;

    gap: 12px;

    margin-bottom: 15px;

}

.logo {

    width: 48px;
    height: 48px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 14px;

    background:
        linear-gradient(
            135deg,
            #00eaff,
            #0066ff
        );

    box-shadow:
        0 0 15px rgba(0,234,255,0.6);

    font-size: 26px;

}

.brand-title {

    color: white;

    font-size: 23px;

    font-weight: bold;

    letter-spacing: 2px;

}

.brand-subtitle {

    color: #5eeeff;

    font-size: 10px;

    letter-spacing: 3px;

    margin-top: 3px;

}


/* Display */

.display {

    background:
        linear-gradient(
            145deg,
            #05070a,
            #10151c
        );

    border-radius: 20px;

    border: 1px solid rgba(0,234,255,0.2);

    padding: 18px;

    margin-bottom: 18px;

    min-height: 120px;

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: flex-end;

    box-shadow:
        inset 0 0 25px rgba(0,0,0,0.9),
        0 0 15px rgba(0,234,255,0.05);

    overflow: hidden;

}

.expression {

    width: 100%;

    text-align: right;

    color: #64717e;

    font-size: 17px;

    min-height: 25px;

    overflow-x: auto;

    white-space: nowrap;

}

.result {

    width: 100%;

    text-align: right;

    color: #ffffff;

    font-size: clamp(30px, 7vw, 50px);

    font-weight: 700;

    letter-spacing: 1px;

    overflow-x: auto;

    white-space: nowrap;

    text-shadow:
        0 0 7px #00eaff,
        0 0 18px rgba(0,234,255,0.5);

}


/* Buttons */

.buttons {

    display: grid;

    grid-template-columns: repeat(4, 1fr);

    gap: 11px;

}


button {

    height: 67px;

    border: none;

    border-radius: 16px;

    background:
        linear-gradient(
            145deg,
            #1c2029,
            #0d1016
        );

    color: #dcecff;

    font-size: 20px;

    font-weight: 600;

    cursor: pointer;

    border: 1px solid rgba(255,255,255,0.06);

    box-shadow:
        0 6px 12px rgba(0,0,0,0.45),
        inset 0 1px 0 rgba(255,255,255,0.04);

    transition:
        transform 0.08s,
        box-shadow 0.15s,
        background 0.15s;

    position: relative;

    overflow: hidden;

}


/* Ripple */

button::after {

    content: "";

    position: absolute;

    width: 10px;

    height: 10px;

    border-radius: 50%;

    background: rgba(255,255,255,0.5);

    transform: scale(0);

    opacity: 0;

    pointer-events: none;

}

button.clicked::after {

    animation: ripple 0.35s ease-out;

}

@keyframes ripple {

    0% {
        transform: scale(0);
        opacity: 0.7;
    }

    100% {
        transform: scale(15);
        opacity: 0;
    }

}


button:hover {

    background:
        linear-gradient(
            145deg,
            #26313d,
            #111822
        );

    box-shadow:
        0 0 12px rgba(0,234,255,0.25),
        0 6px 15px rgba(0,0,0,0.5);

    transform: translateY(-2px);

}

button:active {

    transform:
        translateY(2px)
        scale(0.96);

}


/* Number buttons */

.number {

    color: #ffffff;

}


/* Operators */

.operator {

    color: #00eaff;

    background:
        linear-gradient(
            145deg,
            #102b35,
            #08151b
        );

    border-color:
        rgba(0,234,255,0.25);

}

.operator:hover {

    box-shadow:
        0 0 18px rgba(0,234,255,0.4);

}


/* Equals */

.equals {

    color: white;

    background:
        linear-gradient(
            135deg,
            #0077ff,
            #7a00ff
        );

    box-shadow:
        0 0 15px rgba(0,119,255,0.4),
        0 0 30px rgba(122,0,255,0.25);

}

.equals:hover {

    background:
        linear-gradient(
            135deg,
            #00bfff,
            #9b00ff
        );

    box-shadow:
        0 0 25px rgba(0,234,255,0.6),
        0 0 40px rgba(150,0,255,0.3);

}


/* Clear */

.clear {

    color: #ff5277;

    background:
        linear-gradient(
            145deg,
            #32141e,
            #180b10
        );

    border-color:
        rgba(255,82,119,0.25);

}


/* Backspace */

.back {

    color: #ffb84d;

}


/* Percentage */

.percent {

    color: #bb8cff;

}


/* Zero */

.zero {

    grid-column: span 2;

}


/* History */

.history {

    margin-top: 18px;

    padding-top: 15px;

    border-top:
        1px solid rgba(255,255,255,0.07);

}

.history-title {

    color: #5eeeff;

    font-size: 11px;

    letter-spacing: 3px;

    margin-bottom: 8px;

}

.history-list {

    color: #687581;

    font-size: 13px;

    max-height: 75px;

    overflow-y: auto;

}

.history-item {

    padding: 4px 0;

}


/* Mobile */

@media (max-width: 500px) {

    .calculator {
        padding: 14px;
        border-radius: 22px;
    }

    button {
        height: 58px;
        font-size: 18px;
        border-radius: 13px;
    }

    .display {
        min-height: 105px;
    }

}

</style>

</head>


<body>

<div class="calculator">

    <div class="brand">

        <div class="logo">
            🧮
        </div>

        <div>

            <div class="brand-title">
                NEON CALCULATOR
            </div>

            <div class="brand-subtitle">
                DIGITAL COMPUTATION SYSTEM
            </div>

        </div>

    </div>


    <div class="display">

        <div class="expression" id="expression">
            Ready...
        </div>

        <div class="result" id="result">
            0
        </div>

    </div>


    <div class="buttons">

        <button class="clear" data-value="C">
            C
        </button>

        <button class="back" data-value="BACK">
            ⌫
        </button>

        <button class="percent" data-value="%">
            %
        </button>

        <button class="operator" data-value="/">
            ÷
        </button>


        <button class="number" data-value="7">
            7
        </button>

        <button class="number" data-value="8">
            8
        </button>

        <button class="number" data-value="9">
            9
        </button>

        <button class="operator" data-value="*">
            ×
        </button>


        <button class="number" data-value="4">
            4
        </button>

        <button class="number" data-value="5">
            5
        </button>

        <button class="number" data-value="6">
            6
        </button>

        <button class="operator" data-value="-">
            −
        </button>


        <button class="number" data-value="1">
            1
        </button>

        <button class="number" data-value="2">
            2
        </button>

        <button class="number" data-value="3">
            3
        </button>

        <button class="operator" data-value="+">
            +
        </button>


        <button class="number zero" data-value="0">
            0
        </button>

        <button class="number" data-value=".">
            .
        </button>

        <button class="equals" data-value="=">
            =
        </button>

    </div>


    <div class="history">

        <div class="history-title">
            CALCULATION HISTORY
        </div>

        <div class="history-list" id="history">
            No calculations yet
        </div>

    </div>

</div>


<script>

let current = "";
let expression = "";

const resultDisplay =
    document.getElementById("result");

const expressionDisplay =
    document.getElementById("expression");

const historyDisplay =
    document.getElementById("history");


/* --------------------------------------------------
   SOUND ENGINE
-------------------------------------------------- */

let audioContext = null;


function getAudioContext() {

    if (!audioContext) {

        audioContext =
            new (
                window.AudioContext ||
                window.webkitAudioContext
            )();

    }

    return audioContext;
}


function playClickSound(type = "normal") {

    try {

        const ctx = getAudioContext();

        const oscillator =
            ctx.createOscillator();

        const gain =
            ctx.createGain();

        oscillator.connect(gain);

        gain.connect(ctx.destination);


        if (type === "equals") {

            oscillator.type = "sine";

            oscillator.frequency.setValueAtTime(
                420,
                ctx.currentTime
            );

            oscillator.frequency.exponentialRampToValueAtTime(
                900,
                ctx.currentTime + 0.12
            );

        }

        else if (type === "operator") {

            oscillator.type = "triangle";

            oscillator.frequency.setValueAtTime(
                300,
                ctx.currentTime
            );

            oscillator.frequency.exponentialRampToValueAtTime(
                500,
                ctx.currentTime + 0.07
            );

        }

        else {

            oscillator.type = "sine";

            oscillator.frequency.setValueAtTime(
                650,
                ctx.currentTime
            );

            oscillator.frequency.exponentialRampToValueAtTime(
                350,
                ctx.currentTime + 0.045
            );

        }


        gain.gain.setValueAtTime(
            0.0001,
            ctx.currentTime
        );

        gain.gain.exponentialRampToValueAtTime(
            0.08,
            ctx.currentTime + 0.005
        );

        gain.gain.exponentialRampToValueAtTime(
            0.0001,
            ctx.currentTime + 0.09
        );


        oscillator.start();

        oscillator.stop(
            ctx.currentTime + 0.1
        );

    }

    catch(error) {

        console.log("Audio unavailable");

    }

}


/* --------------------------------------------------
   DISPLAY
-------------------------------------------------- */

function updateDisplay() {

    if (current === "") {

        resultDisplay.innerText = "0";

    }

    else {

        resultDisplay.innerText = current;

    }

    expressionDisplay.innerText =
        expression || "Ready...";

}


/* --------------------------------------------------
   HISTORY
-------------------------------------------------- */

let history = [];


function addHistory(text) {

    history.unshift(text);

    if (history.length > 5) {

        history.pop();

    }

    historyDisplay.innerHTML =
        history
        .map(item =>
            `<div class="history-item">${item}</div>`
        )
        .join("");

}


/* --------------------------------------------------
   CALCULATE
-------------------------------------------------- */

function calculate() {

    if (!current) return;

    try {

        let calculation = current;

        calculation =
            calculation.replace(/%/g, "/100");

        /*
           Only allow calculator characters.
           This prevents arbitrary JavaScript
           from being entered.
        */

        if (!/^[0-9+\-*/().\s]+$/.test(calculation)) {

            throw new Error("Invalid");

        }

        let answer =
            Function(
                '"use strict"; return (' +
                calculation +
                ')'
            )();


        if (!Number.isFinite(answer)) {

            throw new Error("Math error");

        }


        let oldExpression = current;

        let formatted =
            Number.isInteger(answer)
                ? answer.toString()
                : Number(answer.toFixed(10)).toString();


        expression =
            oldExpression + " =";

        current =
            formatted;


        addHistory(
            oldExpression
            .replace(/\*/g, "×")
            .replace(/\//g, "÷")
            + " = "
            + formatted
        );


        playClickSound("equals");

        updateDisplay();

    }

    catch(error) {

        resultDisplay.innerText =
            "ERROR";

        expressionDisplay.innerText =
            "Invalid calculation";

        playClickSound("operator");

        setTimeout(() => {

            current = "";

            expression = "";

            updateDisplay();

        }, 900);

    }

}


/* --------------------------------------------------
   BUTTON PRESS
-------------------------------------------------- */

function press(value, button) {

    button.classList.remove("clicked");

    void button.offsetWidth;

    button.classList.add("clicked");


    /* Clear */

    if (value === "C") {

        current = "";

        expression = "";

        playClickSound();

        updateDisplay();

        return;

    }


    /* Backspace */

    if (value === "BACK") {

        current =
            current.slice(0, -1);

        playClickSound();

        updateDisplay();

        return;

    }


    /* Equals */

    if (value === "=") {

        calculate();

        return;

    }


    /* Percentage */

    if (value === "%") {

        if (current !== "") {

            current += "%";

        }

        playClickSound("operator");

        updateDisplay();

        return;

    }


    /* Operators */

    if (
        value === "+" ||
        value === "-" ||
        value === "*" ||
        value === "/"
    ) {

        if (current === "") {

            return;

        }


        /* Prevent double operators */

        if (/[+\-*/]$/.test(current)) {

            current =
                current.slice(0, -1);

        }


        current += value;

        playClickSound("operator");

        updateDisplay();

        return;

    }


    /* Decimal */

    if (value === ".") {

        let parts =
            current.split(/[+\-*/]/);

        let lastNumber =
            parts[parts.length - 1];


        if (lastNumber.includes(".")) {

            return;

        }

    }


    /* Number */

    current += value;

    playClickSound();

    updateDisplay();

}


/* --------------------------------------------------
   BUTTON EVENTS
-------------------------------------------------- */

document
    .querySelectorAll("button")
    .forEach(button => {

        button.addEventListener(
            "click",
            () => {

                press(
                    button.dataset.value,
                    button
                );

            }
        );

    });


/* --------------------------------------------------
   KEYBOARD SUPPORT
-------------------------------------------------- */

document.addEventListener(
    "keydown",
    function(event) {

        let key =
            event.key;

        let button =
            document.querySelector(
                `button[data-value="${CSS.escape(key)}"]`
            );


        if (
            /^[0-9]$/.test(key) ||
            key === "." ||
            key === "+" ||
            key === "-" ||
            key === "*" ||
            key === "/" ||
            key === "%"
        ) {

            if (button) {

                press(key, button);

            }

            return;

        }


        if (
            key === "Enter" ||
            key === "="
        ) {

            let equals =
                document.querySelector(
                    'button[data-value="="]'
                );

            press("=", equals);

            return;

        }


        if (key === "Backspace") {

            let back =
                document.querySelector(
                    'button[data-value="BACK"]'
                );

            press("BACK", back);

            return;

        }


        if (key === "Escape") {

            let clear =
                document.querySelector(
                    'button[data-value="C"]'
                );

            press("C", clear);

        }

    }
);


/* Initial display */

updateDisplay();

</script>

</body>
</html>
"""


components.html(
    calculator_html,
    height=720,
    scrolling=False
)


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("""
<div style="
    text-align:center;
    margin-top:15px;
    color:#4d5965;
    font-size:11px;
    letter-spacing:2px;
">
    PRESS THE BUTTONS • USE YOUR KEYBOARD • ENJOY THE SOUND
</div>
""", unsafe_allow_html=True)
import streamlit as st


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="centered"
)


# ============================================================
# CUSTOM DESIGN
# ============================================================

st.markdown(
    """
    <style>

    /* =========================
       MAIN PAGE
       ========================= */

    .stApp {
        background:
            radial-gradient(
                circle at 50% -10%,
                rgba(124, 77, 255, 0.18),
                transparent 35%
            ),
            #080a0f;
    }

    .block-container {
        max-width: 820px;
        padding-top: 35px;
        padding-bottom: 60px;
    }


    /* =========================
       TITLE
       ========================= */

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 850;
        letter-spacing: -1.5px;

        background: linear-gradient(
            90deg,
            #8b5cf6,
            #ec4899,
            #38bdf8
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        margin-bottom: 3px;
    }

    .subtitle {
        text-align: center;
        color: #858b9b;
        font-size: 15px;
        margin-bottom: 35px;
    }


    /* =========================
       SECTION HEADERS
       ========================= */

    .section-title {
        font-size: 22px;
        font-weight: 750;
        margin-top: 15px;
        margin-bottom: 15px;
        color: #f4f5f7;
    }


    /* =========================
       INPUTS
       ========================= */

    .stTextInput label,
    .stNumberInput label {
        color: #8e95a5 !important;
        font-size: 13px !important;
    }

    .stTextInput input,
    .stNumberInput input {

        background-color: #171a22 !important;

        color: #f4f5f7 !important;

        border: 1px solid #2c303c !important;

        border-radius: 9px !important;

        height: 42px !important;
    }

    .stTextInput input:focus,
    .stNumberInput input:focus {

        border-color: #8b5cf6 !important;

        box-shadow:
            0 0 0 1px #8b5cf6 !important;
    }


    /* =========================
       NORMAL BUTTONS
       ========================= */

    .stButton button {

        border-radius: 9px;

        background-color: #12151c;

        color: #dfe2e8;

        border: 1px solid #303542;

        font-weight: 600;

        min-height: 42px;

        transition: all 0.18s ease;
    }

    .stButton button:hover {

        border-color: #8b5cf6;

        background-color: #191522;

        color: white;

        transform: translateY(-1px);
    }


    /* =========================
       CALCULATE BUTTON
       ========================= */

    div.stButton > button[kind="primary"] {

        background:
            linear-gradient(
                100deg,
                #7c3aed,
                #db2777
            );

        border: none;

        color: white;

        font-size: 15px;

        font-weight: 750;

        min-height: 48px;

        box-shadow:
            0 8px 25px
            rgba(124, 58, 237, 0.20);
    }

    div.stButton > button[kind="primary"]:hover {

        background:
            linear-gradient(
                100deg,
                #8b5cf6,
                #ec4899
            );

        box-shadow:
            0 10px 30px
            rgba(236, 72, 153, 0.22);
    }


    /* =========================
       METRIC CARDS
       ========================= */

    [data-testid="stMetric"] {

        background:
            linear-gradient(
                145deg,
                #151821,
                #101219
            );

        border:
            1px solid #292e3a;

        border-radius: 13px;

        padding:
            15px 14px;

        min-height: 92px;

        box-shadow:
            0 8px 25px
            rgba(0,0,0,0.18);
    }

    [data-testid="stMetricLabel"] {

        color: #858b9b !important;

        font-size: 12px !important;
    }

    [data-testid="stMetricValue"] {

        color: #f5f6f8 !important;

        font-size: 25px !important;

        font-weight: 750 !important;
    }


    /* =========================
       OVERALL GRADE
       ========================= */

    .grade-container {

        text-align: center;

        background:
            radial-gradient(
                circle at center,
                rgba(236, 72, 153, 0.09),
                transparent 65%
            );

        border:
            1px solid #343946;

        border-radius: 16px;

        padding:
            20px;

        margin-top: 18px;
        margin-bottom: 18px;
    }

    .grade-label {

        color: #858b9b;

        font-size: 13px;
    }

    .grade-number {

        font-size: 62px;

        line-height: 1.05;

        font-weight: 900;

        background:
            linear-gradient(
                135deg,
                #a78bfa,
                #f472b6
            );

        -webkit-background-clip: text;

        -webkit-text-fill-color: transparent;
    }

    .grade-average {

        color: #858b9b;

        font-size: 14px;
    }


    /* =========================
       SUBJECT RESULT
       ========================= */

    .subject-result-box {

        background-color: #11141b;

        border:
            1px solid #282d38;

        border-radius: 10px;

        padding:
            11px 15px;

        margin-bottom: 7px;
    }


    /* =========================
       DIVIDER
       ========================= */

    hr {

        border-color: #252a34;

        margin:
            28px 0;
    }


    /* =========================
       MOBILE
       ========================= */

    @media (max-width: 700px) {

        .block-container {
            padding-left: 18px;
            padding-right: 18px;
        }

        .main-title {
            font-size: 34px;
        }

    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_grade(percentage):

    if percentage >= 90:
        return "A+"

    if percentage >= 85:
        return "A"

    if percentage >= 80:
        return "A-"

    if percentage >= 75:
        return "B+"

    if percentage >= 70:
        return "B"

    if percentage >= 65:
        return "B-"

    if percentage >= 60:
        return "C+"

    if percentage >= 55:
        return "C"

    if percentage >= 50:
        return "C-"

    if percentage >= 45:
        return "D"

    return "F"


def get_gpa(percentage):

    if percentage >= 90:
        return 4.0

    if percentage >= 85:
        return 3.9

    if percentage >= 80:
        return 3.7

    if percentage >= 75:
        return 3.3

    if percentage >= 70:
        return 3.0

    if percentage >= 65:
        return 2.7

    if percentage >= 60:
        return 2.3

    if percentage >= 55:
        return 2.0

    if percentage >= 50:
        return 1.7

    if percentage >= 45:
        return 1.0

    return 0.0


def format_number(number):

    # 85.0 -> 85
    # 85.50 -> 85.5
    # 85.67 -> 85.67

    if number == int(number):
        return str(int(number))

    return f"{number:.2f}".rstrip("0").rstrip(".")


# ============================================================
# TITLE
# ============================================================

st.markdown(
    '<div class="main-title">🎓 Grade Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Calculate your marks, percentage, grade and GPA'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "subjects" not in st.session_state:

    st.session_state.subjects = [
        {
            "name": "Mathematics",
            "marks": 0.0
        },
        {
            "name": "Science",
            "marks": 0.0
        },
        {
            "name": "English",
            "marks": 0.0
        }
    ]


if "results" not in st.session_state:

    st.session_state.results = None


# ============================================================
# SUBJECT HEADER
# ============================================================

st.markdown(
    '<div class="section-title">📚 Your Subjects</div>',
    unsafe_allow_html=True
)


# ============================================================
# SUBJECT INPUTS
# ============================================================

for i in range(
    len(st.session_state.subjects)
):

    # Much tighter column proportions.
    #
    # Before:
    # subject ----------- marks -------- delete
    #
    # Now:
    # subject ---------------- marks -- x

    col_subject, col_marks, col_delete = st.columns(
        [5.4, 2.1, 0.55],
        gap="small"
    )


    # -------------------------
    # SUBJECT NAME
    # -------------------------

    with col_subject:

        st.text_input(
            "Subject",
            value=st.session_state.subjects[i]["name"],
            key=f"subject_name_{i}"
        )


    # -------------------------
    # MARKS
    # -------------------------

    with col_marks:

        st.number_input(
            "Marks",
            min_value=0.0,
            max_value=100.0,
            value=float(
                st.session_state.subjects[i]["marks"]
            ),
            step=0.5,
            key=f"subject_marks_{i}"
        )


    # -------------------------
    # DELETE
    # -------------------------

    with col_delete:

        st.write("")

        if st.button(
            "×",
            key=f"delete_subject_{i}",
            help="Remove subject"
        ):

            if len(
                st.session_state.subjects
            ) > 1:

                st.session_state.subjects.pop(i)

                st.session_state.results = None

                st.rerun()

            else:

                st.warning(
                    "You need at least one subject."
                )


# ============================================================
# UPDATE SUBJECT DATA
# ============================================================

for i in range(
    len(st.session_state.subjects)
):

    st.session_state.subjects[i]["name"] = (
        st.session_state.get(
            f"subject_name_{i}",
            st.session_state.subjects[i]["name"]
        )
    )

    st.session_state.subjects[i]["marks"] = (
        st.session_state.get(
            f"subject_marks_{i}",
            st.session_state.subjects[i]["marks"]
        )
    )


# ============================================================
# ADD / RESET
# ============================================================

col_add, col_reset = st.columns(
    2,
    gap="small"
)


with col_add:

    if st.button(
        "＋ Add Subject",
        use_container_width=True
    ):

        new_subject_number = (
            len(st.session_state.subjects) + 1
        )

        st.session_state.subjects.append(
            {
                "name":
                    f"Subject {new_subject_number}",

                "marks":
                    0.0
            }
        )

        st.session_state.results = None

        st.rerun()


with col_reset:

    if st.button(
        "↻ Reset",
        use_container_width=True
    ):

        st.session_state.subjects = [
            {
                "name": "Mathematics",
                "marks": 0.0
            },
            {
                "name": "Science",
                "marks": 0.0
            },
            {
                "name": "English",
                "marks": 0.0
            }
        ]

        st.session_state.results = None

        st.rerun()


# ============================================================
# CALCULATE BUTTON
# ============================================================

st.write("")

calculate = st.button(
    "⚡ Calculate My Grade",
    type="primary",
    use_container_width=True
)


# ============================================================
# CALCULATE
# ============================================================

if calculate:

    subjects = []

    total_marks = 0.0


    for i in range(
        len(st.session_state.subjects)
    ):

        name = st.session_state.get(
            f"subject_name_{i}",
            ""
        )

        marks = st.session_state.get(
            f"subject_marks_{i}",
            0.0
        )


        # -------------------------
        # CLEAN NAME
        # -------------------------

        name = str(name).strip()

        if name == "":
            name = f"Subject {i + 1}"


        # -------------------------
        # CLEAN MARKS
        # -------------------------

        marks = float(marks)

        marks = max(
            0.0,
            min(
                100.0,
                marks
            )
        )


        subjects.append(
            {
                "name": name,
                "marks": marks
            }
        )


        total_marks += marks


    # ========================================================
    # TOTAL
    # ========================================================

    total_possible = (
        len(subjects) * 100
    )


    # ========================================================
    # PERCENTAGE
    # ========================================================

    if total_possible > 0:

        percentage = (
            total_marks
            /
            total_possible
        ) * 100

    else:

        percentage = 0.0


    # ========================================================
    # GRADE
    # ========================================================

    grade = get_grade(
        percentage
    )


    # ========================================================
    # GPA
    # ========================================================

    gpa = get_gpa(
        percentage
    )


    # ========================================================
    # SAVE
    # ========================================================

    st.session_state.results = {

        "subjects":
            subjects,

        "total":
            total_marks,

        "possible":
            total_possible,

        "percentage":
            percentage,

        "grade":
            grade,

        "gpa":
            gpa
    }


# ============================================================
# RESULTS
# ============================================================

if st.session_state.results is not None:

    result = st.session_state.results


    # ========================================================
    # DIVIDER
    # ========================================================

    st.divider()


    # ========================================================
    # RESULTS TITLE
    # ========================================================

    st.markdown(
        '<div class="section-title">📊 Your Results</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # RESULT CARDS
    # ========================================================

    col1, col2, col3 = st.columns(
        3,
        gap="small"
    )


    # --------------------------------------------------------
    # TOTAL MARKS
    # --------------------------------------------------------

    with col1:

        st.metric(
            "Total Marks",
            (
                f'{format_number(result["total"])}'
                f'/{result["possible"]}'
            )
        )


    # --------------------------------------------------------
    # PERCENTAGE
    # --------------------------------------------------------

    with col2:

        st.metric(
            "Percentage",
            (
                f'{format_number(result["percentage"])}%'
            )
        )


    # --------------------------------------------------------
    # GPA
    # --------------------------------------------------------

    with col3:

        st.metric(
            "GPA",
            f'{result["gpa"]:.2f}/4.0'
        )


    # ========================================================
    # OVERALL GRADE
    # ========================================================

    st.markdown(
        '<div class="grade-container">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="grade-label">'
        'Overall Grade'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="grade-number">'
        f'{result["grade"]}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="grade-average">'
        f'Average: {format_number(result["percentage"])}%'
        f'</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # PERFORMANCE BAR
    # ========================================================

    progress = (
        result["percentage"] / 100
    )

    progress = max(
        0.0,
        min(
            1.0,
            progress
        )
    )

    st.progress(
        progress,
        text=(
            "Overall Performance • "
            f'{format_number(result["percentage"])}%'
        )
    )


    # ========================================================
    # SUBJECT RESULTS
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        '📚 Subject Results'
        '</div>',
        unsafe_allow_html=True
    )


    for subject in result["subjects"]:

        marks = subject["marks"]

        subject_grade = get_grade(
            marks
        )


        col_name, col_result = st.columns(
            [5, 2],
            gap="small"
        )


        with col_name:

            st.markdown(
                '<div class="subject-result-box">',
                unsafe_allow_html=True
            )

            st.write(
                f'**{subject["name"]}**'
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


        with col_result:

            st.markdown(
                '<div class="subject-result-box">',
                unsafe_allow_html=True
            )

            st.write(
                f'**{format_number(marks)}/100 '
                f'· {subject_grade}**'
            )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )
import random
import streamlit as st

# ----------------------------------------------------------------------
# Page setup
# ----------------------------------------------------------------------
st.set_page_config(page_title="Quiz Master", page_icon="🧠", layout="centered")

_WALLPAPER = "data:image/jpeg;base64,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"

st.markdown("""
<style>
/* ==========================================================
   QUIZ MASTER — MODERN DARK / SPACE WALLPAPER
   ========================================================== */

html, body, .stApp, .stMarkdown, p, div, span, label, input, textarea, button {
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
}

html, body, .stApp {
    color: #f5f5f7 !important;
}

/* Full-page wallpaper with a readability overlay */
.stApp {
    background-image:
        linear-gradient(
            180deg,
            rgba(3,3,6,0.42) 0%,
            rgba(3,3,6,0.70) 46%,
            rgba(3,3,6,0.84) 100%
        ),
        radial-gradient(
            circle at 50% 18%,
            rgba(132,92,255,0.17),
            transparent 34%
        ),
        url("__WALLPAPER__") !important;
    background-size: cover !important;
    background-position: center center !important;
    background-attachment: fixed !important;
}

/* Soft vignette / cinematic depth */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background:
        radial-gradient(circle at 50% 40%, transparent 0%, rgba(0,0,0,0.16) 55%, rgba(0,0,0,0.55) 100%);
}

/* Keep the actual Streamlit content above the overlay */
.main, [data-testid="stAppViewContainer"] > section {
    position: relative;
    z-index: 1;
}

.main-title, h1, h2, h3, h4 {
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
    font-weight: 800 !important;
    color: #ffffff !important;
}

.main-title {
    text-align: center;
    font-size: 2rem;
    letter-spacing: 1.5px;
    margin-bottom: 0.35rem;
    text-shadow:
        0 0 12px rgba(184,148,255,0.40),
        0 5px 28px rgba(0,0,0,0.75);
}

.subtitle {
    text-align: center;
    color: #c2c3ce !important;
    font-size: 1.02rem;
    font-weight: 600 !important;
    letter-spacing: 0.2px;
    margin-bottom: 2rem;
}

/* Question cards: translucent glass over the wallpaper */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background:
        linear-gradient(
            145deg,
            rgba(17,16,24,0.79),
            rgba(7,7,12,0.68)
        ) !important;
    border: 1px solid rgba(255,255,255,0.13) !important;
    border-radius: 22px !important;
    padding: 0.85rem 1rem !important;
    box-shadow:
        0 18px 45px rgba(0,0,0,0.34),
        inset 0 1px 0 rgba(255,255,255,0.045);
    backdrop-filter: blur(13px);
    -webkit-backdrop-filter: blur(13px);
    transition:
        transform 0.18s ease,
        border-color 0.18s ease,
        box-shadow 0.18s ease;
}

div[data-testid="stVerticalBlockBorderWrapper"]:hover {
    transform: translateY(-2px);
    border-color: rgba(184,148,255,0.30) !important;
    box-shadow:
        0 22px 55px rgba(0,0,0,0.40),
        0 0 32px rgba(126,88,220,0.10),
        inset 0 1px 0 rgba(255,255,255,0.055);
}

/* Question / choice inputs */
.stTextInput > div > div {
    background: rgba(12,12,18,0.72) !important;
    border: 1px solid rgba(255,255,255,0.11) !important;
    border-radius: 14px !important;
    transition:
        border-color 0.18s ease,
        box-shadow 0.18s ease,
        background 0.18s ease;
}

.stTextInput > div > div:focus-within {
    border-color: rgba(180,150,255,0.72) !important;
    background: rgba(15,14,23,0.86) !important;
    box-shadow:
        0 0 0 3px rgba(171,132,255,0.08),
        0 0 26px rgba(126,88,220,0.10);
}

.stTextInput input {
    color: #f7f6fb !important;
    background: transparent !important;
    font-size: 0.98rem !important;
    font-weight: 600 !important;
    padding: 0.78rem 0.95rem !important;
}

.stTextInput input::placeholder {
    color: #767786 !important;
    font-weight: 500 !important;
}

/* Choice labels sit clearly ABOVE their own input */
.choice-dot {
    display: block !important;
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.3px;
    color: #ddd9ea !important;
    margin: 0.62rem 0 0.34rem 0 !important;
    padding-left: 0.18rem !important;
    line-height: 1.2 !important;
}

.choice-dot + div {
    margin-top: 0 !important;
}

/* Radio choices */
.stRadio > div[role="radiogroup"] {
    gap: 0.55rem !important;
}

.stRadio label {
    background: rgba(255,255,255,0.035) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 13px !important;
    padding: 0.38rem 0.62rem !important;
    font-weight: 650 !important;
    transition:
        border-color 0.18s ease,
        background 0.18s ease,
        transform 0.18s ease;
}

.stRadio label:hover {
    background: rgba(255,255,255,0.055) !important;
    border-color: rgba(184,148,255,0.28) !important;
}

/* Buttons */
.stButton > button,
button[kind="primary"], button[kind="secondary"],
[data-testid="stBaseButton-primary"],
[data-testid="stBaseButton-secondary"] {
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
    font-size: 0.76rem !important;
    font-weight: 800 !important;
    letter-spacing: 0.35px;
    border-radius: 13px !important;
    background:
        linear-gradient(145deg, rgba(24,22,34,0.90), rgba(10,9,15,0.90)) !important;
    color: #f4f2fa !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    padding: 0.72rem 0.9rem !important;
    box-shadow:
        0 8px 24px rgba(0,0,0,0.26),
        inset 0 1px 0 rgba(255,255,255,0.04);
    transition:
        transform 0.16s ease,
        border-color 0.16s ease,
        box-shadow 0.16s ease;
}

.stButton > button:hover,
button[kind="secondary"]:hover,
[data-testid="stBaseButton-secondary"]:hover {
    transform: translateY(-2px);
    border-color: rgba(184,148,255,0.48) !important;
    box-shadow:
        0 13px 30px rgba(0,0,0,0.30),
        0 0 24px rgba(126,88,220,0.10);
}

button[kind="primary"],
[data-testid="stBaseButton-primary"] {
    background:
        linear-gradient(100deg, #6841d8, #b92c78) !important;
    border: none !important;
    color: #ffffff !important;
    box-shadow:
        0 12px 30px rgba(115,66,220,0.22),
        inset 0 1px 0 rgba(255,255,255,0.15);
}

button[kind="primary"]:hover,
[data-testid="stBaseButton-primary"]:hover {
    background:
        linear-gradient(100deg, #8055ed, #d43e8b) !important;
    box-shadow:
        0 15px 36px rgba(115,66,220,0.28),
        0 0 28px rgba(212,62,139,0.12);
}

/* Result cards */
.result-box {
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
    font-size: 0.98rem !important;
    font-weight: 650 !important;
    padding: 1rem 1.1rem;
    border: 1px solid rgba(184,148,255,0.19);
    border-radius: 18px;
    margin-bottom: 0.75rem;
    color: #ffffff !important;
    line-height: 1.6;
    background:
        linear-gradient(
            145deg,
            rgba(18,17,26,0.78),
            rgba(9,9,14,0.74)
        );
    box-shadow:
        0 12px 30px rgba(0,0,0,0.24),
        inset 0 1px 0 rgba(255,255,255,0.035);
    backdrop-filter: blur(11px);
}

.result-box.wrong {
    border-style: solid;
    border-color: rgba(248,113,113,0.28);
    color: #ebe8f0 !important;
}

/* Score / metric cards */
div[data-testid="stMetricValue"] {
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
    font-weight: 800 !important;
    color: #ffffff !important;
    font-size: 1.45rem !important;
}

div[data-testid="stMetricLabel"] {
    font-family: "Inter", "Segoe UI", Arial, sans-serif !important;
    font-weight: 700 !important;
    color: #a9a8b5 !important;
}

/* Alerts / warnings */
div[data-testid="stAlert"] {
    border-radius: 14px !important;
    background: rgba(15,14,21,0.78) !important;
    backdrop-filter: blur(9px);
}

/* Mobile */
@media (max-width: 700px) {
    .main-title {
        font-size: 1.55rem;
    }

    .subtitle {
        font-size: 0.94rem;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 18px !important;
        padding: 0.7rem 0.78rem !important;
    }
}
</style>
""".replace("__WALLPAPER__", _WALLPAPER), unsafe_allow_html=True)


# ----------------------------------------------------------------------
# Easy basic-programming question bank (used to pre-fill new question slots)
# ----------------------------------------------------------------------
QUESTION_BANK = [
    {"question": "Which symbol is used to write a comment in Python?",
     "choices": ["//", "<!-- -->", "#", "**"], "answer": "C"},
    {"question": "Which line correctly creates a variable named age with value 10?",
     "choices": ["age = 10", "var age = 10", "int age = 10;", "10 = age"], "answer": "A"},
    {"question": 'What does print("Hello") do?',
     "choices": ["Nothing", "Shows an error", "Displays the text Hello", "Creates a variable"], "answer": "C"},
    {"question": "Which of these is a whole number (integer)?",
     "choices": ['"5"', "5.0", "5", "True"], "answer": "C"},
    {"question": "Which symbol is used for addition in most languages?",
     "choices": ["+", "&", "-", "%"], "answer": "A"},
    {"question": "Which type of loop repeats code a set number of times?",
     "choices": ["if statement", "for loop", "function", "variable"], "answer": "B"},
    {"question": "What is the file extension for a Python script?",
     "choices": [".py", ".exe", ".txt", ".java"], "answer": "A"},
    {"question": "Which of these stores a list of items, like [1, 2, 3]?",
     "choices": ["String", "List", "Boolean", "Integer"], "answer": "B"},
    {"question": 'What does an "if" statement do?',
     "choices": ["Repeats code forever", "Makes a decision based on a condition",
                 "Stores a number", "Prints text"], "answer": "B"},
    {"question": "A value that is either True or False is called a...",
     "choices": ["String", "Boolean", "Float", "Array"], "answer": "B"},
    {"question": 'Joining "Hello" and "World" into one text is called...',
     "choices": ["Subtraction", "Concatenation", "Division", "Looping"], "answer": "B"},
    {"question": "Which symbol ends a line of code in languages like Java or C++?",
     "choices": [".", ",", ";", ":"], "answer": "C"},
    {"question": "What do we call mistakes in code that stop it from working?",
     "choices": ["Features", "Bugs", "Functions", "Variables"], "answer": "B"},
    {"question": "Which of these is a text (string) data type example?",
     "choices": ["5", "True", '"hello"', "5.5"], "answer": "C"},
    {"question": "What does a function let you do?",
     "choices": ["Store a single number", "Reuse a block of code", "Draw a picture", "Delete files"], "answer": "B"},
]

CHOICE_KEYS = ["a", "b", "c", "d"]


# ----------------------------------------------------------------------
# Callbacks (all session_state mutations happen here, BEFORE widgets
# with the same keys are re-created on the next run)
# ----------------------------------------------------------------------
def init_question_slot(i):
    rq = random.choice(QUESTION_BANK)
    st.session_state[f"q_{i}"] = rq["question"]
    for key, val in zip(CHOICE_KEYS, rq["choices"]):
        st.session_state[f"{key}_{i}"] = val
    st.session_state[f"correct_{i}"] = rq["answer"]


def add_question():
    i = st.session_state.num_questions
    init_question_slot(i)
    st.session_state.num_questions += 1


def remove_last_question():
    if st.session_state.num_questions > 1:
        i = st.session_state.num_questions - 1
        for prefix in ["q", "a", "b", "c", "d", "correct"]:
            st.session_state.pop(f"{prefix}_{i}", None)
        st.session_state.num_questions -= 1


def reroll_question(i):
    init_question_slot(i)


def start_quiz():
    questions = []
    all_filled = True
    for i in range(st.session_state.num_questions):
        q_text = st.session_state.get(f"q_{i}", "")
        a = st.session_state.get(f"a_{i}", "")
        b = st.session_state.get(f"b_{i}", "")
        c = st.session_state.get(f"c_{i}", "")
        d = st.session_state.get(f"d_{i}", "")
        correct = st.session_state.get(f"correct_{i}", "A")
        if not (q_text and a and b and c and d):
            all_filled = False
        questions.append({
            "question": q_text,
            "choices": {"A": a, "B": b, "C": c, "D": d},
            "correct": correct,
        })

    if not all_filled:
        st.session_state.setup_warning = True
        return

    st.session_state.setup_warning = False
    st.session_state.quiz_questions = questions
    st.session_state.quiz_started = True
    st.session_state.user_answers = {}
    st.session_state.submitted = False


def back_to_setup():
    st.session_state.quiz_started = False
    st.session_state.submitted = False


def retry_same_quiz():
    st.session_state.user_answers = {}
    st.session_state.submitted = False


# ----------------------------------------------------------------------
# Session state defaults
# ----------------------------------------------------------------------
st.session_state.setdefault("quiz_started", False)
st.session_state.setdefault("submitted", False)
st.session_state.setdefault("setup_warning", False)
st.session_state.setdefault("quiz_questions", [])
st.session_state.setdefault("user_answers", {})

if "num_questions" not in st.session_state:
    st.session_state.num_questions = 3
    for _i in range(3):
        init_question_slot(_i)

# ----------------------------------------------------------------------
# Header
# ----------------------------------------------------------------------
st.markdown('<div class="main-title">🧠 QUIZ MASTER</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create your own quiz and challenge yourself!</div>', unsafe_allow_html=True)

# ========================================================================
# PHASE 0 — SETUP / BUILDER (editable, can add or remove questions)
# ========================================================================
if not st.session_state.quiz_started:

    add_col, remove_col = st.columns(2)
    with add_col:
        st.button("➕ ADD QUESTION", use_container_width=True, on_click=add_question)
    with remove_col:
        st.button("➖ REMOVE LAST", use_container_width=True, on_click=remove_last_question)

    st.write("")

    for i in range(st.session_state.num_questions):
        with st.container(border=True):
            head_col, rand_col = st.columns([5, 1])
            with head_col:
                st.markdown(f"#### 📝 Question {i + 1}")
            with rand_col:
                st.button("🎲", key=f"rand_{i}", on_click=reroll_question, args=(i,),
                          help="Fill with a random basic-programming question")

            st.text_input("Question", key=f"q_{i}", placeholder="Example: What is the capital of France?")

            col1, col2 = st.columns(2)
            with col1:
                st.markdown('<div class="choice-dot">🔵 Choice A</div>', unsafe_allow_html=True)
                st.text_input("Choice A", key=f"a_{i}", placeholder="Enter choice A", label_visibility="collapsed")
                st.markdown('<div class="choice-dot">🟢 Choice C</div>', unsafe_allow_html=True)
                st.text_input("Choice C", key=f"c_{i}", placeholder="Enter choice C", label_visibility="collapsed")
            with col2:
                st.markdown('<div class="choice-dot">🟡 Choice B</div>', unsafe_allow_html=True)
                st.text_input("Choice B", key=f"b_{i}", placeholder="Enter choice B", label_visibility="collapsed")
                st.markdown('<div class="choice-dot">🔴 Choice D</div>', unsafe_allow_html=True)
                st.text_input("Choice D", key=f"d_{i}", placeholder="Enter choice D", label_visibility="collapsed")

            st.radio("Correct answer", ["A", "B", "C", "D"], key=f"correct_{i}", horizontal=True)

    st.write("")
    st.button("🚀 START QUIZ", use_container_width=True, type="primary", on_click=start_quiz)

    if st.session_state.setup_warning:
        st.warning("⚠️ Please fill in every question and all four choices.")

# ========================================================================
# PHASE 1 — TAKE THE QUIZ
# ========================================================================
elif not st.session_state.submitted:

    for i, q in enumerate(st.session_state.quiz_questions):
        with st.container(border=True):
            st.markdown(f"**Q{i + 1}. {q['question']}**")
            options = [f"{k}. {v}" for k, v in q["choices"].items()]
            picked = st.radio("choose", options, key=f"ans_{i}", label_visibility="collapsed")
            st.session_state.user_answers[i] = picked[0]

    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ SUBMIT", use_container_width=True, type="primary"):
            st.session_state.submitted = True
            st.rerun()
    with col2:
        st.button("✏️ BACK TO SETUP", use_container_width=True, on_click=back_to_setup)

# ========================================================================
# PHASE 2 — RESULTS
# ========================================================================
else:
    score = 0
    total = len(st.session_state.quiz_questions)

    for i, q in enumerate(st.session_state.quiz_questions):
        user_letter = st.session_state.user_answers.get(i)
        correct_letter = q["correct"]
        is_correct = user_letter == correct_letter
        if is_correct:
            score += 1

        if is_correct:
            st.markdown(
                f'<div class="result-box">✅ Q{i + 1}. {q["question"]}<br><br>'
                f'Your answer: {user_letter}. {q["choices"][user_letter]} — Correct!</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f'<div class="result-box wrong">❌ Q{i + 1}. {q["question"]}<br><br>'
                f'Your answer: {user_letter}. {q["choices"][user_letter]}<br>'
                f'Correct answer: {correct_letter}. {q["choices"][correct_letter]}</div>',
                unsafe_allow_html=True,
            )

    st.write("")
    m1, m2 = st.columns(2)
    m1.metric("SCORE", f"{score} / {total}")
    m2.metric("PERCENT", f"{(score / total) * 100:.0f}%" if total else "0%")

    if total and score == total:
        st.balloons()

    col1, col2 = st.columns(2)
    with col1:
        st.button("🔁 RETRY SAME QUIZ", use_container_width=True, type="primary", on_click=retry_same_quiz)
    with col2:
        st.button("✏️ EDIT / NEW QUIZ", use_container_width=True, on_click=back_to_setup)

import random
import streamlit as st


# ============================================================
#                         GUESS ME
#                  CLEAN STREAMLIT VERSION
# ============================================================


# ----------------------------- STATE -------------------------

if "gm_secret" not in st.session_state:
    st.session_state.gm_secret = random.randint(1, 100)

if "gm_attempts" not in st.session_state:
    st.session_state.gm_attempts = 0

if "gm_finished" not in st.session_state:
    st.session_state.gm_finished = False

if "gm_message" not in st.session_state:
    st.session_state.gm_message = "The number is somewhere between 1 and 100."

if "gm_message_type" not in st.session_state:
    st.session_state.gm_message_type = "normal"

if "gm_best" not in st.session_state:
    st.session_state.gm_best = None

if "gm_difficulty" not in st.session_state:
    st.session_state.gm_difficulty = "NORMAL"

if "gm_animation" not in st.session_state:
    st.session_state.gm_animation = ""


DIFFICULTIES = {
    "EASY": 50,
    "NORMAL": 100,
    "HARD": 500
}


# ============================================================
#                         FUNCTIONS
# ============================================================

def reset_game():
    maximum = DIFFICULTIES[st.session_state.gm_difficulty]

    st.session_state.gm_secret = random.randint(1, maximum)
    st.session_state.gm_attempts = 0
    st.session_state.gm_finished = False
    st.session_state.gm_message = (
        f"The number is somewhere between 1 and {maximum}."
    )
    st.session_state.gm_message_type = "normal"
    st.session_state.gm_animation = "enter"


def make_guess(value):
    if st.session_state.gm_finished:
        return

    if value is None or str(value).strip() == "":
        st.session_state.gm_message = "Enter a number first."
        st.session_state.gm_message_type = "error"
        st.session_state.gm_animation = "shake"
        return

    try:
        guess = int(value)
    except (ValueError, TypeError):
        st.session_state.gm_message = "That's not a valid number."
        st.session_state.gm_message_type = "error"
        st.session_state.gm_animation = "shake"
        return

    maximum = DIFFICULTIES[st.session_state.gm_difficulty]

    if guess < 1 or guess > maximum:
        st.session_state.gm_message = (
            f"Choose a number between 1 and {maximum}."
        )
        st.session_state.gm_message_type = "error"
        st.session_state.gm_animation = "shake"
        return

    st.session_state.gm_attempts += 1

    secret = st.session_state.gm_secret

    # TOO LOW
    if guess < secret:
        st.session_state.gm_message = "Too low  ↑  go higher."
        st.session_state.gm_message_type = "hint"
        st.session_state.gm_animation = "shake"

    # TOO HIGH
    elif guess > secret:
        st.session_state.gm_message = "Too high  ↓  go lower."
        st.session_state.gm_message_type = "hint"
        st.session_state.gm_animation = "shake"

    # CORRECT
    else:
        st.session_state.gm_finished = True
        st.session_state.gm_message_type = "win"
        st.session_state.gm_animation = "win"

        old_best = st.session_state.gm_best

        if old_best is None or st.session_state.gm_attempts < old_best:
            st.session_state.gm_best = st.session_state.gm_attempts

            st.session_state.gm_message = (
                f"CORRECT. The number was {secret}.  "
                f"NEW BEST — {st.session_state.gm_attempts} guesses."
            )
        else:
            st.session_state.gm_message = (
                f"CORRECT. The number was {secret}.  "
                f"{st.session_state.gm_attempts} guesses."
            )


# ============================================================
#                            CSS
# ============================================================

st.markdown(
    """
<style>

.gm-card {
    background: rgba(7, 7, 7, 0.96);
    border: 1px solid #292929;
    border-radius: 18px;
    padding: 32px;
    margin-top: 25px;
    margin-bottom: 25px;
    box-shadow: 0 20px 60px rgba(0,0,0,0.55);
}

.gm-title {
    text-align: center;
    color: #eeeeee;
    font-size: 34px;
    font-weight: 800;
    letter-spacing: -1px;
    margin: 0;
}

.gm-subtitle {
    text-align: center;
    color: #666666;
    font-family: monospace;
    font-size: 10px;
    letter-spacing: 2px;
    margin-top: 4px;
}

.gm-range {
    text-align: center;
    color: #eeeeee;
    font-size: 46px;
    font-weight: 800;
    letter-spacing: -2px;
    margin-top: 18px;
}

.gm-question {
    text-align: center;
    color: #777777;
    font-size: 13px;
    margin-top: 3px;
}

.gm-message {
    text-align: center;
    color: #aaaaaa;
    font-family: monospace;
    font-size: 12px;
    margin-top: 17px;
    margin-bottom: 18px;
}

.gm-stat {
    background: #0d0d0d;
    border: 1px solid #292929;
    border-radius: 10px;
    padding: 13px 5px;
    text-align: center;
    transition: 0.2s ease;
}

.gm-stat:hover {
    border-color: #555555;
    transform: translateY(-2px);
}

.gm-stat-label {
    color: #555555;
    font-family: monospace;
    font-size: 8px;
    letter-spacing: 1.5px;
}

.gm-stat-value {
    color: #eeeeee;
    font-family: monospace;
    font-size: 17px;
    font-weight: bold;
    margin-top: 5px;
}

.gm-section {
    text-align: center;
    color: #555555;
    font-family: monospace;
    font-size: 9px;
    letter-spacing: 2px;
    margin-top: 25px;
    margin-bottom: 8px;
}

.gm-card-enter {
    animation: gmEnter 0.5s ease;
}

.gm-card-shake {
    animation: gmShake 0.35s ease;
}

.gm-card-win {
    animation: gmWin 0.65s ease;
}

@keyframes gmEnter {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes gmShake {
    0% { transform: translateX(0); }
    20% { transform: translateX(-7px); }
    40% { transform: translateX(7px); }
    60% { transform: translateX(-5px); }
    80% { transform: translateX(5px); }
    100% { transform: translateX(0); }
}

@keyframes gmWin {
    0% {
        transform: scale(1);
        box-shadow: 0 0 0 rgba(255,255,255,0);
    }
    50% {
        transform: scale(1.015);
        box-shadow: 0 0 35px rgba(255,255,255,0.12);
    }
    100% {
        transform: scale(1);
        box-shadow: 0 0 0 rgba(255,255,255,0);
    }
}

div.stButton > button {
    background: #0d0d0d !important;
    color: #dddddd !important;
    border: 1px solid #303030 !important;
    border-radius: 9px !important;
    transition: all 0.18s ease !important;
}

div.stButton > button:hover {
    background: #181818 !important;
    color: #ffffff !important;
    border-color: #666666 !important;
    transform: translateY(-2px);
}

div.stButton > button:active {
    transform: scale(0.97);
}

div[data-baseweb="input"] {
    background: #080808 !important;
    border-radius: 9px !important;
    border: 1px solid #292929 !important;
}

div[data-baseweb="input"]:focus-within {
    border-color: #666666 !important;
    box-shadow: 0 0 0 1px #666666 !important;
}

input {
    color: #eeeeee !important;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
#                         GAME HEADER
# ============================================================

animation_class = {
    "enter": "gm-card-enter",
    "shake": "gm-card-shake",
    "win": "gm-card-win"
}.get(st.session_state.gm_animation, "")


# IMPORTANT:
# There are NO nested HTML blocks here.
# This prevents the <div> error you were getting.

st.markdown(
    f"""
<div class="gm-card {animation_class}">
<div class="gm-title">GUESS ME</div>
<div class="gm-subtitle">A NUMBER IS WAITING.</div>
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
#                           RANGE
# ============================================================

maximum = DIFFICULTIES[st.session_state.gm_difficulty]

st.markdown(
    f"""
<div class="gm-range">1 — {maximum}</div>
<div class="gm-question">Can you figure it out?</div>
""",
    unsafe_allow_html=True
)


# ============================================================
#                         INPUT AREA
# ============================================================

input_column, button_column = st.columns(
    [3, 1],
    vertical_alignment="bottom"
)


with input_column:

    guess_value = st.text_input(
        "guess_input",
        placeholder="Enter your guess...",
        label_visibility="collapsed",
        key="gm_input"
    )


with button_column:

    pressed_guess = st.button(
        "GUESS",
        use_container_width=True,
        key="gm_guess_button"
    )


if pressed_guess:

    make_guess(guess_value)

    st.session_state.gm_animation = ""

    st.rerun()


# ============================================================
#                           MESSAGE
# ============================================================

if st.session_state.gm_message_type == "win":
    message_color = "#eeeeee"

elif st.session_state.gm_message_type == "error":
    message_color = "#ff6666"

else:
    message_color = "#aaaaaa"


st.markdown(
    f"""
<div class="gm-message" style="color:{message_color};">
{st.session_state.gm_message}
</div>
""",
    unsafe_allow_html=True
)


# ============================================================
#                            STATS
# ============================================================

stat_a, stat_b, stat_c = st.columns(3)


best_display = (
    "—"
    if st.session_state.gm_best is None
    else str(st.session_state.gm_best)
)


with stat_a:

    st.markdown(
        f"""
<div class="gm-stat">
<div class="gm-stat-label">ATTEMPTS</div>
<div class="gm-stat-value">{st.session_state.gm_attempts}</div>
</div>
""",
        unsafe_allow_html=True
    )


with stat_b:

    st.markdown(
        f"""
<div class="gm-stat">
<div class="gm-stat-label">BEST</div>
<div class="gm-stat-value">{best_display}</div>
</div>
""",
        unsafe_allow_html=True
    )


with stat_c:

    st.markdown(
        f"""
<div class="gm-stat">
<div class="gm-stat-label">MODE</div>
<div class="gm-stat-value">{st.session_state.gm_difficulty}</div>
</div>
""",
        unsafe_allow_html=True
    )


# ============================================================
#                         DIFFICULTY
# ============================================================

st.markdown(
    '<div class="gm-section">DIFFICULTY</div>',
    unsafe_allow_html=True
)


easy, normal, hard = st.columns(3)


with easy:

    if st.button(
        "EASY",
        use_container_width=True,
        key="gm_easy"
    ):

        st.session_state.gm_difficulty = "EASY"
        reset_game()
        st.rerun()


with normal:

    if st.button(
        "NORMAL",
        use_container_width=True,
        key="gm_normal"
    ):

        st.session_state.gm_difficulty = "NORMAL"
        reset_game()
        st.rerun()


with hard:

    if st.button(
        "HARD",
        use_container_width=True,
        key="gm_hard"
    ):

        st.session_state.gm_difficulty = "HARD"
        reset_game()
        st.rerun()


# ============================================================
#                         NEW GAME
# ============================================================

st.write("")

if st.button(
    "↻  NEW GAME",
    use_container_width=True,
    key="gm_new_game"
):

    reset_game()
    st.rerun()
