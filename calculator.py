import streamlit as st #used to create ui(text,buttons)
import math

#“Set the configuration of the app page”
st.set_page_config(page_title=" Calculator",
                   page_icon="🔥")



if "expr" not in st.session_state:
    st.session_state.expr = ""

def add(val):
    st.session_state.expr += str(val)

def clear():
    st.session_state.expr = ""

def calculate():
    try:
        expression = st.session_state.expr
        
        expression = expression.replace("π", str(math.pi))
        expression = expression.replace("e", str(math.e))
        expression = expression.replace("^", "**")

        
        result = eval(expression, {"__builtins__": None}, {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
            "fact": math.factorial
        })

        st.session_state.expr = str(result)

    except:
        st.session_state.expr = "Error"


st.title("🧮 Advanced Scientific Calculator")

st.text_input("Display", value=st.session_state.expr, disabled=True)


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button("7", on_click=add, args=("7",))
    st.button("4", on_click=add, args=("4",))
    st.button("1", on_click=add, args=("1",))
    st.button("0", on_click=add, args=("0",))

with col2:
    st.button("8", on_click=add, args=("8",))
    st.button("5", on_click=add, args=("5",))
    st.button("2", on_click=add, args=("2",))
    st.button(".", on_click=add, args=(".",))

with col3:
    st.button("9", on_click=add, args=("9",))
    st.button("6", on_click=add, args=("6",))
    st.button("3", on_click=add, args=("3",))
    st.button("+", on_click=add, args=("+",))

with col4:
    st.button("/", on_click=add, args=("/",))
    st.button("*", on_click=add, args=("*",))
    st.button("-", on_click=add, args=("-",))
    st.button("=", on_click=calculate)

st.markdown("### Scientific")

col5, col6, col7, col8 = st.columns(4)

with col5:
    st.button("sin", on_click=add, args=("sin(",))
    st.button("cos", on_click=add, args=("cos(",))

with col6:
    st.button("tan", on_click=add, args=("tan(",))
    st.button("log", on_click=add, args=("log(",))

with col7:
    st.button("ln", on_click=add, args=("ln(",))
    st.button("√", on_click=add, args=("sqrt(",))

with col8:
    st.button("π", on_click=add, args=("π",))
    st.button("e", on_click=add, args=("e",))


st.markdown("### Advanced")

col9, col10, col11, col12 = st.columns(4)

with col9:
    st.button("^", on_click=add, args=("^",))
    st.button("x²", on_click=add, args=("**2",))

with col10:
    st.button("x³", on_click=add, args=("**3",))
    st.button("1/x", on_click=add, args=("1/(",))

with col11:
    st.button("fact", on_click=add, args=("fact(",))
    st.button("(", on_click=add, args=("(",))

with col12:
    st.button(")", on_click=add, args=(")",))
    st.button("Clear", on_click=clear)

