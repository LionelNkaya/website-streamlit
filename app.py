import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")
img_sharehub = Image.open("images/shareHub.png")
img_rqm = Image.open("images/rqm.png")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Lionel :wave:")
    st.title("A Software Solution Builder")
    st.write(
        "My goal is to build applications that allow information to be shared and great ideas to scale."
    )

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            - I build automation tools that allow high producers in comapnies to produce even more.
            - I analyse data.
            - I build education ressources and train users on new tools.
            - I write documentation for other developers.
            - I use low code tools, to build data over forms apps.
            - I build for the web with HTML, CSS, JS and SQL, Python & PHP on the back end.

            """
        )

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_sharehub)
    with text_column:
        st.subheader("[shareHub](https://sharehub.lionelnkaya.com)")
        st.write(
            """
            When you share with shareHub, we use the Facebook and Twitter API so that you can share your ideas with the world without loosing innumerable hours logged in  to your social media accounts scrolling through content.
            """
        )
        st.markdown("[Code Repo](https://github.com/LionelNkaya/shareHub)")

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_rqm)
    with text_column:
        st.subheader("[Random Quote Machine](https://randomquotemachine.lionelnkaya.com)")
        st.write(
            """
            Press the button and receive encouragement in the LORD. Possibility to post the Bible quote to your Tweeter account.
            """
        )
        st.markdown("[Code Repo](https://github.com/LionelNkaya/RandomQuoteMachine)")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! PUT YOUR OWN EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/c478058a3427fc24b2d171982039ca60" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
