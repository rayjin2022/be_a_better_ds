# DS Playground
This repo is a collection of public resources to help you to grab technical skills in data science fields through practical projects.

Currently, this repo includes topics of:

1. **Data Wrangling Scenarios** - Data Analysis: basic pandas queries that helps quickly answer business problems
2. **Regression Scenarios** - Demand Forecasting: projects using Random Forest, Time Series, and Regression Techniques to predict future demand/sales based on historical data
3. **Model Interpretation** - Shapley value: helps identify feature importance and to what extend each feature is affecting final prediction
4. **(WIP) Classification Scenarios** - Propensity Scoring
5. **(WIP) Recommender System**

Ready? Let's have fun with real-world data challenges!

## Quick Navigator
| Topic | Project |
| --- | --- | 
| Demand Forecasting | [Bike demand forecast based on features such as timing and weather indicators](https://github.com/rayjin2022/ds_playground/tree/main/Demand%20Forecasting/bike%20demand%20forecasting) |
| Demand Forecasting | [Item-level demand forecasting for different stores based on trend only](https://github.com/rayjin2022/ds_playground/tree/main/Demand%20Forecasting/store%20item%20demand%20forecasting) |
| Data Analysis | [Lego Data - basic pandas](https://github.com/rayjin2022/ds_playground/tree/main/Data%20Analysis/lego%20analysis%20with%20pandas) |
| Data Analysis | [Order Data - pandas + ployly html reports](https://github.com/rayjin2022/ds_playground/tree/main/Data%20Analysis/sales%20analysis%20with%20plotly) |
| Data Analysis | [Order Data - RFM Analysis](https://github.com/rayjin2022/ds_playground/tree/main/Data%20Analysis/RFM%20analysis) |
| Model Interpretation | [Boston house price - shapley value of features affecting house prices](https://github.com/rayjin2022/ds_playground/tree/main/Model%20Interpretation%20-%20Shap%20Value)|

## Demand Forecasting
It's one of the most classic scenario of how regression models solving real-world requests. The companies need a scientific way to anticipate future sales, thus avoid issues including but not limit to:

1. Out-of-stock and understocking leads to lost of sales, extra refillment cost
2. Overstocking leads to cost of inventory, low turnover, and high working capital
3. Preoccupied supply team refrain from focusing on value-added work 

The following datasets and solutions are included regarding this topic:
- [Bike demand forecast based on features such as timing and weather indicators](https://github.com/rayjin2022/ds_playground/tree/main/Demand%20Forecasting/bike%20demand%20forecasting)

- [Item-level demand forecasting for different stores based on trend only](https://github.com/rayjin2022/ds_playground/tree/main/Demand%20Forecasting/store%20item%20demand%20forecasting)

#### Internal Learnings from Best practices
1. [Demand Forecasting for a Sports Apparel Company](https://drive.google.com/drive/u/0/folders/1eGp8G2CUZjyLDJPXAwTwRoQzZquSZSOx)
    
    Differentiators:
    - Applied models that works best for short, mid, and long-term demand forecasting 
    - Reconstructed data for anomaly periods

2. [Demand Planning for a Retail & Wholeselling Company](https://drive.google.com/drive/u/0/folders/1SlJPyE2ojEvUDQo0EBrXOe5AbA0GU8kK)

    Differentiators:
    - Considered external factors such as holidays, temperature
    - Models were generated for 1500 loops for each SKU each week before finding an optimum
    
## Data Analysis
Not all projects requires Machine Learning, but definitely requireds Data Analysis.

No matter encounter with what kind of data, it's always important to first have a basic understanding of the data.

It's recommended to use pandas-profiling to quickly screen the basic condition of data, then use visualizations (histograms, box plots, scatter plots) to make deep dives on distributions and correlation among features. Crucial features are often found during EDA process, and otherwise would never be found or thought of if jumped into modelling process directly.

The following datasets and solutions are included regarding this topic:
- [Lego Data - basic pandas](https://github.com/rayjin2022/ds_playground/tree/main/Data%20Analysis/lego%20analysis%20with%20pandas)

- [Order Data - pandas + ployly html reports](https://github.com/rayjin2022/ds_playground/tree/main/Data%20Analysis/sales%20analysis%20with%20plotly)

- [Order Data - RFM Analysis](https://github.com/rayjin2022/ds_playground/tree/main/Data%20Analysis/RFM%20analysis)

## Model Interpretation
Although the main focus of ML projects is to make as much accurate predictions as possible, model interpretability, as a intermediate output, is more important than the result.

The following datasets and solutions are included regarding this topic:
- [Boston house price - shapley value of features affecting house prices](https://github.com/rayjin2022/ds_playground/tree/main/Model%20Interpretation%20-%20Shap%20Value)

## References

Original links of resources in this repo are listed below:

| Topic | Author | Project Desription | Note |
| --- | --- | --- | --- |
| Data Analysis | [Joao Correia](https://github.com/joaolcorreia) | [RFM Analysis](https://github.com/joaolcorreia/RFM-analysis) | Simple way to quick segment customers based on Recency, Frequency, and Monetory 
| Data Analysis | [Keith Galli](https://github.com/KeithGalli) | [Lego Data Analysis](https://github.com/KeithGalli/lego-analysis) | How to conduct basic pandas manipulation |
| Model Interpretation | [Vytautas Bielinskas](https://www.linkedin.com/in/bielinskas/) | [Shap Value of Ad's](https://www.youtube.com/watch?v=u7Om2joZWYs) | Examples to explain equation of calculating shap value|
| Model Interpretation | [Ajay Halthor](https://github.com/ajhalthor) | [Shap Value of features in Boston House Prices dataset](https://github.com/ajhalthor/model-interpretability/blob/main/Shap%20Values.ipynb) | Performed shap calculation and visualization on house price regression model|
