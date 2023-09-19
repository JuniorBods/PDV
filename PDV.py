from streamlit_card import card
from streamlit_extras.grid import grid
import streamlit as st



n = 1
def cards():
    
    # my_grid = grid(n,5,5,5, vertical_align="center", gap="small")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        card(
            title="Card 1",
            text="Card 1",
            
        )
        card(
            title="Card 6",
            text="Card 3",
        )
    
    with col2:
        card(
            title="Card 2",
            text="Card 2",
        )
        card(
            title="Card 5",
            text="Card 3",
        )

        
    with col3:
        card(
            title="Card 3",
            text="Card 3",
        )
        card(
            title="Card 4",
            text="Card 4",
        )