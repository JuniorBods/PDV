import streamlit as st
from streamlit_extras.grid import grid

from datetime import datetime, timedelta



def dashboard():
    my_grid = grid(1, 4, [2, 4, 1], 1, 4, vertical_align="bottom")
    # Row 1:
    data = datetime.today().date()
    my_grid.date_input("Selecione uma Data", value=(data-timedelta(days=6), data), format="DD/MM/YYYY")
   # Row 2:
    mes1 = {
    "totaldevendas" : 1450.00,
    "lucrobruto" : 1000.50,
    "custoproduto" : 581.50,
    "ticketmedio" : 30.25}
    
    mes2 ={
    "totaldevendas" : 2501.00,
    "lucrobruto" : 528.66,
    "custoproduto" : 1700.35,
    "ticketmedio" : 45.25}
    
    
    
    # Lista de métricas
    metricas = ["totaldevendas", "lucrobruto", "custoproduto", "ticketmedio"]
    metricas_nome = ["Total de Vendas", "Lucro Bruto", "Custo de Produto", "Ticket Médio"]

    # Calcular a diferença percentual para cada métrica usando um loop for
    for metrica, nome in zip(metricas, metricas_nome):
        dif_percentual = ((mes2[metrica] - mes1[metrica]) / mes1[metrica]) * 100
        print(f"Diferença percentual para {metrica.capitalize()}: {dif_percentual:.2f}%")
    
        my_grid.metric(label=nome, value=mes2[metrica], delta=f"{dif_percentual:.2f}"+"%")

    # Row 2:
    my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    my_grid.text_input("Your name")
    my_grid.button("Send", use_container_width=True)
    # Row 3:
    my_grid.text_area("Your message", height=40)
    # Row 4:
    my_grid.dataframe(random_df, use_container_width=True)
    my_grid.line_chart(random_df, use_container_width=True)
    # Row 5 (uses the spec from row 1):
    with my_grid.expander("Show Filters", expanded=True):
        st.slider("Filter by Age", 0, 100, 50)
        st.slider("Filter by Height", 0.0, 2.0, 1.0)
        st.slider("Filter by Weight", 0.0, 100.0, 50.0)
    my_grid.dataframe(random_df, use_container_width=True)