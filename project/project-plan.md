# Project Plan

## Title
<!-- Give your project a short title. -->
Unveiling the Climate Crisis: A Data Science Investigation of Climate Related Issues (CO<sub>2</sub> emissions and climated related disasters) 

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. How did CO<sub>2</sub> start to peak, and are the climate related disasters correlated with CO<sub>2</sub> emissions??

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
This project investigates the relationship between global warming trends (specifically  𝐶𝑂<sub>2</sub> emissions) and the increase in climate-related disasters, analyzed on a decadal basis. Utilizing data science techniques, including statistical and machine learning methods, we examine the impact of CO<sub>2</sub> emissions on the observed increase in disasters.
## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: CO<sub>2</sub> Emission by countries Year wise (1750-2022)
* Metadata URL: https://www.kaggle.com/datasets/moazzimalibhatti/co2-emission-by-countries-year-wise-17502022/
* Data URL: https://www.kaggle.com/datasets/moazzimalibhatti/co2-emission-by-countries-year-wise-17502022/
* Data Type: CSV

This dataset is available in Kaggle and contains detailed comparison of all countries in the world who and when and how much CO<sub>2</sub> emitted from 1750-2022.

### Datasource2: Climate Related Disaster Frequency
* Metadata URL:  https://climatedata.imf.org/datasets/b13b69ee0dde43a99c811f592af4e821_0/about
* Data URL: https://opendata.arcgis.com/datasets/b13b69ee0dde43a99c811f592af4e821_0.csv
* Data Type: CSV 

This dataset, made available by the IMF, depicts the well-documented links between climate change and natural disasters, as evidenced by a wide variety of climate change literature.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Prior to conducting correlation analysis, we will preprocess both datasets by cleaning unwanted columns and ensuring consistency in date and country code formats [#1][i1]
2. Make the working pipeline to get curated data [#2][i2]
3. Plot EDA trends of CO<sub>2</sub> emissions and disaster frequencies. Using these parameters we will try to find the impact regarding the occurrance of climate related disasters[#3][i3]
4. Make assumptions and try to find the correlation between the two datasets (CO<sub>2</sub>emissions and disaster frequencies) [#4][i4]


[i1]: https://github.com/poshraj24/Data_Science-MADE/issues/1
[i2]: https://github.com/poshraj24/Data_Science-MADE/issues/2
[i3]: https://github.com/poshraj24/Data_Science-MADE/issues/3
[i4]: https://github.com/poshraj24/Data_Science-MADE/issues/4
