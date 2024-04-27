import reflex as rx

from rashed_portfolio.ui.global_components.nav_bar import navbar
from rashed_portfolio.ui.pages.home.components.banner import home_banner


def index() -> rx.Component:
    return rx.fragment(
        navbar(active_item='Home'),
        home_banner(),
    )
