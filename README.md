# Salary Predictor 💰📊

An interactive machine learning web application that predicts salaries based on years of experience using Linear Regression. Built with Streamlit for easy deployment and user interaction.

## 🔗 Live Application

**[→ Launch Salary Predictor App](https://shettynaviya-salary-predictor-app-8rq6rn.streamlit.app/)**

> 💡 **Try it now!** Enter your years of experience and get instant salary predictions powered by machine learning.

## 🎯 Features

- **Home Page** - Interactive/non-interactive data visualizations with filtering
- **Prediction Page** - ML-powered salary predictions based on experience
- **Contribute Page** - Add your data to improve the model

## 🛠️ Technologies

- Python 3.8+
- Streamlit
- Scikit-learn (Linear Regression)
- Pandas, NumPy
- Matplotlib, Plotly
- Pillow

## 📂 Project Structure
```
Salary-Predictor/
├── data/
│   └── sal.jpg
├── app.py
├── Salary_Data.csv
└── README.md
```

## 🚀 Quick Start

### Installation
```bash
git clone https://github.com/shettynaviya/Salary-Predictor.git
cd Salary-Predictor
pip install -r requirements.txt
```

### Run Application
```bash
streamlit run app.py
```

Open browser at `http://localhost:8501`

## 📦 Requirements
```txt
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
matplotlib>=3.7.0
plotly>=5.17.0
scikit-learn>=1.3.0
Pillow>=10.0.0
```

## 📊 Dataset

**Salary_Data.csv** contains:
- YearsExperience (0-20 years)
- Salary (USD)

## 🎨 Pages

### 1. Home
- View and filter salary data
- Toggle between Matplotlib and Plotly charts
- Show/hide data table

### 2. Prediction
- Input years of experience (0-20)
- Get instant salary prediction
- ML model: Linear Regression

### 3. Contribute
- Submit your experience and salary
- Data appended to CSV
- View recent submissions

## 🎯 Use Cases

- Job seekers estimating fair salaries
- HR professionals benchmarking compensation
- Students planning career expectations
- Researchers studying salary trends

## 🔮 Future Enhancements

- [ ] Multiple feature support (education, location, industry)
- [ ] Advanced ML models (Random Forest, XGBoost)
- [ ] Model performance metrics display
- [ ] Deploy to Streamlit Cloud
- [ ] User authentication

## 📧 Contact

**Shetty Naviya**
- GitHub: [@shettynaviya](https://github.com/shettynaviya)

## 📄 License

MIT License

---

⭐ Star this repo if helpful! | 💼 Know your worth with ML
