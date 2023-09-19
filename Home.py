import streamlit as st
from streamlit_extras.grid import grid
from streamlit_extras.keyboard_url import keyboard_to_url
from markdownlit import mdlit
from streamlit_extras.metric_cards import style_metric_cards

from streamlit_extras.stodo import to_do
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.tags import tagger_component
from streamlit_option_menu import option_menu
from DashboardVendas import dashboard
from CadastroProduto import produtos
from PDV import cards

def main():
    

    with st.sidebar:
        logo = st.sidebar.image("pdv2.png", width=200)
        escolha = option_menu(
        menu_title = "Menu",
        options = ["Dashboard","PDV","Clientes","Produtos"],
        icons = ["bar-chart","cart4","people","boxes"],
        menu_icon = "cast",
        default_index = 0,)
    
    if escolha == "Dashboard":
        dashboard()
 
    if escolha == "PDV":
        cards()

    if escolha == "Clientes":
        pass
    
    if escolha == "Produtos":
        produtos()



if __name__ == '__main__':
    main()