{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 ![Ironhack logo](https://i.imgur.com/1QgrNNw.png)\
\
# Unemployment in Europe\
\
Analysis of unemployment statistics in Europe\
<br>Ironhack Berlin week 6 project\
<br>Julia Zimpel, Malon Kraaijvanger, Sunday Oluwadare & Rinze Douma\
<br>18/09/2020\
\
## Content\
- [Project description](#Project-description)\
- [Workflow](#Workflow)\
- [Organization](#Organization)\
- [Links](#Links)\
\
## Project description\
\
### Research question\
**Our research question is 'What factors impact the unemployment rate of EU28?'**\
<br>Here we are looking at the EU28 countries and compare it to Greece, who was hit hard by the financial crisis, and Germany, who's economy stayed fairly stable. \
\
### Hypotheses\
With the research question in mind, we are assuming various outcomes:\
1. The unemployment for the EU28 countries increased for all EU28 countries after the financial crisis of 2008. \
2. The unemployment rate is higher for females than for males.\
3. Countries with higher GDP have a lower unemployment rate.\
4. Countries with a higher income inequality have a higher unemployment rate.\
5. It is less likely that people with higher education have a higher unemployment rate than people with lower or medium education levels.\
\
### Findings\
1. Greece was hit harder after the financial crisis and the unemployment rate increased. However the unemployment rate for Germany didn't change much and it even slightly decreased. \
2. In Greece the female unemployment is much higher than the male unemployment, however in Germany the male unemployment is slightly higher than the female unemployment.\
3. Countries with a higher GDP have a lower unemployment rate.\
4. There's no correlation between income inequality and unemployment.\
5. Generally people with a higher education level have a higher employment rate.\
\
\
## Workflow\
1. First research questions and potential hypotheses on unemployment were gathered. \
2. Then, general unemployment data for EU28 from Eurostats was cleaned for initial evaluation of the potential hypotheses. \
3. During cleaning it became transparent which additional data was needed for the hypotheses. For instance, other datasets on gender and GINI from Eurostats as well as on GDP from the OECD were obtained. \
4. The datasets were cleaned, and correlations analyzed. \
5. The data was then visualized for easier interpretation.\
\
\
## Issues\
- Selecting data in huge dataset\
- Cleaning columns in tables, complex dataset\
- Complex codes used in dataset\
- Mainly percentage data\
- Short time period (2008-2019)\
- Only yearly data available, not more granular \
- Some datasets use whole population, instead of active population\
\
## Assumptions\
\
- Rise of Unemployment in Greece after Financial Crisis\
- Higher female employment for Greece, higher male for Germany\
- Higher GDP, lower unemployment\
- No correlation between income inequality and unemployment          \
\
## Organization\
\
#### Data\
- Eurostat tables: https://ec.europa.eu/eurostat/web/lfs/data/database \
- GDP: https://data.oecd.org/gdp/gross-domestic-product-gdp.htm\
- Gini coefficient of equivalised disposable income \
- EU-SILC survey: https://ec.europa.eu/eurostat/web/income-and-living-conditions/data/database\
<br>**Directories**\
<br>Raw: `tsv` and `other_raw_data`\
<br>Intermediate: `pickles`\
<br>Final: `output`\
<br>Explanation files: `translation_of_codes`\
\
\
#### Notebooks\
This folder contains all jupyter notebooks we worked on during the project, which include data cleaning and analysis:\
- Eurostat's general unemployment data\
- Eurostat's gender and unemployment data\
- Eurostat's education levels and unemployment data\
- GINI data\
- GDP data\
\
#### Visuals\
- Tableau graphs\
- Graphs as image files\
\
\
## Next steps\
For further analysis the following could be done:\
- Forecasting future unemployment rate\
- Collect more granular data\
- Normalise measurements\
- Investigate other potential impacting factors\
\
\
## Links\
- [Repository](https://github.com/therinz/unemployment_stats)\
- [Translation dictionaries for codes in tables](https://ec.europa.eu/eurostat/estat-navtree-portlet-prod/BulkDownloadListing?sort=1&dir=dic%2Fen)\
}