# 🌍 World Marriage Dataset Analysis

This project provides a simple **exploratory data analysis (EDA)** of the [World Marriage Dataset](https://www.kaggle.com/datasets/dataanalyst001/world-marriage-dataset) using Python libraries like **Pandas**, **Seaborn**, **Matplotlib**, and **Plotly**. The aim is to clean the data, visualize key trends, and generate insights related to marital status across different countries.

---

## 📁 Dataset Source

- **Source**: [Kaggle: World Marriage Dataset](https://www.kaggle.com/datasets/dataanalyst001/world-marriage-dataset)
- **License**: Open-source (check Kaggle page for details)

---

## 🧰 Tools Used

| Tool         | Purpose                             |
|--------------|-------------------------------------|
| `pandas`     | Data manipulation                   |
| `seaborn`    | Static visualizations               |
| `matplotlib` | Plot styling and layout             |
| `plotly`     | Interactive visualizations (optional) |
| `kagglehub`  | Dataset download from Kaggle        |

---

## 🚀 How It Works

### ✅ Step 1: Download Dataset

```python
import kagglehub
path = kagglehub.dataset_download("dataanalyst001/world-marriage-dataset")
```

### ✅ Step 2: Load and Clean Data

- Load CSV into a DataFrame.
- Clean column names (lowercase, no spaces).
- Check for missing values.

### ✅ Step 3: Visualize

- Countplot for **marital status distribution**.
- Barplot for **top 10 countries by marriage proportion**.

### ✅ Step 4: Export

- Save the cleaned dataset as: `cleaned_world_marriage_data.csv`.

---

## 📊 Key Insights

- 💡 The dataset contains various **marital statuses**, with `'Married'` being the most frequent.
- 💡 Marriage rate is approximated by the **proportion of married individuals per country**.
- 💡 Some countries have a **significantly higher proportion** of married people than others.

---

## 📂 Output Files

| File                             | Description                        |
|----------------------------------|------------------------------------|
| `cleaned_world_marriage_data.csv` | Cleaned dataset after processing   |
| Visualizations                   | Shown via Python/Notebook outputs  |

---

## 🔧 How to Run

### 🔁 Clone the repository:

```bash
git clone https://github.com/yourusername/world-marriage-analysis.git
cd world-marriage-analysis
```

### 📦 Install dependencies:

```bash
pip install pandas seaborn matplotlib plotly kagglehub
```

### ▶️ Run the script:

```bash
python your_script_name.py
```

> Replace `your_script_name.py` with your actual filename.

---

## 🧠 Possible Improvements

- Use Plotly for interactive charts.
- Build a web dashboard using Streamlit.
- Compare marriage stats with other factors like age, employment, education.

---

## 👤 Author

**Vineeth K**  
🎓 BTech Graduate in AI & Data Science  
📍 Thrissur, Kerala, India  
💼 Aspiring Data Scientist  
📅 2025  

---

## ⭐ Star this repo if you found it useful!
