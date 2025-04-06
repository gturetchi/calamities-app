import streamlit as st

from utils.filters import init_sidebar_filters


def init_config() -> None:
    """Initialize the application.
    """
    # Shared page config
    st.set_page_config(
        page_title="Natural Calamities",
        page_icon=":material/globe:",
        layout='wide'
    )

    # Logo
    st.logo("images/logo.png")

    # Page setup
    home_page = st.Page(
        page="views/home.py",
        title="Home",
        icon=":material/home:",
        default=True
    )
    metric_page = st.Page(
        page="views/metric.py",
        title="Metric view",
        icon=":material/percent:"
    )
    table_page = st.Page(
        page="views/table.py",
        title="Table view",
        icon=":material/table:"
    )
    map_page = st.Page(
        page="views/map.py",
        title="Map view",
        icon=":material/map:"
    )
    time_page = st.Page(
        page="views/time.py",
        title="Time view",
        icon=":material/timeline:"
    )

    # Navigation setup
    pg = st.navigation(
        pages=[
            home_page,
            metric_page,
            table_page,
            map_page,
            time_page
        ]
    )
    pg.run()


def app() -> None:
    init_config()
    init_sidebar_filters()

    # Sidebar link

    # st.sidebar.link_button(
    #     ":globe_with_meridians: EM-DAT Project Website",
    #     url="https://www.emdat.be/",
    #     use_container_width=True
    # )
    # st.sidebar.link_button(
    #     ":arrow_down: EM-DAT Data Download",
    #     url="https://public.emdat.be/",
    #     use_container_width=True
    # )
    # st.sidebar.link_button(
    #     ":blue_book: EM-DAT Documentation",
    #     url="https://doc.emdat.be/",
    #     use_container_width=True
    # )

    # st.session_state # uncomment for debugging


app()
