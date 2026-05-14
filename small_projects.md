# 🚀 Data Science Mini Projects: From Zero to Deployment

### A Structured 30-Day Project Journey for Aspiring Data Scientists

> **Prerequisites:** Basic Python (variables, loops, functions, lists, dictionaries)
> **Goal:** Build real-world intuition across the full Data Science pipeline — from raw data to a deployed model.

---

## 🗺️ Journey Roadmap

```
Phase 1: Foundations      → NumPy & Pandas (Days 1–5)
Phase 2: Data Wrangling   → Cleaning & EDA (Days 6–10)
Phase 3: Visualization    → Storytelling with Data (Days 11–13)
Phase 4: Statistics       → Math Behind the Models (Days 14–16)
Phase 5: Machine Learning → Regression & Classification (Days 17–22)
Phase 6: Advanced ML      → Ensemble & Unsupervised (Days 23–26)
Phase 7: Deployment       → From Model to Product (Days 27–30)
```

---

## 📦 PHASE 1 — Foundations with NumPy & Pandas

> *Learn the building blocks every data scientist uses daily.*

---

### 📅 Day 1 — NumPy: The Number Cruncher

**Project:** Student Grade Analyzer

**Objective:** Use NumPy arrays to analyze a class's exam scores — compute statistics, find toppers, and flag failures.

**What You'll Learn:**

* Creating and slicing NumPy arrays
* `np.mean()`, `np.median()`, `np.std()`, `np.percentile()`
* Boolean masking and filtering
* Broadcasting

**Tasks:**

1. Create a NumPy array of 50 randomly generated scores (0–100)
2. Find mean, median, highest, lowest score
3. Find students who scored below 40 (fail) and above 85 (distinction)
4. Normalize the scores between 0 and 1
5. Reshape the array into 5 rows × 10 students and compute row-wise averages (per subject)

**Dataset:** Generate using `np.random.randint(0, 100, size=50)`

**Technologies:**

| Tool             | Purpose                 |
| ---------------- | ----------------------- |
| Python 3.x       | Base language           |
| NumPy            | Array operations        |
| Jupyter Notebook | Development environment |

**Bonus Challenge:** Add weightage (e.g., 40% theory, 60% practical) and compute weighted final scores.

---

### 📅 Day 2 — NumPy: Image as a Matrix

**Project:** Grayscale Image Manipulator

**Objective:** Understand that images are just matrices — manipulate pixel values using NumPy operations.

**What You'll Learn:**

* Loading and representing images as arrays
* Array slicing (cropping)
* Matrix operations (flip, rotate, brightness)
* `np.clip()`, `np.dot()`

**Tasks:**

1. Load any image using `matplotlib.image.imread()`
2. Convert it to grayscale by averaging RGB channels
3. Increase/decrease brightness by adding/subtracting a constant
4. Flip the image horizontally and vertically
5. Crop a region using array slicing
6. Display all versions side-by-side

**Dataset:** Any `.jpg` image from your device, or download from [Unsplash](https://unsplash.com/) (free, royalty-free)

**Technologies:**

| Tool             | Purpose                   |
| ---------------- | ------------------------- |
| NumPy            | Pixel matrix manipulation |
| Matplotlib       | Image display             |
| Jupyter Notebook | Development environment   |

**Bonus Challenge:** Apply a blur effect by averaging pixel values with their neighbors.

---

### 📅 Day 3 — Pandas: Your First DataFrame

**Project:** IPL Match Data Explorer

**Objective:** Load a real CSV dataset and perform fundamental Pandas operations to extract insights.

**What You'll Learn:**

* `pd.read_csv()`, `.head()`, `.info()`, `.describe()`
* Selecting columns, filtering rows
* `.value_counts()`, `.groupby()`, `.sort_values()`
* Handling basic missing values with `.isnull()`, `.dropna()`

**Tasks:**

1. Load the IPL matches dataset
2. Find the total number of matches played each season
3. Find which team won the most matches overall
4. List all matches played at a specific venue
5. Find the top 5 players with the most "Player of the Match" awards
6. Check for null values and drop incomplete rows

**Dataset:** [IPL Complete Dataset – Kaggle](https://www.kaggle.com/datasets/manasgarg/ipl)
*(File: `matches.csv`)*

**Technologies:**

| Tool             | Purpose                       |
| ---------------- | ----------------------------- |
| Pandas           | Data loading and manipulation |
| Jupyter Notebook | Development environment       |

**Bonus Challenge:** Find the win percentage of each team when batting first vs. fielding first.

---

### 📅 Day 4 — Pandas: GroupBy & Aggregation

**Project:** Sales Performance Dashboard (Data Layer)

**Objective:** Master aggregations and grouping to summarize business data like an analyst.

**What You'll Learn:**

* `groupby()` with multiple keys
* `agg()` with multiple functions
* `pivot_table()`
* Adding computed columns
* `apply()` with lambda

**Tasks:**

1. Load the Superstore Sales dataset
2. Find total sales and profit by Region and Category
3. Identify the top 3 performing Sub-Categories in each Region
4. Calculate profit margin % = (Profit / Sales) × 100 as a new column
5. Create a pivot table of average sales by Region and Segment
6. Find months with negative total profit

**Dataset:** [Sample Superstore – Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

**Technologies:**

| Tool             | Purpose                     |
| ---------------- | --------------------------- |
| Pandas           | GroupBy, pivot, aggregation |
| Jupyter Notebook | Development environment     |

**Bonus Challenge:** Using `resample()`, find quarterly sales trends after converting the Order Date column to datetime.

---

### 📅 Day 5 — Pandas: Merging & Reshaping Data

**Project:** E-Commerce Order Intelligence

**Objective:** Combine multiple related tables (like SQL joins) and reshape data to answer business questions.

**What You'll Learn:**

* `pd.merge()` (inner, left, outer joins)
* `pd.concat()`
* `.melt()` and `.pivot()`
* Multi-index DataFrames
* String operations with `.str`

**Tasks:**

1. Load the Orders, Customers, and Products tables
2. Merge all three into a single master DataFrame
3. Find total revenue per customer (merge + groupby)
4. Identify customers who never placed a second order (left join trick)
5. Use `.melt()` to reshape wide monthly sales columns into a long format
6. Extract the year and month from order dates using `.str` / `dt` accessor

**Dataset:** [Brazilian E-Commerce (Olist) – Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
*(Use: orders, customers, order_items, products tables)*

**Technologies:**

| Tool             | Purpose                        |
| ---------------- | ------------------------------ |
| Pandas           | Merging, reshaping, string ops |
| Jupyter Notebook | Development environment        |

**Bonus Challenge:** Find the average delivery time in days and identify cities with the slowest deliveries.

---

## 🧹 PHASE 2 — Data Wrangling: Cleaning & EDA

> *Real data is messy. Learn to tame it.*

---

### 📅 Day 6 — Data Cleaning Part 1: Missing Values

**Project:** Titanic Survival – Data Preparation

**Objective:** Handle missing values using multiple strategies and understand the impact of each choice.

**What You'll Learn:**

* Identifying missing data patterns (MCAR, MAR, MNAR — conceptually)
* `.isnull().sum()`, heatmap of nulls
* Imputation: mean, median, mode, forward fill, custom logic
* Dropping vs. imputing decisions

**Tasks:**

1. Load the Titanic dataset and map all missing values
2. Visualize missing data using a heatmap (`seaborn.heatmap`)
3. Impute `Age` using median grouped by `Pclass` and `Sex`
4. Fill `Embarked` with the mode
5. Drop the `Cabin` column (too many nulls to salvage)
6. Verify no nulls remain and document every decision made

**Dataset:** [Titanic – Kaggle](https://www.kaggle.com/competitions/titanic/data) or `seaborn.load_dataset('titanic')`

**Technologies:**

| Tool             | Purpose                 |
| ---------------- | ----------------------- |
| Pandas           | Missing value handling  |
| Seaborn          | Missing value heatmap   |
| Matplotlib       | Visualization           |
| Jupyter Notebook | Development environment |

**Bonus Challenge:** Compare model accuracy (logistic regression) with different imputation strategies.

---

### 📅 Day 7 — Data Cleaning Part 2: Duplicates, Types & Outliers

**Project:** Zomato Restaurant Data Cleanup

**Objective:** Handle real-world dirtiness — duplicate rows, wrong data types, and statistical outliers.

**What You'll Learn:**

* `.duplicated()`, `.drop_duplicates()`
* Type conversion: `astype()`, `pd.to_numeric()`, `pd.to_datetime()`
* Outlier detection: IQR method, Z-score
* Removing or capping outliers

**Tasks:**

1. Load the Zomato dataset
2. Find and remove duplicate restaurant entries
3. Clean the `rate` column (remove "/5", convert to float)
4. Clean the `approx_cost` column (remove commas, convert to int)
5. Detect cost outliers using IQR and visualize with a boxplot
6. Cap outliers at the 95th percentile instead of removing them

**Dataset:** [Zomato Bangalore Restaurants – Kaggle](https://www.kaggle.com/datasets/himanshupoddar/zomato-bangalore-restaurants)

**Technologies:**

| Tool             | Purpose                   |
| ---------------- | ------------------------- |
| Pandas           | Cleaning, type conversion |
| Seaborn          | Boxplot                   |
| Scipy            | Z-score calculation       |
| Jupyter Notebook | Development environment   |

**Bonus Challenge:** After cleaning, find the top 5 restaurant types by average rating in each area.

---

### 📅 Day 8 — Data Cleaning Part 3: Feature Engineering

**Project:** House Price Feature Builder

**Objective:** Create new meaningful features from existing ones to boost downstream model performance.

**What You'll Learn:**

* Extracting features from datetime columns
* Label encoding and One-Hot Encoding
* Creating ratio/interaction features
* Binning continuous variables (`pd.cut()`, `pd.qcut()`)
* `sklearn.preprocessing.LabelEncoder`, `pd.get_dummies()`

**Tasks:**

1. Load the House Prices dataset
2. Extract `HouseAge` = `YrSold` - `YearBuilt` and `RemodelAge` = `YrSold` - `YearRemodAdd`
3. Create `TotalSF` = `TotalBsmtSF` + `1stFlrSF` + `2ndFlrSF`
4. One-hot encode `Neighborhood` and other categorical columns
5. Bin `OverallQual` into three groups: Low / Medium / High
6. Create `HasGarage`, `HasPool`, `HasFireplace` binary flags

**Dataset:** [House Prices: Advanced Regression – Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)

**Technologies:**

| Tool             | Purpose                    |
| ---------------- | -------------------------- |
| Pandas           | Feature creation, encoding |
| Scikit-learn     | LabelEncoder               |
| Jupyter Notebook | Development environment    |

**Bonus Challenge:** Compute the correlation of all new features with `SalePrice` and rank them.

---

### 📅 Day 9 — Exploratory Data Analysis (EDA) Part 1

**Project:** Netflix Content Strategy Analysis

**Objective:** Use statistical summaries and visualizations to uncover patterns and tell a story with data.

**What You'll Learn:**

* Univariate analysis (distributions, frequency counts)
* Bivariate analysis (correlations, cross-tabs)
* `seaborn`: `histplot`, `countplot`, `boxplot`, `violinplot`
* `matplotlib` subplots and formatting

**Tasks:**

1. Load the Netflix dataset and clean it (parse dates, fill nulls)
2. Analyze the distribution of content types (Movie vs. TV Show)
3. Find top 10 countries by content production
4. Plot the trend of content added per year
5. Analyze rating distributions across different content types
6. Explore which genres dominate Movies vs. TV Shows

**Dataset:** [Netflix Movies and TV Shows – Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

**Technologies:**

| Tool             | Purpose                   |
| ---------------- | ------------------------- |
| Pandas           | Data manipulation         |
| Matplotlib       | Base plotting             |
| Seaborn          | Statistical visualization |
| Jupyter Notebook | Development environment   |

**Bonus Challenge:** Create a word cloud from the `description` column to find the most common themes.

---

### 📅 Day 10 — Exploratory Data Analysis (EDA) Part 2

**Project:** COVID-19 Global Trends EDA

**Objective:** Perform a complete, publication-quality EDA on a time-series dataset and present your findings as a structured notebook report.

**What You'll Learn:**

* Time series resampling and rolling averages
* Correlation heatmaps
* Log-scale visualization
* Multi-panel dashboards with Matplotlib
* Writing a data story (structured observations)

**Tasks:**

1. Load the Our World in Data COVID-19 dataset
2. Plot daily new cases for India, USA, and Brazil on the same chart
3. Compute and plot a 7-day rolling average to smooth noise
4. Create a correlation heatmap between: cases, deaths, vaccinations, GDP per capita
5. Identify the 3 waves of COVID in India using the rolling average
6. Write a short "Data Story" section summarizing 5 key findings

**Dataset:** [Our World in Data – COVID-19](https://github.com/owid/covid-19-data/tree/master/public/data)
*(Direct CSV: `https://covid.ourworldindata.org/data/owid-covid-data.csv`)*

**Technologies:**

| Tool             | Purpose                  |
| ---------------- | ------------------------ |
| Pandas           | Time series manipulation |
| Matplotlib       | Multi-panel plotting     |
| Seaborn          | Heatmap                  |
| Jupyter Notebook | Development environment  |

**Bonus Challenge:** Animate new case trends over time using `matplotlib.animation`.

---

## 📊 PHASE 3 — Visualization: Storytelling with Data

> *Numbers don't speak — charts do.*

---

### 📅 Day 11 — Matplotlib & Seaborn Mastery

**Project:** India Census Data Dashboard

**Objective:** Build a multi-chart visual dashboard to communicate population insights clearly.

**What You'll Learn:**

* `plt.subplots()` grid layouts
* Bar charts, pie charts, line plots, scatter plots
* Annotations and custom formatting
* Color palettes and themes in Seaborn
* Saving figures as high-resolution images

**Tasks:**

1. Load the India Census 2011 dataset
2. Plot top 10 states by population (horizontal bar chart)
3. Plot urban vs. rural population split (stacked bar)
4. Scatter plot: literacy rate vs. sex ratio by state
5. Heatmap of state-wise population density
6. Combine all 4 charts into a 2×2 subplot dashboard

**Dataset:** [India Census 2011 – Kaggle](https://www.kaggle.com/datasets/danofer/india-census)

**Technologies:**

| Tool             | Purpose                  |
| ---------------- | ------------------------ |
| Matplotlib       | Custom chart creation    |
| Seaborn          | Styled statistical plots |
| Pandas           | Data preparation         |
| Jupyter Notebook | Development environment  |

**Bonus Challenge:** Add a choropleth map of India showing literacy rates by state using `geopandas`.

---

### 📅 Day 12 — Plotly: Interactive Visualizations

**Project:** Global Development Indicators Explorer

**Objective:** Build interactive, web-ready charts that let users explore data dynamically — like a mini Tableau.

**What You'll Learn:**

* `plotly.express` for quick charts
* `plotly.graph_objects` for customization
* Interactive scatter plots with hover info
* Animated bubble charts over time
* Saving as HTML

**Tasks:**

1. Load the Gapminder dataset
2. Create an interactive scatter plot: GDP per Capita vs. Life Expectancy (colored by continent)
3. Add country name as hover tooltip and population as bubble size
4. Animate the same chart over years using `animation_frame`
5. Create an interactive bar race chart for top 10 countries by GDP
6. Export the final chart as a standalone `.html` file

**Dataset:** `px.data.gapminder()` (built into Plotly Express) or [Gapminder – GitHub](https://github.com/jennybc/gapminder)

**Technologies:**

| Tool                 | Purpose                  |
| -------------------- | ------------------------ |
| Plotly Express       | Quick interactive charts |
| Plotly Graph Objects | Custom visuals           |
| Pandas               | Data prep                |
| Jupyter Notebook     | Development environment  |

**Bonus Challenge:** Build a choropleth world map showing life expectancy by country with a year slider.

---

### 📅 Day 13 — Dashboard Building with Streamlit

**Project:** Stock Price Analysis App

**Objective:** Build your first live web dashboard — a real app that non-technical users can interact with.

**What You'll Learn:**

* Streamlit layout: `st.title`, `st.sidebar`, `st.columns`
* User inputs: `st.selectbox`, `st.slider`, `st.date_input`
* Displaying DataFrames and charts interactively
* Running a Streamlit app locally
* Basic app deployment flow

**Tasks:**

1. Let users select a stock ticker (AAPL, TSLA, INFY, etc.) from a dropdown
2. Let users select a date range using a slider
3. Fetch historical data using `yfinance`
4. Display a line chart of closing price
5. Show a statistics summary table (open, close, high, low, volume)
6. Add a 30-day moving average toggle checkbox

**Dataset:** Live data via `yfinance` library (`pip install yfinance`)

**Technologies:**

| Tool      | Purpose            |
| --------- | ------------------ |
| Streamlit | Web app framework  |
| yfinance  | Live stock data    |
| Plotly    | Interactive charts |
| Pandas    | Data manipulation  |

**Bonus Challenge:** Add a "Prediction" tab that shows a 7-day simple moving average forecast.

---

## 🔢 PHASE 4 — Statistics: The Math Behind the Models

> *Understand WHY models work before you use them.*

---

### 📅 Day 14 — Descriptive Statistics & Distributions

**Project:** Salary Distribution Analyzer

**Objective:** Apply core statistical concepts to understand real salary data and its distribution shape.

**What You'll Learn:**

* Central tendency: mean, median, mode
* Spread: variance, standard deviation, IQR
* Skewness and kurtosis
* Normal distribution, log-normal distribution
* QQ plots

**Tasks:**

1. Load the Data Science jobs and salaries dataset
2. Compute full descriptive statistics for salary columns
3. Plot histogram + KDE of salaries
4. Check skewness — apply log transformation and re-plot
5. Generate a Q-Q plot to test for normality (`scipy.stats.probplot`)
6. Compare salary distributions across experience levels using overlapping KDE plots

**Dataset:** [Data Science Job Salaries – Kaggle](https://www.kaggle.com/datasets/ruchi798/data-science-job-salaries)

**Technologies:**

| Tool             | Purpose                    |
| ---------------- | -------------------------- |
| Pandas           | Data manipulation          |
| Scipy            | Statistical tests          |
| Seaborn          | KDE and distribution plots |
| Matplotlib       | QQ plots                   |
| Jupyter Notebook | Development environment    |

**Bonus Challenge:** Perform a confidence interval calculation for the mean salary at the 95% confidence level.

---

### 📅 Day 15 — Hypothesis Testing

**Project:** A/B Test Result Analyzer for an E-Commerce Site

**Objective:** Use statistical tests to make data-driven decisions — just like product teams do at real companies.

**What You'll Learn:**

* Null and alternative hypotheses
* Two-sample t-test
* Chi-square test
* p-value interpretation
* Type I and Type II errors

**Tasks:**

1. Load the A/B test dataset
2. Define the hypothesis: Does the new landing page increase conversions?
3. Check sample sizes and ensure they are representative
4. Perform a two-sample z-test / t-test on conversion rates
5. Interpret the p-value and make a recommendation
6. Perform a Chi-square test on categorical variables (e.g., browser type vs. conversion)

**Dataset:** [A/B Testing Dataset – Kaggle](https://www.kaggle.com/datasets/zhangluyuan/ab-testing)

**Technologies:**

| Tool             | Purpose                       |
| ---------------- | ----------------------------- |
| Scipy            | t-test, chi-square, z-test    |
| Statsmodels      | Proportion z-test             |
| Pandas           | Data manipulation             |
| Seaborn          | Distribution comparison plots |
| Jupyter Notebook | Development environment       |

**Bonus Challenge:** Calculate the required sample size to detect a 2% improvement with 95% confidence and 80% power.

---

### 📅 Day 16 — Correlation & Feature Relationships

**Project:** Health Indicators Relationship Study

**Objective:** Quantify relationships between variables to understand which features matter for prediction.

**What You'll Learn:**

* Pearson and Spearman correlation
* Correlation matrix heatmap
* Scatter matrix / pair plot
* Multicollinearity detection (VIF)
* Point-biserial correlation for binary vs. continuous

**Tasks:**

1. Load the Heart Disease dataset
2. Create a full correlation matrix heatmap
3. Identify the top 5 features most correlated with the target variable
4. Plot a pair plot for the top 4 features, colored by target class
5. Compute VIF (Variance Inflation Factor) to detect multicollinear features
6. Remove one feature from each highly correlated pair (VIF > 5)

**Dataset:** [Heart Disease UCI – Kaggle](https://www.kaggle.com/datasets/ronitf/heart-disease-uci)

**Technologies:**

| Tool             | Purpose                 |
| ---------------- | ----------------------- |
| Pandas           | Data manipulation       |
| Seaborn          | Heatmap, pairplot       |
| Scipy            | Spearman correlation    |
| Statsmodels      | VIF calculation         |
| Jupyter Notebook | Development environment |

**Bonus Challenge:** Apply Principal Component Analysis (PCA) and see how much variance 2 components explain.

---

## 🤖 PHASE 5 — Machine Learning: Regression & Classification

> *Build models that actually predict something.*

---

### 📅 Day 17 — Linear Regression: Your First ML Model

**Project:** Car Price Predictor

**Objective:** Build, evaluate, and interpret your first machine learning model end-to-end.

**What You'll Learn:**

* Train-test split
* `sklearn` pipeline: fit → predict → evaluate
* MSE, RMSE, MAE, R² score
* Residual plots
* Coefficients and their interpretation

**Tasks:**

1. Load and clean the Car Prices dataset
2. Encode categorical variables (fuel type, seller type, etc.)
3. Split data: 80% train, 20% test
4. Train a `LinearRegression` model
5. Evaluate with RMSE and R²
6. Plot actual vs. predicted prices
7. Visualize and interpret the top coefficients

**Dataset:** [Car Price Prediction – Kaggle](https://www.kaggle.com/datasets/vijayaadithyanvg/car-price-predictionused-cars)

**Technologies:**

| Tool                 | Purpose                       |
| -------------------- | ----------------------------- |
| Scikit-learn         | Linear Regression, metrics    |
| Pandas               | Data prep                     |
| Matplotlib / Seaborn | Residual and prediction plots |
| Jupyter Notebook     | Development environment       |

**Bonus Challenge:** Apply Ridge and Lasso regression and compare their R² scores and coefficient shrinkage.

---

### 📅 Day 18 — Logistic Regression: Binary Classification

**Project:** Diabetes Risk Predictor

**Objective:** Predict whether a patient has diabetes using health metrics — a classic binary classification problem.

**What You'll Learn:**

* Logistic regression intuition (sigmoid function)
* Confusion matrix, Accuracy, Precision, Recall, F1-score
* ROC curve and AUC
* Decision threshold tuning
* Classification report

**Tasks:**

1. Load and explore the Pima Diabetes dataset
2. Handle zeros in medical columns (replace with median)
3. Scale features using `StandardScaler`
4. Train a `LogisticRegression` model
5. Evaluate with confusion matrix and classification report
6. Plot the ROC curve and compute AUC
7. Try threshold = 0.3 instead of 0.5 — how does recall change?

**Dataset:** [Pima Indians Diabetes – Kaggle](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

**Technologies:**

| Tool                 | Purpose                          |
| -------------------- | -------------------------------- |
| Scikit-learn         | LogisticRegression, metrics, ROC |
| Pandas               | Data prep                        |
| Matplotlib / Seaborn | ROC curve, confusion matrix      |
| Jupyter Notebook     | Development environment          |

**Bonus Challenge:** Try SMOTE oversampling to handle class imbalance and compare results.

---

### 📅 Day 19 — Decision Tree & Model Explainability

**Project:** Loan Approval Classifier

**Objective:** Build a decision tree model and understand how it makes decisions visually.

**What You'll Learn:**

* Decision Tree: Gini impurity vs. entropy
* Tree visualization with `sklearn.tree.plot_tree`
* Overfitting vs. pruning (`max_depth`)
* Feature importance
* Cross-validation

**Tasks:**

1. Load the Loan Prediction dataset and clean it
2. Encode all categorical features
3. Train a `DecisionTreeClassifier` with no depth limit — observe overfitting
4. Prune the tree using `max_depth=4` — observe the change
5. Visualize the final tree structure
6. Plot feature importances as a bar chart
7. Use 5-fold cross-validation to get a robust accuracy estimate

**Dataset:** [Loan Prediction – Analytics Vidhya / Kaggle](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)

**Technologies:**

| Tool             | Purpose                                 |
| ---------------- | --------------------------------------- |
| Scikit-learn     | DecisionTreeClassifier, cross_val_score |
| Matplotlib       | Tree visualization                      |
| Pandas           | Data prep                               |
| Jupyter Notebook | Development environment                 |

**Bonus Challenge:** Compare the decision tree to K-Nearest Neighbors (KNN) at K=3, 5, 7.

---

### 📅 Day 20 — Random Forest & Hyperparameter Tuning

**Project:** Employee Attrition Predictor

**Objective:** Use an ensemble model and optimize it systematically — the way real ML engineers work.

**What You'll Learn:**

* Random Forest: bagging and feature randomness
* `GridSearchCV` and `RandomizedSearchCV`
* Learning curves (bias-variance)
* SHAP values for model explainability
* Saving a model with `joblib`

**Tasks:**

1. Load the IBM HR Employee Attrition dataset
2. Encode all categorical features; scale numericals
3. Train a baseline `RandomForestClassifier`
4. Tune hyperparameters: `n_estimators`, `max_depth`, `min_samples_split` using `GridSearchCV`
5. Compare baseline vs. tuned model using F1-score
6. Compute and plot SHAP feature importance values
7. Save the final trained model as `attrition_model.pkl` using `joblib`

**Dataset:** [IBM HR Analytics – Kaggle](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)

**Technologies:**

| Tool             | Purpose                    |
| ---------------- | -------------------------- |
| Scikit-learn     | RandomForest, GridSearchCV |
| SHAP             | Model explainability       |
| joblib           | Model persistence          |
| Pandas           | Data prep                  |
| Jupyter Notebook | Development environment    |

**Bonus Challenge:** Build a `Pipeline` object that chains preprocessing + model for clean deployment-ready code.

---

### 📅 Day 21 — Support Vector Machine & Multi-class Classification

**Project:** Handwritten Digit Recognizer (MNIST)

**Objective:** Classify images into 10 digit classes and evaluate multi-class performance.

**What You'll Learn:**

* SVM with RBF kernel
* Multi-class confusion matrix
* `classification_report` for multi-class
* Feature scaling importance for SVMs
* Dimensionality reduction before SVM (PCA)

**Tasks:**

1. Load the MNIST digit dataset from `sklearn.datasets`
2. Visualize 25 sample digits in a 5×5 grid
3. Apply PCA to reduce from 784 to 50 dimensions
4. Train an `SVC(kernel='rbf')` model
5. Evaluate with multi-class classification report
6. Plot a confusion matrix heatmap — which digits get confused?
7. Visualize 5 misclassified examples

**Dataset:** `sklearn.datasets.load_digits()` or [MNIST – Kaggle](https://www.kaggle.com/competitions/digit-recognizer/data)

**Technologies:**

| Tool             | Purpose                  |
| ---------------- | ------------------------ |
| Scikit-learn     | SVC, PCA, metrics        |
| Matplotlib       | Digit visualization      |
| Seaborn          | Confusion matrix heatmap |
| Jupyter Notebook | Development environment  |

**Bonus Challenge:** Compare SVM with a simple Neural Network (MLPClassifier) — which is faster and more accurate?

---

### 📅 Day 22 — End-to-End ML Pipeline

**Project:** Movie Revenue Prediction — Full Pipeline

**Objective:** Apply everything from Day 1–21 into one complete, clean, modular ML project.

**What You'll Learn:**

* Structuring a professional ML notebook
* `sklearn.pipeline.Pipeline` with `ColumnTransformer`
* Combining numerical and categorical preprocessing
* Final model evaluation and reporting
* Documenting and presenting results

**Tasks:**

1. Load the TMDB Movies dataset
2. Select relevant features and define target (`revenue`)
3. Build a full preprocessing pipeline (impute → encode → scale)
4. Train and compare 3 models: Linear Regression, Random Forest, Gradient Boosting
5. Evaluate all 3 using cross-validated RMSE
6. Select the best model and present a clean "Model Card" summary
7. Export the final pipeline as a `.pkl` file

**Dataset:** [TMDB 5000 Movie Dataset – Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

**Technologies:**

| Tool                       | Purpose                          |
| -------------------------- | -------------------------------- |
| Scikit-learn               | Full pipeline, ColumnTransformer |
| XGBoost / GradientBoosting | Ensemble model                   |
| Pandas                     | Data prep                        |
| Matplotlib                 | Results comparison               |
| joblib                     | Pipeline export                  |
| Jupyter Notebook           | Development environment          |

**Bonus Challenge:** Add a `FeatureUnion` that creates polynomial features for only numerical columns.

---

## 🌲 PHASE 6 — Advanced ML: Ensemble & Unsupervised

> *Go beyond the basics — learn what top Kagglers use.*

---

### 📅 Day 23 — XGBoost & Gradient Boosting

**Project:** Credit Card Fraud Detection

**Objective:** Handle a severely imbalanced dataset and use a powerful boosting algorithm to detect fraud.

**What You'll Learn:**

* XGBoost internals (boosting, learning rate, trees)
* Handling class imbalance: `scale_pos_weight`, SMOTE
* `XGBClassifier` with early stopping
* Precision-Recall curve (better than ROC for imbalance)
* Feature importance from XGBoost

**Tasks:**

1. Load the Credit Card Fraud dataset
2. Check class imbalance (fraud ratio ≈ 0.17%)
3. Train XGBoost with `scale_pos_weight` to handle imbalance
4. Use early stopping with a validation set
5. Plot the Precision-Recall curve
6. Find the threshold that maximizes F1-score
7. Plot XGBoost feature importances

**Dataset:** [Credit Card Fraud Detection – Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

**Technologies:**

| Tool             | Purpose                 |
| ---------------- | ----------------------- |
| XGBoost          | Gradient boosting model |
| Imbalanced-learn | SMOTE oversampling      |
| Scikit-learn     | Metrics, PR curve       |
| Pandas           | Data prep               |
| Jupyter Notebook | Development environment |

**Bonus Challenge:** Stack XGBoost with a Logistic Regression meta-learner (basic stacking ensemble).

---

### 📅 Day 24 — K-Means Clustering

**Project:** Customer Segmentation for a Retail Store

**Objective:** Use unsupervised learning to discover hidden customer groups — a real marketing use case.

**What You'll Learn:**

* K-Means algorithm intuition
* Elbow method and Silhouette score for choosing K
* Cluster profiling and labeling
* Visualizing clusters with PCA (2D) and Seaborn
* RFM (Recency, Frequency, Monetary) analysis

**Tasks:**

1. Load the Mall Customers or Online Retail dataset
2. Build RFM features: Recency, Frequency, Monetary value
3. Scale features before clustering
4. Use the Elbow method to select optimal K (try K = 2–10)
5. Train `KMeans` with best K
6. Assign cluster labels and profile each cluster
7. Visualize clusters in 2D using PCA
8. Name the clusters (e.g., "High Value Loyals", "Churning Bargain Hunters")

**Dataset:** [Mall Customer Segmentation – Kaggle](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python) or [Online Retail – UCI](https://archive.ics.uci.edu/dataset/352/online+retail)

**Technologies:**

| Tool                 | Purpose                       |
| -------------------- | ----------------------------- |
| Scikit-learn         | KMeans, PCA, silhouette_score |
| Pandas               | Feature engineering           |
| Seaborn / Matplotlib | Cluster visualization         |
| Jupyter Notebook     | Development environment       |

**Bonus Challenge:** Try DBSCAN and Hierarchical Clustering — compare cluster quality using silhouette scores.

---

### 📅 Day 25 — Natural Language Processing (NLP) Basics

**Project:** Amazon Product Review Sentiment Analyzer

**Objective:** Process raw text data and build a classifier that understands sentiment — your first NLP project.

**What You'll Learn:**

* Text preprocessing: lowercasing, stopword removal, stemming/lemmatization
* Bag of Words (CountVectorizer) and TF-IDF
* Naive Bayes and Logistic Regression for text
* Word cloud visualization
* Confusion matrix for sentiment

**Tasks:**

1. Load the Amazon Reviews dataset
2. Clean text: remove HTML, punctuation, stopwords; apply lemmatization
3. Vectorize using TF-IDF (`TfidfVectorizer`)
4. Train a `MultinomialNB` and `LogisticRegression` classifier
5. Compare accuracy, F1 for both models
6. Generate word clouds for positive and negative reviews separately
7. Test the model on 5 custom reviews you write yourself

**Dataset:** [Amazon Product Reviews – Kaggle](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews)

**Technologies:**

| Tool             | Purpose                 |
| ---------------- | ----------------------- |
| NLTK / spaCy     | Text preprocessing      |
| Scikit-learn     | TF-IDF, classifiers     |
| WordCloud        | Text visualization      |
| Pandas           | Data manipulation       |
| Jupyter Notebook | Development environment |

**Bonus Challenge:** Use `transformers` (HuggingFace) with a pre-trained BERT model to compare against your TF-IDF baseline.

---

### 📅 Day 26 — Time Series Forecasting

**Project:** Store Sales Forecaster

**Objective:** Forecast future sales using time series techniques — critical for supply chain and business planning.

**What You'll Learn:**

* Time series components: trend, seasonality, noise
* Stationarity and ADF test
* ARIMA model fitting
* Facebook Prophet for easy forecasting
* Forecast evaluation: MAPE, RMSE

**Tasks:**

1. Load the Rossmann Store Sales dataset
2. Resample to daily/weekly totals
3. Decompose the time series (trend + seasonality + residual)
4. Test for stationarity with the ADF test; apply differencing if needed
5. Fit an ARIMA model and forecast next 30 days
6. Fit a Facebook Prophet model with yearly and weekly seasonality
7. Compare ARIMA vs. Prophet using MAPE on a holdout set

**Dataset:** [Rossmann Store Sales – Kaggle](https://www.kaggle.com/competitions/rossmann-store-sales/data)

**Technologies:**

| Tool             | Purpose                        |
| ---------------- | ------------------------------ |
| Statsmodels      | ARIMA, ADF test, decomposition |
| Prophet          | Facebook's forecasting library |
| Pandas           | Time series resampling         |
| Matplotlib       | Forecast visualization         |
| Jupyter Notebook | Development environment        |

**Bonus Challenge:** Add external regressors to Prophet (e.g., holidays, promotions) to improve accuracy.

---

## 🚀 PHASE 7 — Deployment: From Model to Product

> *A model that isn't deployed is just a Jupyter notebook.*

---

### 📅 Day 27 — Building a REST API with Flask

**Project:** Iris Flower Classifier API

**Objective:** Wrap your trained ML model in a REST API so any application can consume predictions via HTTP.

**What You'll Learn:**

* Flask app structure
* Loading a saved `.pkl` model
* Building `POST` endpoints that accept JSON
* Returning predictions as JSON
* Testing the API with Postman or `requests`

**Tasks:**

1. Train and save an Iris classifier model using `joblib`
2. Create a Flask app with a `/predict` POST endpoint
3. The endpoint accepts JSON: `{"sepal_length": 5.1, "sepal_width": 3.5, ...}`
4. Return the predicted class and probability as JSON response
5. Add an `/health` GET endpoint that returns `{"status": "OK"}`
6. Test the API locally using `curl` or Postman
7. Add basic input validation (reject invalid feature values)

**Dataset:** `sklearn.datasets.load_iris()` (built-in)

**Technologies:**

| Tool             | Purpose            |
| ---------------- | ------------------ |
| Flask            | REST API framework |
| joblib           | Model loading      |
| Scikit-learn     | Iris classifier    |
| Postman / curl   | API testing        |
| Jupyter Notebook | Model training     |

**Bonus Challenge:** Add rate limiting to your API using `flask-limiter` (max 10 requests/minute).

---

### 📅 Day 28 — Streamlit Deployment: Full ML App

**Project:** House Price Prediction Web App

**Objective:** Build a complete, user-facing web application — from form input to real-time ML prediction.

**What You'll Learn:**

* Building multi-page Streamlit apps
* Form inputs mapped to model features
* Real-time inference in the app
* Displaying prediction with confidence
* Professional UI with Streamlit components

**Tasks:**

1. Use the cleaned House Prices dataset and trained model from Day 17
2. Build a Streamlit app with sidebar inputs for all features
3. On button click, preprocess inputs and run inference
4. Display the predicted price prominently with a confidence range
5. Show a chart comparing the predicted price to average prices in the same neighborhood
6. Add a "Model Info" tab showing model accuracy and feature importances
7. Run the app locally and share a screenshot of the working app

**Dataset:** From Day 17 — [House Prices – Kaggle](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)

**Technologies:**

| Tool         | Purpose               |
| ------------ | --------------------- |
| Streamlit    | Web app UI            |
| joblib       | Model loading         |
| Scikit-learn | Preprocessing + model |
| Plotly       | In-app charts         |
| Pandas       | Feature handling      |

**Bonus Challenge:** Add a "What-If Analysis" tool where users can drag sliders to see how changing features affects the price.

---

### 📅 Day 29 — Dockerizing Your ML App

**Project:** Containerized Sentiment Analysis API

**Objective:** Package your ML application into a Docker container so it runs identically on any machine — the industry standard for deployment.

**What You'll Learn:**

* Writing a `Dockerfile`
* Building and running Docker images
* Exposing ports and passing environment variables
* `requirements.txt` best practices
* The concept of container vs. virtual machine

**Tasks:**

1. Use the sentiment analysis model from Day 25
2. Create a Flask API that serves the model (`/predict` endpoint)
3. Write a `requirements.txt` with all dependencies pinned
4. Write a `Dockerfile`:
   * Base image: `python:3.10-slim`
   * Copy code, install requirements, expose port, set entrypoint
5. Build the Docker image: `docker build -t sentiment-api .`
6. Run the container: `docker run -p 5000:5000 sentiment-api`
7. Test the containerized API with a POST request

**Dataset:** From Day 25 — Model trained on Amazon Reviews

**Technologies:**

| Tool              | Purpose          |
| ----------------- | ---------------- |
| Docker            | Containerization |
| Flask             | API framework    |
| joblib / pickle   | Model loading    |
| Python slim image | Base container   |

**Bonus Challenge:** Write a `docker-compose.yml` that runs both the Flask API and a Redis cache together.

---

### 📅 Day 30 — Cloud Deployment: Capstone Project

**Project:** End-to-End ML Product — Deploy to the Cloud

**Objective:** Take your best model from this journey, build a complete app, and deploy it live on the internet for the world to use.

**What You'll Learn:**

* Deploying Streamlit apps to **Streamlit Community Cloud** (free)
* Deploying Flask APIs to **Render** or **Railway** (free tier)
* GitHub integration for CI/CD
* Environment variables and secrets management
* Creating a professional project README

**Tasks:**

1. Choose your best project (Days 17–26) as the capstone topic
2. Build a polished Streamlit app with proper UI/UX
3. Push all code to a GitHub repository
4. Write a professional `README.md` with: project overview, dataset source, model used, accuracy, how to run locally, and live demo link
5. Deploy to Streamlit Community Cloud via GitHub integration
6. Test the live URL and share it
7. Write a 1-page "Project Report" summarizing: problem, approach, results, and learnings

**Dataset:** Student's choice (any dataset from this journey)

**Technologies:**

| Tool                      | Purpose                         |
| ------------------------- | ------------------------------- |
| Streamlit                 | Web app                         |
| GitHub                    | Version control + CI/CD trigger |
| Streamlit Community Cloud | Free app hosting                |
| Render / Railway          | Flask API hosting (optional)    |
| joblib                    | Model serving                   |
| Markdown                  | README documentation            |

**Bonus Challenge:** Set up GitHub Actions to automatically retrain and redeploy your model when new data is pushed.

---

## 📚 Master Technology Reference

| Technology               | Used From      | Purpose                   |
| ------------------------ | -------------- | ------------------------- |
| Python 3.x               | Day 1          | Base language             |
| Jupyter Notebook         | Day 1          | Interactive development   |
| NumPy                    | Day 1–2       | Array operations          |
| Pandas                   | Day 3–30      | Data manipulation         |
| Matplotlib               | Day 2–30      | Base visualization        |
| Seaborn                  | Day 6–30      | Statistical visualization |
| Plotly                   | Day 12–28     | Interactive charts        |
| Streamlit                | Day 13, 28, 30 | Web apps                  |
| Scikit-learn             | Day 17–30     | ML models & preprocessing |
| XGBoost                  | Day 23         | Gradient boosting         |
| NLTK / spaCy             | Day 25         | NLP preprocessing         |
| Statsmodels              | Day 15–16, 26 | Statistics                |
| Scipy                    | Day 14–15     | Scientific computing      |
| Prophet                  | Day 26         | Time series forecasting   |
| SHAP                     | Day 20         | Model explainability      |
| Flask                    | Day 27, 29     | REST API                  |
| Docker                   | Day 29         | Containerization          |
| GitHub                   | Day 30         | Version control           |
| Streamlit Cloud / Render | Day 30         | Cloud deployment          |

---

## 🏆 Student Progress Tracker

| Day | Project                  | Phase             | Completed |
| --- | ------------------------ | ----------------- | --------- |
| 1   | Grade Analyzer           | NumPy             | ☐        |
| 2   | Image Manipulator        | NumPy             | ☐        |
| 3   | IPL Explorer             | Pandas            | ☐        |
| 4   | Sales Dashboard          | Pandas            | ☐        |
| 5   | E-Commerce Intelligence  | Pandas            | ☐        |
| 6   | Titanic Data Cleaning    | Wrangling         | ☐        |
| 7   | Zomato Cleanup           | Wrangling         | ☐        |
| 8   | House Price Features     | Wrangling         | ☐        |
| 9   | Netflix EDA              | EDA               | ☐        |
| 10  | COVID-19 EDA             | EDA               | ☐        |
| 11  | India Census Dashboard   | Visualization     | ☐        |
| 12  | Gapminder Interactive    | Visualization     | ☐        |
| 13  | Stock Price App          | Visualization     | ☐        |
| 14  | Salary Distributions     | Statistics        | ☐        |
| 15  | A/B Test Analyzer        | Statistics        | ☐        |
| 16  | Health Correlation Study | Statistics        | ☐        |
| 17  | Car Price Predictor      | ML Regression     | ☐        |
| 18  | Diabetes Risk Predictor  | ML Classification | ☐        |
| 19  | Loan Approval Classifier | ML Classification | ☐        |
| 20  | Employee Attrition       | ML Ensemble       | ☐        |
| 21  | Digit Recognizer         | ML SVM            | ☐        |
| 22  | Movie Revenue Pipeline   | ML Pipeline       | ☐        |
| 23  | Fraud Detection          | XGBoost           | ☐        |
| 24  | Customer Segmentation    | Clustering        | ☐        |
| 25  | Sentiment Analyzer       | NLP               | ☐        |
| 26  | Sales Forecaster         | Time Series       | ☐        |
| 27  | Flower Classifier API    | Deployment        | ☐        |
| 28  | House Price App          | Deployment        | ☐        |
| 29  | Dockerized API           | Deployment        | ☐        |
| 30  | Capstone Project         | Deployment        | ☐        |

---

## 💡 General Tips for Every Project

1. **Always start with EDA** — never jump straight to modeling
2. **Document every decision** — why did you choose median over mean?
3. **Version control from Day 1** — push to GitHub daily
4. **Write clean code** — use functions, not 200-line cells
5. **Interpret your results** — numbers mean nothing without context
6. **Test your models on edge cases** — what breaks it?
7. **Google is your best friend** — every data scientist Googles constantly

---

*Curated for aspiring Data Scientists | Start with curiosity, end with a deployed product.*
