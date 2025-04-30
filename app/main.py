import streamlit as st
from generator import generate_mixed_distribution
from visualizer import plot_histogram, plot_sorted
from utils import load_config, save_config_json

import pandas as pd
import json

st.set_page_config(page_title='Генератор чисел и анализ данных', page_icon='👋', layout='wide')

page = st.sidebar.selectbox("Выберите страницу", ["Генератор чисел", "О разработчике"])

if page == "О разработчике":
    st.markdown("# Генератор чисел с композицией двух линейных распределений\n\n## Информация о разработчике")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**ФИО:** Мингазов Тимур Рафаэлевич  \n**Номер учебной группы:** ИВТ-222")
    with col2:
        st.markdown(
            "**О наборе данных:**  \n"
            "Данный проект реализует генерацию чисел с использованием композиции двух линейных распределений.  \n"
            "Пользователь может задать параметры, визуализировать и сохранить результат.  \n"
            "Также реализована возможность загрузки конфигурационного файла для воспроизведения ранее сохранённых параметров генерации."
        )

elif page == "Генератор чисел":
    st.title("Генератор случайных чисел")

    st.subheader("Импорт параметров из JSON")
    config_file = st.file_uploader("Загрузите JSON с параметрами генерации", type=['json'])
    config_data = load_config(config_file)

    st.subheader("Настройки генерации")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Первое распределение**")
        a1 = st.number_input("a1", value=config_data.get('a1', 1.0))
        b1 = st.number_input("b1", value=config_data.get('b1', 0.0))

    with col2:
        st.markdown("**Второе распределение**")
        a2 = st.number_input("a2", value=config_data.get('a2', -1.0))
        b2 = st.number_input("b2", value=config_data.get('b2', 1.0))

    with col3:
        st.markdown("**Общие настройки**")
        xmin = st.number_input("xmin", value=config_data.get('xmin', 0.0))
        xmax = st.number_input("xmax", value=config_data.get('xmax', 1.0))
        w = st.slider("Вес первого распределения (w)", 0.0, 1.0, config_data.get('w', 0.5))
        N = st.number_input("Количество чисел (N)", min_value=1, max_value=1000000, value=int(config_data.get('N', 1000)), step=1)

    if xmin >= xmax:
        st.error("Ошибка: xmin должен быть < xmax")
    else:
        samples = generate_mixed_distribution(a1, b1, a2, b2, xmin, xmax, w, N)
        df = pd.DataFrame(samples, columns=['value'])

        st.subheader("Первые 20 значений")
        st.write(df.head(20))

        st.subheader("Гистограмма")
        st.pyplot(plot_histogram(df), use_container_width=True)

        st.subheader("Упорядоченные значения")
        st.pyplot(plot_sorted(df), use_container_width=True)

        st.markdown("---")

        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("Скачать CSV", data=csv, file_name='samples.csv', mime='text/csv')

        json_data = save_config_json(a1, b1, a2, b2, xmin, xmax, w, N)
        st.download_button("Скачать параметры генерации (JSON)", data=json_data, file_name='settings.json', mime='application/json')

        st.info("Генерация и экспорт завершены.")
