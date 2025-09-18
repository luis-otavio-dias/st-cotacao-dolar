import requests
import streamlit as st
import pandas as pd


def main():
    data = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL").json()
    url = "https://docs.awesomeapi.com.br/api-de-moedas"

    first_col, second_col = [], []

    for key, value in data["USDBRL"].items():
        first_col.append(key)
        second_col.append(value)

    st.title("Cotação do Dólar")
    st.markdown(
        """
        Aplicativo para consultar informações da cotação do dólar em tempo real
        usando a API de Cotações de [**AwesomeAPI**](%s).
        """
        % url
    )
    st.markdown("### Dados da Cotação do Dólar")
    st.write(
        pd.DataFrame(
            {
                "key": first_col,
                "value": second_col,
            },
        )
    )


if __name__ == "__main__":
    main()
