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
