from flask import Flask, render_template
import os, folium
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


woj = os.path.join('data', 'pl_woj.geojson')
woj_density = os.path.join('data', 'pl_ppl_density.csv')
woj_density_data = pd.read_csv(woj_density)
woj_graduates = os.path.join('data', 'pl_graduates.csv')
woj_graduates_data = pd.read_csv(woj_graduates)


@app.route('/pl-woj-density')
def pl_density():
    map = folium.Map(
        location=[52.06, 19.48],
        zoom_start=6,
    )
    folium.Choropleth(
        geo_data=woj,
        name="choropleth",
        data=woj_density_data,
        columns=["Wojewodztwo", "Gestosc"],
        key_on="feature.id",
        fill_color="YlGn",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Gęstość zaludnienia [os./km2] (2020 r.)",
    ).add_to(map)

    return map._repr_html_()


@app.route('/pl-woj-graduates')
def pl_graduates():
    map = folium.Map(
        location=[52.06, 19.48],
        zoom_start=6,
    )
    folium.Choropleth(
        geo_data=woj,
        name="choropleth",
        data=woj_graduates_data,
        columns=["Wojewodztwo", "Absolwenci"],
        key_on="feature.id",
        fill_color="BuPu",
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name="Absolwenci uczelni na 10 tys. ludności (2020 r.)",
    ).add_to(map)

    return map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
