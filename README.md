# Exercise Badges

![](https://byob.yarr.is/poshraj24/Data_Science-MADE/score_ex1) ![](https://byob.yarr.is/poshraj24/Data_Science-MADE/score_ex2) ![](https://byob.yarr.is/poshraj24/Data_Science-MADE/score_ex3) ![](https://byob.yarr.is/poshraj24/Data_Science-MADE/score_ex4) ![](https://byob.yarr.is/poshraj24/Data_Science-MADE/score_ex5)

# Methods of Advanced Data Engineering Project: Unveiling the Climate Crisis: A Data Science Investigation of Climate Related Issues (CO2 emissions and climated related disasters) 
## Overview
This project explores the relationship between global warming trends, specifically CO<sub>2</sub> emissions, and the increase in climate-related disasters on a yearly(decade-wise) basis. Utilizing data science techniques, we aim to quantify the impact of CO<sub>2</sub> emissions on the frequency and severity of climate-related disasters. The goal is to provide insights into how rising CO<sub>2</sub> levels have contributed to the increase in these disasters and to identify potential strategies for mitigation.
## Datasets
The following data sources are used in this project:

CO<sub>2</sub> Emission by Countries Year Wise (1750-2022):

Metadata URL: Kaggle Metadata
Data URL: Kaggle Data
Data Type: CSV
Description: This dataset contains detailed comparisons of CO<sub>2</sub> emissions from various countries from 1750 to 2022.
Climate Related Disaster Frequency:

Metadata URL: IMF Metadata
Data URL: ArcGIS Data
Data Type: CSV
Description: This dataset, provided by the IMF, details the frequency of climate-related disasters and their links to climate change as documented in climate change literature.
#Implementation
The data from both sources are handled by a two scripts under <code>Extract_Transform</code>, <code>pipeline.py</code> whereas analytics is handled via <code>analysis-report.ipynb</code> file. 

Test cases have been written and verified using pytest to ensure the robustness of the code.
# Main Question
How did CO<sub>2</sub>  start to peak, and are the climate related disasters correlated with CO<sub>2</sub>emissions?
# Final Results
The project addresses a major research question, which are detailed in the issues section and in the project plan document, project-plan.md. The findings are summarized in the final report pdf, analysis-report.pdf, and the code used to generate these findings is available in the exploration notebook, analysis-report.ipynb.
## Kaggle Authentication
To access the dataset from Kaggle, follow these steps:
1. Go to [Kaggle Account Settings](https://www.kaggle.com/settings).
2. Download your Kaggle API key as a `kaggle.json` file.
3. Place the `kaggle.json` file inside the `/project/` directory.

**Filepath:** `/project/kaggle.json`

```
{
  "username":"p*****j",
  "key":"1d51***********************a7"
}
```

## Set Execute Permissions for the Pipeline Script
Before running the analysis pipeline, ensure that the pipeline script has execute permissions. Run the following command:

```bash
chmod +x ./project/pipeline.sh
```
## Run the Analysis Pipeline
Navigate to the project directory and execute the pipeline script:

```bash
cd project && ./pipeline.sh
```

## Set Execute Permissions for the Test Pipeline Script
If you want to run the test pipeline, grant execute permissions to the test script:

```bash
chmod +x ./project/tests.sh
```

## Run the Test Pipeline
Navigate to the project directory and execute the test script:

```bash
cd project && ./tests.sh
```

## Analysis Report
Explore the detailed analysis report [here](https://github.com/poshraj24/Data_Science-MADE/blob/main/project/analysis-report.pdf).
