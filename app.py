
import streamlit as st

st.set_page_config(
    page_title="Virtual pH Testing Lab",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 Virtual pH Testing Laboratory")
st.write("Explore acids, bases and neutral solutions through interactive experiments.")

st.divider()

solutions = {
    "Lemon Juice": 2.0,
    "Vinegar": 2.5,
    "Orange Juice": 3.5,
    "Coffee": 5.0,
    "Milk": 6.5,
    "Pure Water": 7.0,
    "Baking Soda Solution": 8.3,
    "Soap Solution": 10.0
}

st.header("🔬 Experiment 1: Test a Solution")

selected = st.selectbox(
    "Choose a chemical solution:",
    list(solutions.keys())
)

ph = solutions[selected]

if ph < 7:
    nature = "Acidic"
    colour = "Red / Orange"
elif ph == 7:
    nature = "Neutral"
    colour = "Green"
else:
    nature = "Basic"
    colour = "Blue / Purple"

c1, c2, c3 = st.columns(3)

c1.metric("pH Value", ph)
c2.metric("Nature", nature)
c3.metric("Indicator Colour", colour)

if nature == "Acidic":
    st.error("The selected solution is acidic.")
elif nature == "Neutral":
    st.success("The selected solution is neutral.")
else:
    st.info("The selected solution is basic.")

st.divider()

st.header("🌈 Visual pH Scale")

st.caption("The pH scale ranges from 0 to 14.")

st.progress(ph / 14)

c1, c2, c3 = st.columns(3)
c1.write("🔴 Acidic: Below 7")
c2.write("🟢 Neutral: 7")
c3.write("🔵 Basic: Above 7")

st.divider()

st.header("📋 Experiment Observation")

st.write("Selected solution:", selected)
st.write("pH value:", ph)
st.write("Classification:", nature)
st.write("Indicator colour:", colour)

st.caption(
    "Note: These are illustrative educational values, "
    "not actual laboratory measurements."
)

st.divider()

st.header("📚 Learn Chemistry")

with st.expander("What is pH?"):
    st.write("pH measures how acidic or basic an aqueous solution is.")

with st.expander("What are acids?"):
    st.write("Acids have a pH below 7. Example: Lemon juice.")

with st.expander("What are bases?"):
    st.write("Bases have a pH above 7. Example: Baking soda solution.")

with st.expander("What is neutral?"):
    st.write("A neutral solution has a pH of 7. Example: Pure water.")

st.divider()

st.header("📝 Knowledge Quiz")

answer = st.radio(
    "What is the pH of pure water at approximately room temperature?",
    ["2", "5", "7", "10"],
    key="quiz"
)

if st.button("Check Answer"):
    if answer == "7":
        st.success("Correct! Excellent work!")
    else:
        st.warning("Try again! The correct pH is 7.")

st.divider()

st.caption("Virtual Chemistry Laboratory | Learning Through Experiments")
