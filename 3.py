import streamlit as B
B.set_page_config(page_title="Sea", page_icon="🐬🦐🦑", layout="wide")
B.title("Ласкаво просимо до мого додатку!")
tab1, tab2, tab3 = B.tabs  (["About me", "My instrument", "Корисні посилання"])
with tab1:
    B.header("Знайомство з автором")
    C1, C2=B.columns([1, 2])
    with C1:
        B.image("https://thumbs.dreamstime.com/b/2-193155720.jpg?w=768")
    with C2:
        B.subheader("Привіт, я майбутній розробник ігор!")
        B.write("Я навчаюсь в МКА IT Step і проходив  курси Roblox Studio і Kodu.")
        with B.container():
            B.info("Контакти для зв'язку")
            B.markdown("- GitHub: [Мій профіль](https://github.com)")
            B.markdown("- E-mail: rosrobnykrosrobnykiv@itstep.org")
with tab2:
    B.info("У процесі розробки")
with tab3:
    B.header("Корисні посилання")
    C3, C4 = B.columns([1, 2])
    with C3:
        B.image("https://thumbs.dreamstime.com/b/2-193155720.jpg?w=768")
    with C4:
        B.subheader("Я часто звертаюсь до цих сайтів.")
        B.write("Там я можу задовільнити свої хобі.")
        with B.container():
            B.info("Посилання")
            B.markdown("♟️ Lichess: [Шахи](https://lichess.org/)")
            B.markdown("🚴‍♀️ Veloland: [Веломагазин](https://velo-land.com.ua/)")
            B.markdown("🏄️ Хороший відпочинок: [Тур-агенство](https://xo.ua/)")
            B.markdown("🖍️ Епіцентрк: [Магазин кантоварів](https://epicentrk.ua/)")
            B.markdown("- E-mail: rosrobnykrosrobnykiv@itstep.org")