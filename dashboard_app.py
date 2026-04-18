"""
Task 3 Dashboard (Dash)

Run:
    python dashboard_app.py

Then open:
    http://127.0.0.1:8050
"""

import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html


def load_data() -> pd.DataFrame:
    """
    Load dataset for dashboard.
    Using Plotly's built-in gapminder dataset for reliable local execution.
    """
    return px.data.gapminder()


def build_layout(df: pd.DataFrame) -> html.Div:
    years = sorted(df["year"].unique())
    continents = sorted(df["continent"].unique())

    return html.Div(
        [
            html.H2("Global Trends Dashboard", style={"marginBottom": "8px"}),
            html.P(
                "Explore how GDP per capita, life expectancy, and population vary by year and continent.",
                style={"marginTop": "0", "color": "#4a4a4a"},
            ),
            html.Div(
                [
                    html.Label("Select Year"),
                    dcc.Slider(
                        id="year-slider",
                        min=int(min(years)),
                        max=int(max(years)),
                        step=5,
                        value=int(max(years)),
                        marks={int(y): str(y) for y in years},
                    ),
                ],
                style={"marginBottom": "20px"},
            ),
            html.Div(
                [
                    html.Label("Select Continents"),
                    dcc.Dropdown(
                        id="continent-dropdown",
                        options=[{"label": c, "value": c} for c in continents],
                        value=continents,
                        multi=True,
                        placeholder="Filter by continent",
                    ),
                ],
                style={"marginBottom": "20px"},
            ),
            html.Div(
                [
                    html.Div(id="kpi-countries", className="kpi-card"),
                    html.Div(id="kpi-avg-life", className="kpi-card"),
                    html.Div(id="kpi-avg-gdp", className="kpi-card"),
                ],
                style={
                    "display": "grid",
                    "gridTemplateColumns": "repeat(auto-fit, minmax(170px, 1fr))",
                    "gap": "10px",
                    "marginBottom": "16px",
                },
            ),
            dcc.Graph(id="scatter-graph"),
            dcc.Graph(id="bar-graph"),
        ],
        style={
            "maxWidth": "1100px",
            "margin": "20px auto",
            "padding": "0 12px",
            "fontFamily": "Segoe UI, Arial, sans-serif",
        },
    )


def create_app() -> Dash:
    df = load_data()
    app = Dash(__name__)
    app.title = "Internship Dashboard"
    app.layout = build_layout(df)

    @app.callback(
        [
            Output("scatter-graph", "figure"),
            Output("bar-graph", "figure"),
            Output("kpi-countries", "children"),
            Output("kpi-avg-life", "children"),
            Output("kpi-avg-gdp", "children"),
        ],
        [Input("year-slider", "value"), Input("continent-dropdown", "value")],
    )
    def update_charts(year: int, continents: list[str]):
        selected = continents or sorted(df["continent"].unique())
        filtered = df[(df["year"] == year) & (df["continent"].isin(selected))]

        scatter_fig = px.scatter(
            filtered,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            hover_name="country",
            log_x=True,
            title=f"GDP per Capita vs Life Expectancy ({year})",
        )
        scatter_fig.update_layout(margin=dict(l=20, r=20, t=45, b=20))

        bar_data = (
            filtered.groupby("continent", as_index=False)["lifeExp"]
            .mean()
            .rename(columns={"lifeExp": "avg_lifeExp"})
        )
        bar_fig = px.bar(
            bar_data,
            x="continent",
            y="avg_lifeExp",
            color="continent",
            title=f"Average Life Expectancy by Continent ({year})",
            labels={"avg_lifeExp": "Avg Life Expectancy"},
        )
        bar_fig.update_layout(showlegend=False, margin=dict(l=20, r=20, t=45, b=20))

        country_count = filtered["country"].nunique()
        avg_life = filtered["lifeExp"].mean() if not filtered.empty else 0.0
        avg_gdp = filtered["gdpPercap"].mean() if not filtered.empty else 0.0

        kpi_style = {
            "border": "1px solid #d8d8d8",
            "borderRadius": "8px",
            "padding": "10px 12px",
            "backgroundColor": "#fafafa",
        }
        kpi_label_style = {"fontSize": "12px", "color": "#6a6a6a", "margin": "0"}
        kpi_value_style = {"fontSize": "20px", "fontWeight": "600", "margin": "4px 0 0 0"}

        countries_kpi = html.Div(
            [html.P("Countries", style=kpi_label_style), html.P(f"{country_count}", style=kpi_value_style)],
            style=kpi_style,
        )
        life_kpi = html.Div(
            [html.P("Avg Life Expectancy", style=kpi_label_style), html.P(f"{avg_life:.2f}", style=kpi_value_style)],
            style=kpi_style,
        )
        gdp_kpi = html.Div(
            [html.P("Avg GDP per Capita", style=kpi_label_style), html.P(f"${avg_gdp:,.0f}", style=kpi_value_style)],
            style=kpi_style,
        )

        return scatter_fig, bar_fig, countries_kpi, life_kpi, gdp_kpi

    return app


if __name__ == "__main__":
    dashboard_app = create_app()
    dashboard_app.run(debug=True, port=8050)
