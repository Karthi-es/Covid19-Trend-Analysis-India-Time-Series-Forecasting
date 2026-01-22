# Covid-19 Trend Analysis & Time-Series Forecasting

This repository contains an end-to-end exploration of the Covid-19 situation in India. It covers data cleaning, exploratory analysis, state-wise visualization through an interactive Dash dashboard, and a Support Vector Machine (SVM) based time-series experiment for forecasting confirmed cases.

## Highlights
- Consolidated and cleaned publicly available case, vaccination, and testing data.
- Interactive dashboard to inspect confirmed, recovered, and death trends for every Indian state and union territory.
- Time-series modelling notebook that demonstrates an SVM regression baseline for confirmed case forecasting.

## Data
The repository already ships with the CSV files needed to reproduce the results:
- `Covid19 Final Data.csv`: curated master table used by the dashboard.
- `covid_19_india.csv`, `covid_vaccine_statewise.csv`, `StatewiseTestingDetails.csv`: raw sources used inside the notebook for feature engineering.

## Prerequisites
- Python 3.10+ (project tested with 3.13.2 on Windows 11).
- Git (for cloning) and a modern browser (for the dashboard).

## Setup
1. **Clone**
	```bash
	git clone https://github.com/Karthi-es/Covid19-Trend-Analysis-India-Time-Series-Forecasting.git
	cd Covid-19-Trend-Analysis-India-Time-Series-Forecasting-main
	```
2. **Create & activate a virtual environment**
	```bash
	python -m venv .venv
	# Windows
	.venv\Scripts\activate
	# macOS / Linux
	source .venv/bin/activate
	```
3. **Upgrade pip (optional but recommended)**
	```bash
	python -m pip install --upgrade pip
	```

## Install Dependencies
Install the pinned package versions that match the latest 2026-compatible wheels observed during development:

```bash
pip install \
	 pandas==3.0.0 \
	 numpy==2.4.1 \
	 matplotlib==3.10.8 \
	 plotly==6.5.2 \
	 seaborn==0.13.2 \
	 dash==3.4.0 \
	 scikit-learn==1.8.0
```

> These exact versions ensure compatibility with Python 3.13. Feel free to relax the pins if you are running an older interpreter—just keep pandas ≥1.3, numpy ≥1.20, and scikit-learn ≥1.0.

## Running the Dash Dashboard
1. Verify the CSV files remain in the project root (especially `Covid19 Final Data.csv`).
2. Launch the server:
	```bash
	python Covid-19_Dashboard.py
	```
3. Open the URL printed in the terminal (defaults to http://127.0.0.1:8050/) and use the state dropdown to explore the trends.

### Common Flags
- `python Covid-19_Dashboard.py --port 8080` (edit the script if you need a custom port).
- Set `debug=False` inside `app.run_server` when deploying to production.

## Working with the Notebook
The exploratory notebook `Covid-19_Trend_Analysis.ipynb` contains data wrangling and the SVM time-series experiment.

1. Activate the virtual environment.
2. Install Jupyter (if not already available):
	```bash
	pip install notebook
	```
3. Launch Jupyter and open the notebook:
	```bash
	jupyter notebook
	```
4. Run the cells sequentially. Ensure the CSV files remain relative to the notebook so the default paths resolve.

## Project Structure
- `Covid-19_Dashboard.py` – Dash application for interactive visualization.
- `Covid-19_Trend_Analysis.ipynb` – Data preparation and forecasting experiment.
- `Covid19 Final Data.csv` – Main dataset consumed by the dashboard.
- `covid_19_india.csv`, `covid_vaccine_statewise.csv`, `StatewiseTestingDetails.csv` – Supplemental raw datasets.

## Troubleshooting
- **Missing wheels on Windows**: Ensure you are on Python 3.10+; older versions may not have pre-built wheels for pandas/numpy.
- **Dash server not reachable**: Check that the terminal shows “Running on http://127.0.0.1:8050/”; firewalls or already-bound ports can block it. Change the port via `app.run_server(port=XXXX)`.
- **Encoding errors while reading CSVs**: Pass `encoding="utf-8"` to `pd.read_csv` if you customize file paths.

## Contributing
Pull requests are welcome. Please open an issue first to discuss significant changes or new features. Remember to format code with `black` or your preferred formatter and include screenshots when altering dashboard visuals.
