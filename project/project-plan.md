# Project Plan

## Title
<!-- Give your project a short title. -->
Unveiling the Climate Crisis: A Data Science Investigation of Climate Related Issues (CO2 emissions and climated related disasters) and Solutions

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How did global warming start to peak, what are the probable climate related disasters and how can it be controlled?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project aims to leverage data science techniques to analyze global warming trends and evaluate the effectiveness of potential solutions. By employing a range of statistical and machine learning methods, we will investigate the relationship between various factors (e.g., greenhouse gas emissions, land use changes, solar radiation) and observed temperature increases. We will also model the potential impact of different mitigation strategies (e.g., renewable energy adoption, carbon capture technologies, reforestation) on future climate scenarios. This research has the potential to provide valuable insights for policymakers, scientists, and the general public, informing evidence-based decision-making in the face of the climate crisis.
## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: CO2 Emission by countries Year wise (1750-2022)
* Metadata URL: https://www.kaggle.com/datasets/moazzimalibhatti/co2-emission-by-countries-year-wise-17502022/
* Data URL: https://www.kaggle.com/datasets/moazzimalibhatti/co2-emission-by-countries-year-wise-17502022/
* Data Type: CSV

This dataset is available in Kaggle and contains detailed comparison of all countries in the world who and when and how much CO2 emitted from 1750-2022.

### Datasource2: Climate Change Data
* Metadata URL:  https://climatedata.imf.org/pages/climatechange-data
* Data URL: https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv
* Data Type: CSV 

This dataset, made available by the IMF, depicts the well-documented links between climate change and natural disasters, as evidenced by a wide variety of climate change literature.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Prior to conducting correlation analysis, we will preprocess both datasets by cleaning unwanted columns and ensuring consistency in date and country code formats [#1][i1]
2. Plot EDA trends of CO2 emissions, surface temperatures, rise of water level over time and so on. Using these parameters we will try to find the impact regarding the occurrance of climate related disasters[#2][i2]
3. Make assumptions and try to find the correlation between the two datasets [#3][i3]
4. Insights: Did the assumption really work? [#4][i4]

[i1]: https://github.com/poshraj24/Data_Science-MADE/issues/1
[i2]: https://github.com/poshraj24/Data_Science-MADE/issues/2
[i3]: https://github.com/poshraj24/Data_Science-MADE/issues/3
[i4]: https://github.com/poshraj24/Data_Science-MADE/issues/4
