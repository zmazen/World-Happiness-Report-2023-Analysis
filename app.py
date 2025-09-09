import pandas as pd
import streamlit as st
import plotly.express as px

st.markdown("# **World Happiness Report 2023 Analysis**")

st.markdown("## Project Objective")
st.markdown(
    """
This project analyzes the World Happiness Report 2023 dataset to explore global happiness trends, 
key drivers of happiness, and interesting insights that can be used for decision-making. 

The goal is to create a visually rich, interactive, and insightful report suitable for a portfolio project.
"""
)

st.markdown("## Dataset")
st.markdown(
    """
The dataset includes:
- Ladder Score (overall happiness)
- Economic indicators (GDP per capita)
- Social support
- Healthy life expectancy
- Freedom to make life choices
- Generosity
- Perceptions of corruption
- Dystopia + Residual (used in report calculation)
"""
)


st.markdown("## Loading the Dataset")

df_whr = pd.read_csv("WHR2023.csv")
st.dataframe(df_whr.head())

df_whr.columns = df_whr.columns.str.title()

cols = [
    "Country Name",
    "Ladder Score",
    "Logged Gdp Per Capita",
    "Social Support",
    "Healthy Life Expectancy",
    "Freedom To Make Life Choices",
    "Generosity",
    "Perceptions Of Corruption",
    "Dystopia + Residual"
]

df_whr = df_whr[cols]
df_whr = df_whr.set_index("Country Name")
df_whr.isnull().sum().sort_values(ascending=False)
df_whr = df_whr.dropna(subset=["Healthy Life Expectancy", "Dystopia + Residual"])
df_whr.isnull().sum().sort_values(ascending=False)

st.markdown("## Final Cleaned Dataset")

st.markdown(
    """
We display the full cleaned dataset after:  
- Standardizing column names  
- Selecting relevant variables  
- Setting country names as the index  
- Removing missing values  
- Ensuring no duplicates  

This dataset is now ready for **Exploratory Data Analysis (EDA)** and visualization.  
"""
)

st.dataframe(df_whr.head())

st.markdown("## Descriptive Statistics")

st.markdown(
    """
We generate summary statistics for all numerical columns in the dataset.  

**Key Insights:**  
- The **average Ladder Score (happiness index)** is around **5.54**, with values ranging from **1.86 (least happy)** to **7.80 (most happy)**.  
- **GDP per capita (log)** averages **9.45**, with a wide spread (min: 5.52, max: 11.66). This indicates large economic disparities between countries.  
- **Social Support** is generally high (mean ~0.80), showing most countries report strong social connections.  
- **Healthy Life Expectancy** ranges from ~51.5 to 77.3 years, highlighting differences in healthcare quality and longevity.  
- **Freedom to make life choices** has a median of ~0.80, but some countries score much lower (~0.38).  
- **Generosity** shows large variation, even negative values (indicating below-average contributions).  
- **Perceptions of corruption** tend to be high (mean ~0.72), meaning most countries report corruption as a significant issue.  
- **Dystopia + Residual** averages around **1.78**, serving as the baseline component in the happiness model.  

These statistics provide a first overview of global well-being and the socio-economic factors behind it.  
"""
)

st.dataframe(df_whr.describe())

st.markdown("## Top 10 Happiest Countries in 2023")

st.markdown(
    """
We extract the 10 countries with the highest **Ladder Score** (Happiness Index).  

**Key Insights:**  
- The top positions are dominated by **Nordic countries** (Finland, Denmark, Iceland, Sweden, Norway), confirming their consistent global leadership in happiness rankings.  
- **Finland** ranks first with a score of **7.80**, maintaining its reputation as the happiest country in the world.  
- Economic prosperity plays a significant role: countries like **Luxembourg** and **Switzerland** also score highly, supported by high **GDP per capita**.  
- High scores in **social support, healthy life expectancy, and freedom of life choices** are common traits across these top countries.  
- Interestingly, **Generosity** is not necessarily very high among the top 10 (some countries even score negative), suggesting happiness is more strongly driven by structural and social factors rather than individual donations.  

This top 10 snapshot highlights that **strong social systems, economic stability, and freedom** are key drivers of happiness worldwide.  
"""
)

df_top10 = df_whr.sort_values(by="Ladder Score", ascending=False).head(10)
st.dataframe(df_top10)

st.markdown("## Bottom 10 Happiest Countries in 2023")

st.markdown(
    """
We extract the 10 countries with the lowest **Ladder Score** (Happiness Index).  

**Key Insights:**  
- **Afghanistan** ranks last with a score of **1.85**, reflecting severe political instability, conflict, and lack of basic freedoms.  
- **Lebanon** appears in the bottom 10 despite having relatively high GDP per capita highlighting that **economic wealth alone does not guarantee happiness**.  
- Most bottom countries are located in **Sub-Saharan Africa** (Sierra Leone, Zimbabwe, Congo, Malawi, Comoros, Tanzania, Zambia), where challenges include poverty, health issues, and limited social infrastructure.  
- Scores in **Healthy Life Expectancy** are much lower compared to the global average, often in the mid-50s, indicating weaker healthcare systems.  
- **Freedom to make life choices** and **social support** are also considerably lower, contributing to dissatisfaction.  
- Interestingly, some countries (like Tanzania and Malawi) show relatively high scores in **freedom** or **social support**, but these are not enough to offset weaknesses in economy and health.  

The bottom 10 highlights how **conflict, governance issues, and underdeveloped infrastructure** severely impact happiness levels.  
"""
)

df_bottom10 = df_whr.sort_values(by="Ladder Score").head(10)
st.dataframe(df_bottom10)

st.markdown("## Top 5 Countries by GDP per Capita")

st.markdown(
    """
We now look at the countries with the **highest GDP per capita (log-transformed)**.  

**Key Observations:**  
- **Luxembourg** leads with the highest GDP per capita (**11.66**) and also a high happiness score (**7.22**).  
- **Singapore** and **Ireland** follow, showing strong economies and above-average happiness (6.58 and 6.91).  
- **Switzerland** combines high GDP (**11.16**) with a strong happiness score (**7.24**), ranking among the happiest globally.  
- **UAE** demonstrates high GDP (**11.14**), yet its happiness score (**6.57**) is noticeably lower compared to European counterparts.  

While GDP strongly correlates with happiness, **it’s not the sole determinant**. For instance:  
- **Singapore** has very high GDP but happiness (6.58) is lower than expected.  
- **Ireland and Switzerland** show a better balance between GDP and happiness.  

This suggests that while **economic prosperity is a key driver**, factors like **social support, freedom, and governance** also significantly affect happiness outcomes.  
"""
)

df_topgdp = df_whr.sort_values(by="Logged Gdp Per Capita", ascending=False).head()
st.dataframe(df_topgdp.head())

st.markdown("## Top 5 Countries by Social Support")

st.markdown(
    """
Here we explore the countries with the **highest levels of social support**.  

**Key Observations:**  
- **Iceland** ranks #1 with the strongest social support (**0.983**) and also enjoys a high happiness score (**7.53**).  
- **Finland** and **Denmark** follow closely, both among the happiest countries globally (scores above 7.5).  
- Interestingly, **Slovakia (0.953)** and **Czechia (0.953)** appear in the top list despite having lower happiness scores (6.46 and 6.84).  

This shows that while **social support strongly boosts happiness**, other factors (like GDP, corruption, and freedom) also play a critical role.  
- Nordic countries (Iceland, Finland, Denmark) maintain **both high social support and high happiness**.  
- Central European countries (Slovakia, Czechia) demonstrate that strong social bonds help, but cannot fully offset other limiting factors.  
"""
)

df_topss = df_whr.sort_values(by="Social Support", ascending=False).head()
st.dataframe(df_topss.head())

st.markdown("## Top 5 Countries by Healthy Life Expectancy")

st.markdown(
    """
These countries enjoy the **longest healthy lifespans**, but their happiness scores vary.  

**Key Observations:**  
- **Hong Kong** leads with the highest life expectancy (**77.28 years**) but has a relatively modest happiness score (**5.30**).  
- **Japan (74.35 years)** and **South Korea (73.65 years)** also rank high in life expectancy, yet their happiness scores are in the mid-range (5.9–6.1).  
- **Singapore (73.80 years)** combines both high life expectancy and strong GDP, yielding a higher happiness score (**6.59**).  
- **Switzerland (72.90 years)** stands out as the only country here with both **very high life expectancy and a top-tier happiness score (7.24)**.  

Conclusion:  
- **Long life expectancy alone does not guarantee high happiness.**  
- Other factors (social support, freedom, corruption perceptions) are equally important in shaping well-being.  
- Switzerland shows the most balanced model: wealth, health, and happiness together.  
"""
)

df_tophle = df_whr.sort_values(by="Healthy Life Expectancy", ascending=False).head()
st.dataframe(df_tophle.head())

st.markdown("## Top 5 Countries by Freedom To Make Life Choices")

st.markdown(
    """
These are the nations where people feel **most free to make life decisions** (e.g., career, lifestyle, family).  

**Key Observations:**  
- **Finland (0.961)** tops the list and also has the **highest happiness score (7.80)**, showing a strong link between freedom and life satisfaction.  
- **Cambodia (0.958)** scores almost as high in freedom, but its happiness score is much lower (**4.39**), suggesting that freedom alone cannot overcome challenges like lower GDP and weaker social support.  
- **Sweden (0.948)** and **Norway (0.947)** combine high freedom with **very high happiness scores (7.3–7.4)**.  
- **Bahrain (0.944)** sits in the middle, with a solid happiness score (**6.17**), supported by high GDP but limited by weaker corruption perceptions.  

Conclusion:  
- **Nordic countries (Finland, Sweden, Norway)** show the strongest relationship between freedom and happiness.  
- **Cambodia’s case** highlights that freedom contributes to well-being but must be supported by **economic stability, social support, and governance**.  
- **Bahrain** demonstrates how high freedom combined with wealth can still result in good (but not top-tier) happiness scores.  
"""
)

df_topftmlc = df_whr.sort_values(by="Freedom To Make Life Choices", ascending=False).head()
st.dataframe(df_topftmlc.head())

st.markdown("## Top 5 Countries by Generosity")

st.markdown(
    """
These are the nations with the **highest generosity scores** (measured by charitable giving and willingness to help others).  

**Key Observations:**  
- **Indonesia (0.531)** ranks **#1 in generosity**, with a decent happiness score (**5.28**) despite only moderate GDP.  
- **Myanmar (0.491)** shows **high generosity** but a lower happiness score (**4.37**), reflecting political/economic struggles.  
- **Gambia (0.364)** has relatively high generosity given its **very low GDP**, but happiness remains low (**4.28**).  
- **Thailand (0.289)** balances **above-average generosity** with stronger GDP and life expectancy, leading to a **better happiness score (5.84)**.  
- **Kenya (0.288)** shows similar generosity to Thailand but with lower GDP and life expectancy, resulting in a lower happiness score (**4.49**).  

Conclusion:  
- Generosity **alone does not guarantee happiness**. Countries like **Myanmar, Gambia, and Kenya** score high in generosity but still have low happiness due to economic and governance challenges.  
- **Indonesia and Thailand** show that when generosity is combined with **higher social support and better living standards**, happiness improves.  
- Compared to **Nordic countries**, generosity is not the strongest driver of happiness but reflects cultural values of sharing and resilience in lower-income countries.  
"""
)

df_topg = df_whr.sort_values(by="Generosity", ascending=False).head()
st.dataframe(df_topg.head())

st.markdown("## Top 5 Countries by Perceptions of Corruption")

st.markdown(
    """
These are the nations with the **highest corruption perception scores** (meaning citizens feel corruption is widespread).  

**Key Observations:**  
- **Romania (0.929)** has the **highest corruption perception**, yet its happiness score (**6.59**) is surprisingly good. Likely supported by strong GDP and social support.  
- **Croatia (0.925)** is similar, with relatively high GDP & life expectancy, but corruption perception drags trust down.  
- **Bosnia & Herzegovina (0.918)** shows high corruption perception alongside **medium happiness (5.63)**.  
- **Nigeria (0.911)** reflects both **low life expectancy (54.9 years)** and high corruption, resulting in a lower happiness score (**4.98**).  
- **Bulgaria (0.911)** matches Nigeria in corruption perception, but higher GDP and social support push its happiness score a bit higher (**5.47**).  

**Conclusion:**  
- **High corruption perception does not always destroy happiness**, in places like **Romania and Croatia**, strong GDP, social support, and life expectancy keep happiness relatively high.  
- But in lower-income countries (e.g., **Nigeria**), corruption perception adds another barrier to happiness, amplifying struggles from poor life expectancy and weak infrastructure.  
- Compared to **Nordic countries (low corruption perception + high happiness)**, this group highlights how **trust in institutions** is a key factor in long-term well-being.  
"""
)

df_toppoc = df_whr.sort_values(by="Perceptions Of Corruption", ascending=False).head()
st.dataframe(df_toppoc.head())

st.markdown("# Summary of Key Insights from Top 5 Comparisons")

st.markdown(
    """
1. **GDP (Logged GDP per Capita)**  
- **Luxembourg, Singapore, Ireland, Switzerland, UAE** lead in wealth.  
- High GDP countries usually score **well in happiness**, but not always the highest — money alone doesn’t guarantee well-being.  

2. **Social Support**  
- **Iceland, Finland, Denmark, Slovakia, Czechia** dominate.  
- Strong social safety nets clearly align with **higher happiness scores**.  
- Nordic countries stand out as the happiest due to both wealth and strong support systems.  

3. **Healthy Life Expectancy**  
- **Hong Kong, Japan, Singapore, South Korea, Switzerland** top this list.  
- High life expectancy doesn’t always equal high happiness (e.g., Hong Kong has very high HLE but a modest happiness score).  
- Suggests that **longevity without freedom or trust** may limit well-being.  

4. **Freedom to Make Life Choices**  
- **Finland, Cambodia, Sweden, Norway, Bahrain** rank highest.  
- Freedom strongly correlates with happiness in Nordic nations.  
- Cambodia is an outlier: very high freedom perception, but still relatively low happiness due to weak economy and health.  

5. **Generosity**  
- **Indonesia, Myanmar, Gambia, Thailand, Kenya** lead.  
- Generosity boosts happiness, even in countries with **lower GDP**.  
- Suggests **cultural and community values** play a big role beyond wealth.  

6. **Perceptions of Corruption**  
- **Romania, Croatia, Bosnia & Herzegovina, Nigeria, Bulgaria** show the highest corruption perception.  
- Some (Romania, Croatia) balance it with stronger economies, keeping happiness moderate.  
- Others (Nigeria, Bosnia) struggle more as corruption combines with weaker institutions.  

**Overall Takeaways**  
- **Nordic countries** consistently perform well due to a **balanced mix** of GDP, social support, freedom, and low corruption.  
- **Asian countries** dominate life expectancy but often lag in freedom or trust.  
- **Developing nations** show how **generosity and community bonds** can still provide resilience despite economic struggles.  
- Happiness is **multifactorial** — no single variable (GDP, freedom, health) explains it fully; it’s the combination that matters.  
"""
)

st.markdown("---")

st.markdown("## Data Visualizations")

st.markdown(
    """
Now that we have explored the dataset and key factors, we move on to **interactive visualizations** using **Plotly Express**.  

These visualizations will help us:  
- Compare countries on happiness and key drivers.  
- Identify trends, outliers, and correlations.  
- Tell a visual story that complements our descriptive analysis.  
"""
)

st.markdown("## Visualizing the Top 10 Happiest Countries")

st.markdown(
    """
We use **bar and pie charts** to illustrate the **Ladder Score** for the top 10 countries.  

**Bar Chart Insights:**  
- **Finland** leads clearly with **7.80**, slightly ahead of Denmark (7.59) and Iceland (7.53).  
- The Nordic countries dominate the top ranks, confirming their consistent high performance in global happiness.  
- The bar heights show small gaps among the top 5, indicating that several countries maintain very similar levels of well-being.  
- **Switzerland, Luxembourg, and New Zealand** appear slightly lower but still above 7, highlighting strong global performance.  

**Pie Chart Insights:**  
- The pie chart emphasizes the **relative contribution of each country** to the top 10 happiness bracket.  
- Nordic countries collectively occupy the largest portion, reinforcing that **high social support, freedom, and economic stability** drive happiness.  
- Even smaller slices (New Zealand, Luxembourg) still represent meaningful scores, showing that high happiness is not exclusive to Europe.  

**Conclusion:**  
- Both visualizations clearly highlight the dominance of **Nordic countries** and the narrow range of Ladder Scores among the happiest nations.  
- This visual storytelling makes it easy for viewers to quickly identify **leaders in global well-being**.  
"""
)


fig = px.bar(
    df_top10,
    x=df_top10.index,
    y="Ladder Score",
    color="Ladder Score",
    title="Top 10 Happiest Countries (Ladder Score)",
    labels={"Country Name": "Country Name", "Ladder Score": "Ladder Score"},
    height=500,
)
st.plotly_chart(fig)

fig = px.pie(
    df_top10,
    names=df_top10.index,
    values="Ladder Score",
    title="Top 10 Happiest Countries (Ladder Score)",
)
st.plotly_chart(fig)

st.markdown("## Visualizing the Bottom 10 Least Happy Countries")

st.markdown(
    """
We now examine the **countries with the lowest Ladder Scores** using **bar and pie charts**.  

**Bar Chart Insights:**  
- **Afghanistan (1.86)** ranks lowest, followed by **Lebanon (2.39)** and **Sierra Leone (3.14)**, showing extreme disparities in global happiness.  
- The bar heights clearly demonstrate how large the gap is between the happiest and least happy countries (top scores ~7.8 vs bottom ~1.86).  
- Many of the bottom 10 countries are affected by **conflict, weak governance, and low social support**, which are likely major contributors to their low scores.  

**Pie Chart Insights:**  
- The pie chart highlights how each country contributes proportionally to the bottom 10 bracket.  
- **Afghanistan and Lebanon** occupy the largest slices, emphasizing their extreme low happiness levels.  
- Smaller slices (e.g., Zambia, Tanzania) show that even within the bottom 10, there is variation, but all remain significantly lower than the global average (~5.54).  

**Conclusion:**  
- These visualizations reinforce that **economic, social, and political factors** heavily influence happiness outcomes.  
- Contrasting top 10 vs bottom 10 charts visually demonstrates **the global inequality in well-being**.  
"""
)

fig = px.bar(
    df_bottom10,
    x=df_bottom10.index,
    y="Ladder Score",
    color="Ladder Score",
    title="Bottom 10 Least Happy Countries (Ladder Score)",
    labels={"Country Name": "Country Name", "Ladder Score": "Ladder Score"},
    height=500,
)
st.plotly_chart(fig)

fig = px.pie(
    df_bottom10,
    names=df_bottom10.index,
    values="Ladder Score",
    title="Bottom 10 Least Happy Countries (Ladder Score)",
)
st.plotly_chart(fig)

st.markdown("## Scatter Plot: Ladder Score vs Social Support")

st.markdown(
    """
This scatter plot examines the relationship between **Social Support** and **Ladder Score** across all countries.  

**Key Observations:**  
- There is a **strong positive correlation**: countries with higher social support generally have higher happiness scores.  
- **Nordic countries** (Finland, Denmark, Iceland) cluster at the top-right, showing **high social support and very high happiness**.  
- **Bottom-ranking countries** (Afghanistan, Lebanon, Sierra Leone) are at the bottom-left, reflecting **low social support and low happiness**.  
- The trendline (OLS regression) confirms that **social support is one of the most significant drivers of happiness globally**.  
- Outliers are minimal, suggesting that social support consistently affects well-being across diverse regions.  

**Conclusion:**  
- Social support is a **key predictor of happiness**, highlighting the importance of strong social networks and safety nets in improving national well-being.  
"""
)

fig = px.scatter(
    df_whr,
    x="Social Support",
    y="Ladder Score",
    hover_name=df_whr.index,
    title="Ladder Score vs Social Support",
    labels={"Social Support": "Social Support", "Ladder Score": "Ladder Score"},
    color_discrete_sequence=["#F28E2B"],
    opacity=0.7,
    trendline="ols"
)
st.plotly_chart(fig)

st.markdown("## Scatter Plot: Ladder Score vs Healthy Life Expectancy")

st.markdown(
    """
This scatter plot explores the relationship between **Healthy Life Expectancy** and **Ladder Score**.  

**Key Observations:**  
- There is a **moderate positive correlation**: countries with higher life expectancy generally tend to have higher happiness scores.  
- **Nordic countries** (Finland, Denmark, Iceland) again appear in the top-right quadrant, combining high life expectancy (≈71–72 years) with high happiness.  
- **Lowest-ranking countries** (Afghanistan, Zimbabwe, Congo) have life expectancy around 54–55 years and correspondingly low happiness.  
- Some exceptions exist: **Lebanon** has a relatively high life expectancy (≈66) but very low happiness (2.39), suggesting **other factors, like social support and freedom, heavily influence happiness** beyond life expectancy alone.  
- The trendline (OLS regression) confirms that while healthy life expectancy contributes to happiness, it is **less predictive than social support or GDP**.  

**Conclusion:**  
- Health is important, but **well-being is multidimensional**, and life expectancy alone does not fully explain variations in global happiness.  
"""
)

fig = px.scatter(
    df_whr,
    x="Healthy Life Expectancy",
    y="Ladder Score",
    hover_name=df_whr.index,
    title="Ladder Score vs Healthy Life Expectancy",
    labels={"Healthy Life Expectancy": "Healthy Life Expectancy", "Ladder Score": "Ladder Score"},
    color_discrete_sequence=["#A32976"],
    opacity=0.7,
    trendline="ols"
)
st.plotly_chart(fig)

st.markdown("## Scatter Plot: Ladder Score vs Freedom To Make Life Choices")

st.markdown(
    """
This scatter plot examines how **freedom to make life choices** relates to **Ladder Score**.  

**Key Observations:**  
- There is a **strong positive correlation**: countries where people report more freedom tend to have higher happiness scores.  
- **Top-ranking countries** (Finland, Denmark, Iceland) are in the top-right corner, combining high freedom (~0.93–0.96) with high happiness (~7.5–7.8).  
- **Lowest-ranking countries** (Afghanistan, Lebanon) are at the bottom-left, indicating low freedom (0.38–0.47) and very low happiness (1.86–2.39).  
- Some middle-income countries (like Israel, Netherlands) show **moderate freedom** but still maintain high happiness, suggesting **freedom is necessary but interacts with other factors** like social support and GDP.  
- The OLS trendline confirms freedom as a **critical predictor of happiness**, second only to social support in explanatory power.  

**Conclusion:**  
- Enhancing **personal freedom and choice** is strongly linked to national well-being.  
- Countries with limited freedom face substantial constraints on overall happiness, even if other factors (like GDP) are moderate.  
"""
)

fig = px.scatter(
    df_whr,
    x="Freedom To Make Life Choices",
    y="Ladder Score",
    hover_name=df_whr.index,
    title="Ladder Score vs Freedom To Make Life Choices",
    labels={"Freedom To Make Life Choices": "Freedom To Make Life Choices", "Ladder Score": "Ladder Score"},
    color_discrete_sequence=["#4E268F"],
    opacity=0.7,
    trendline="ols"
)
st.plotly_chart(fig)

st.markdown("## Scatter Plot: Ladder Score vs Generosity")

st.markdown(
    """
This scatter plot explores the relationship between **Generosity** and **Ladder Score** across countries.  

**Key Observations:**  
- The correlation is **weak to moderate**: higher generosity does not always guarantee higher happiness.  
- **Top-ranking countries** (Finland, Denmark, Iceland) have moderate generosity (≈ -0.02 to 0.21) but still maintain high happiness scores, suggesting **other factors like social support and GDP are more decisive**.  
- **Lower-ranking countries** (Afghanistan, Lebanon, Zimbabwe) show a range of generosity values, some positive and some negative, but consistently low happiness, confirming generosity alone is not sufficient.  
- **Outliers** exist: Indonesia (Generosity ≈ 0.531) has relatively higher generosity but only moderate happiness (~5.28), showing that generosity can boost happiness but depends on context.  
- The trendline (OLS) is nearly flat, reinforcing that **generosity has a limited direct effect** on Ladder Score compared to social support or freedom.  

**Conclusion:**  
- Generosity contributes to happiness, but it is **not the primary driver**; economic factors, social support, and personal freedom play larger roles.  
- Policies aiming to improve well-being should consider generosity **in combination with other social and economic factors**.  
"""
)

fig = px.scatter(
    df_whr,
    x="Generosity",
    y="Ladder Score",
    hover_name=df_whr.index,
    title="Ladder Score vs Generosity",
    labels={"Generosity": "Generosity", "Ladder Score": "Ladder Score"},
    color_discrete_sequence=["#188FFF"],
    opacity=0.7,
    trendline="ols"
)
st.plotly_chart(fig)

st.markdown("## Scatter Plot: Ladder Score vs Perceptions Of Corruption")

st.markdown(
    """
This scatter plot examines the effect of **perceived corruption** on **Ladder Score**.  

**Key Observations:**  
- There is a **moderate negative correlation**: countries with higher corruption perception tend to have lower happiness.  
- **Top-ranking countries** (Finland, Denmark, Iceland) show low perceived corruption (≈0.18–0.67) and high happiness (~7.5–7.8).  
- **Lowest-ranking countries** (Afghanistan, Lebanon, Sierra Leone) have high perceived corruption (~0.85–0.89) and correspondingly low happiness (~1.86–3.14).  
- Some exceptions exist: Israel (high perceived corruption ≈0.71) still maintains a high happiness score (~7.47), indicating **other factors like GDP and social support can offset negative impact**.  
- The OLS trendline confirms a **general downward trend**, showing corruption perception is an important but **not sole determinant** of national happiness.  

**Conclusion:**  
- Lowering corruption perception can positively impact national well-being, but it must be **paired with social support, freedom, and economic growth** to maximize happiness.  
"""
)

fig = px.scatter(
    df_whr,
    x="Perceptions Of Corruption",
    y="Ladder Score",
    hover_name=df_whr.index,
    title="Ladder Score vs Perceptions Of Corruption",
    labels={"Perceptions Of Corruption": "Perceptions Of Corruption", "Ladder Score": "Ladder Score"},
    color_discrete_sequence=["#16A17F"],
    opacity=0.7,
    trendline="ols"
)
st.plotly_chart(fig)

st.markdown("## Distribution of Logged GDP Per Capita")

st.markdown(
    """
- **Overview**: This boxplot shows the distribution of “Logged GDP Per Capita” across countries, including all individual points.
- **High outliers**:
  - Luxembourg (11.660), Singapore (11.571), Ireland (11.527), Switzerland (11.164), UAE (11.145)
  - These countries have very high GDP per capita, reflecting strong economies and high standards of living.
- **Low outliers**:
  - Venezuela (5.527), Congo (Kinshasa) (7.007), Mozambique (7.116), Chad (7.261), Liberia (7.277)
  - These countries have very low GDP per capita, indicative of economic struggles or instability.
- **Median & Quartiles**:
  - Most countries cluster between ~8.5 and 10.5 in logged GDP per capita, representing moderate to high economic development.
- **Insights**:
  - Higher GDP per capita generally correlates with better infrastructure, healthcare, and quality of life.
  - Lower GDP per capita countries often face challenges in development, social services, and income equality.
- **Conclusion**: The distribution highlights global economic disparities, with a small set of very wealthy nations and a long tail of lower-income countries.
"""
)

df_plot = df_whr.reset_index()

fig = px.box(df_plot, 
             x="Logged Gdp Per Capita", 
             points="all",
             hover_name="Country Name",
             title="Distribution of Logged GDP Per Capita",
             color_discrete_sequence=["#19D3F3"])
st.plotly_chart(fig)

st.markdown("## Distribution of Social Support")

st.markdown(
    """
- **Overview**: This boxplot visualizes the distribution of “Social Support” scores across countries, including all individual points.
- **High outliers**:
  - Iceland (0.983), Finland (0.969), Denmark (0.954), Slovakia (0.953), Czechia (0.953)
  - These countries have very strong social support networks, reflecting robust family, community, and societal structures.
- **Low outliers**:
  - Afghanistan (0.341), Benin (0.437), Comoros (0.471)
  - These countries face weaker social support systems, likely due to poverty, conflict, or social instability.
- **Median & Quartiles**: Most countries cluster between ~0.7 and 0.9, showing moderate to high social support globally.
- **Insights**:
  - Higher social support is often linked with higher happiness, better health outcomes, and resilience during crises.
  - Lower social support may contribute to societal vulnerability and lower overall well-being.
- **Conclusion**: The extremes highlight global inequalities in social cohesion and community support, while most countries show moderately high social support.
"""
)

fig = px.box(df_plot, 
             x="Social Support", 
             points="all",
             hover_name="Country Name",
             title="Distribution of Social Support",
             color_discrete_sequence=["#FFA15A"])
st.plotly_chart(fig)

st.markdown("## Distribution of Healthy Life Expectancy")

st.markdown(
    """
- **Overview**: This boxplot shows the spread of “Healthy Life Expectancy” scores across countries, with all individual points included.
- **Median & Quartiles**: Most countries fall between ~63 and 72 years, indicating a general clustering around high life expectancy.
- **High outliers**:
  - Hong Kong S.A.R. of China (77.280), Japan (74.349), Singapore (73.800), South Korea (73.650), Switzerland (72.900)
  - These countries have significantly higher life expectancy than the global median.
- **Low outliers**:
  - Mozambique (51.530), Chad (53.125), Zimbabwe (54.050), Guinea (54.185), Afghanistan (54.712)
  - These countries face much lower healthy life expectancy due to economic, health, or social challenges.
- **Insights**:
  - Higher values typically reflect strong healthcare systems, nutrition, and living conditions.
  - Lower values highlight countries struggling with health infrastructure, conflict, or poverty.
- **Conclusion**: The extremes emphasize global disparities in health and longevity, while most countries cluster around moderately high life expectancy.
"""
)

fig = px.box(df_plot, 
             x="Healthy Life Expectancy", 
             points="all",
             hover_name="Country Name",
             title="Distribution of Healthy Life Expectancy",
             color_discrete_sequence=["#AB63FA"])
st.plotly_chart(fig)

st.markdown("## Distribution of Freedom To Make Life Choices")

st.markdown(
    """
- **Overview**: The boxplot displays the spread of “Freedom To Make Life Choices” scores across countries, including all individual points for full transparency.
- **Median & Quartiles**: Most countries score between ~0.7 and 0.9, showing moderate to high freedom in life decisions.
- **Outliers**:
  - **High outliers (very free)**: Finland (0.961), Cambodia (0.958), Sweden (0.948), Norway (0.947), Bahrain (0.944) — significantly higher than the majority.
  - **Low outliers (very restricted)**: Afghanistan (0.382), Comoros (0.470), Lebanon (0.474), Turkiye (0.475), Madagascar (0.522) — much lower freedom than the global median.
- **Insights**:
  - High outliers reflect countries with strong personal autonomy, supportive policies, or societal norms enabling individual choice.
  - Low outliers may indicate political, economic, or social constraints limiting individual freedoms.
- **Conclusion**: Extreme values highlight countries at both ends of the freedom spectrum, useful for understanding disparities in life choice autonomy globally.
"""
)

fig = px.box(df_plot, 
             x="Freedom To Make Life Choices", 
             points="all",
             hover_name="Country Name",
             title="Distribution of Freedom To Make Life Choices",
             color_discrete_sequence=["#00CC96"])
st.plotly_chart(fig)

st.markdown("## Distribution of Generosity")

st.markdown(
    """
- **Overview**: This boxplot shows how generosity scores are spread across countries, displaying all individual points for full visibility.
- **Median & Quartiles**: Most countries cluster around 0.0–0.2, indicating low to moderate generosity in the dataset.
- **Outliers**:
  - **High outliers (very generous)**: Indonesia (0.531), Myanmar (0.491), Gambia (0.364), Thailand (0.289), Kenya (0.288) significantly higher generosity than the majority.
  - **Low outliers (very low generosity)**: Georgia (-0.254), Greece (-0.240), Japan (-0.237), Morocco (-0.231), Botswana (-0.215) exceptionally low generosity scores.
- **Insights**:
  - High outliers may reflect strong cultural, social, or policy-driven generosity.
  - Low outliers could suggest less social cohesion or lower trust and altruism at the national level.
- **Conclusion**: Outliers highlight extremes in generosity and can help identify countries with unusual social behaviors compared to global norms.
"""
)

fig = px.box(df_plot, 
             x="Generosity", 
             points="all",
             hover_name="Country Name",
             title="Distribution of Generosity",
             color_discrete_sequence=["#EF553B"])
st.plotly_chart(fig)

st.markdown("## Distribution of Perceptions Of Corruption")

st.markdown(
    """
- **Overview**: This boxplot displays the range of perceived corruption across countries, highlighting all individual points for better clarity.
- **Median & Quartiles**: Most countries cluster around 0.7–0.9, indicating moderate perceived corruption.
- **Outliers**:
  - **Low outliers (less perceived corruption)**: Singapore (0.146), Finland (0.182), Denmark (0.196), Sweden (0.202), Switzerland (0.266) exceptionally low perception of corruption.
  - **High outliers (more perceived corruption)**: Romania (0.929), Croatia (0.925), Bosnia and Herzegovina (0.918), Nigeria (0.911), Bulgaria (0.911) very high perception of corruption.
- **Insights**:
  - Countries with the lowest perceived corruption tend to be among the happiest or most developed nations.
  - High outliers often indicate systemic governance or transparency issues affecting public trust.
- **Conclusion**: Outliers in corruption perception are strong indicators of institutional effectiveness and may significantly influence overall happiness scores.
"""
)

fig = px.box(df_plot, 
             x="Perceptions Of Corruption", 
             points="all",
             hover_name="Country Name",
             title="Distribution of Perceptions Of Corruption",
             color_discrete_sequence=["#636EFA"])
st.plotly_chart(fig)

st.markdown("## World Happiness Report 2025 – Final Insights")

st.markdown(
    """
### 1. Happiest vs Least Happy Countries
**Top 10 happiest countries:**  
- Nordic dominance: Finland (7.80), Denmark (7.59), Iceland (7.53)  
- Small gaps among top 5 indicate consistently high well-being  

**Bottom 10 least happy countries:**  
- Afghanistan (1.86), Lebanon (2.39), Sierra Leone (3.14)  
- Large gap between top and bottom (~7.8 vs ~1.86)  
- Low scores linked to conflict, poor governance, and weak social support  

**Conclusion:**  
- Global inequality in happiness is evident; top countries cluster tightly, while bottom countries show extreme disparities

---

### 2. Social Support
- **Correlation with happiness:** Strong positive  
- **High outliers:** Iceland (0.983), Finland (0.969), Denmark (0.954)  
- **Low outliers:** Afghanistan (0.341), Benin (0.437), Comoros (0.471)  

**Conclusion:**  
- Social support is a key predictor of national happiness

---

### 3. Healthy Life Expectancy
- **Correlation with happiness:** Moderate positive  
- **High outliers:** Hong Kong (77.28), Japan (74.35), Singapore (73.80)  
- **Low outliers:** Mozambique (51.53), Chad (53.13), Afghanistan (54.71)  

**Conclusion:**  
- Longevity contributes to happiness but is secondary to social and economic factors

---

### 4. Freedom To Make Life Choices
- **Correlation with happiness:** Strong positive  
- **High outliers:** Finland (0.961), Cambodia (0.958), Sweden (0.948)  
- **Low outliers:** Afghanistan (0.382), Comoros (0.470), Lebanon (0.474)  

**Conclusion:**  
- Freedom significantly impacts well-being; limited freedom correlates with low happiness

---

### 5. Generosity
- **Correlation with happiness:** Weak to moderate  
- **High outliers:** Indonesia (0.531), Myanmar (0.491), Gambia (0.364)  
- **Low outliers:** Georgia (-0.254), Greece (-0.240), Japan (-0.237)  

**Conclusion:**  
- Generosity alone is not a strong predictor; it interacts with social support and GDP

---

### 6. Perceptions of Corruption
- **Correlation with happiness:** Moderate negative  
- **Low outliers (less corruption):** Singapore (0.146), Finland (0.182), Denmark (0.196)  
- **High outliers (more corruption):** Romania (0.929), Croatia (0.925), Nigeria (0.911)  

**Conclusion:**  
- Reducing corruption perception improves well-being, but social support, freedom, and GDP are crucial

---

### 7. Logged GDP Per Capita
- **Correlation with happiness:** Positive  
- **High outliers:** Luxembourg (11.66), Singapore (11.57), Ireland (11.53)  
- **Low outliers:** Venezuela (5.53), Mozambique (7.12), Chad (7.26)  

**Conclusion:**  
- Wealth enhances well-being but is insufficient without social support and freedom

---

### 8. Overall Takeaways
- **Primary happiness drivers:** Social support, freedom to make life choices  
- **Secondary drivers:** Healthy life expectancy, GDP per capita  
- **Moderate/limited drivers:** Generosity, perceptions of corruption  
- **Patterns:**  
  - Nordic countries excel across all indicators  
  - Lowest-ranking countries face multiple compounding issues  
  - Outliers reveal exceptional national circumstances
"""
)