# Data-Profiler-with-Streamlit
An interactive Streamlit web app that lets you upload datasets and generate data profiling reports instantly.

It supports **CSV and Excel files**, and provides insights into distributions, correlations, missing values, and more — all inside your browser.

---

## ✨ Features

* 📂 Upload `.csv` and `.xlsx` files (up to **10 MB**)
* 📑 Select sheets when uploading Excel files
* ⚡ Generate **detailed** or **minimal** profiling reports
* 🎨 Switch between **Primary**, **Dark**, and **Orange** themes
* 🔍 Explore statistics, distributions, correlations, missing data, and more

---

## 🛠 Tech Stack

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Pandas](https://pandas.pydata.org/)
* [pandas-profiling==3.6.6](https://github.com/ydataai/pandas-profiling)
* [streamlit-pandas-profiling](https://github.com/pablocFonseca/streamlit-pandas-profiling)

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com//data-profiler-with-.git
cd data-profiler
```

### 2. Create & Activate Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```


---

## 📌 Notes

* This project uses `pandas-profiling==3.6.6` to enable **Dark** and **Orange** themes.
* Newer versions of `ydata-profiling` have deprecated theme options.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

This project is licensed under the MIT License.

---

👉 Do you want me to also generate a **requirements.txt** file for you (with correct versions) so the setup is smoother on GitHub?

