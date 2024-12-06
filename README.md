# [# Malaysia Property Analysis With Python](https://medium.com/@kwanqi.yt/real-estate-analysis-with-python-cfe7eb4cbd88)

The property market has always intrigued me, but the most daunting part is figuring out whether a property is genuinely worth buying. As a beginner, I didn’t know where to begin — until I came across Iherng, a Malaysian property YouTuber who shares practical and educational advice for buyers like me. Inspired by his insights, I decided to take his advice and dive into a property market analysis, combining my familiarity with data and his recommended approach.

From his videos, I learned the importance of two key steps before purchasing any property:

Do your research — Analyze publicly available data.
Perform site visits — Always physically inspect the property you’re considering.
This blog series focuses on answering some crucial questions about the property market:

Is this property worth the asking price?
What factors influence property prices the most?
Whether you’re an investor or someone eyeing a second-hand property, this analysis will help you make informed decisions. In Part 1, I’ll start with actual transacted data to uncover market trends and evaluate property values objectively. Through this series, I hope to not only share my approach but also inspire you to do your homework before making a purchase.

I’ll be using Python as the primary tool for data analysis. Python allows for:

Cleaning and preparing raw data for accurate insights.
Visualizing trends effectively.
Running advanced statistical analyses to assess value.
Now, let’s get started by exploring the dataset!

# Dataset Overview
For this analysis, I used a dataset from the National Property Information Centre (NAPIC), which provides transaction data collected by the government of Malaysia. Here’s what you need to know about the data:

Source: NAPIC Open Data
Coverage: Transactions from 2021 to the first half of 2024.
Data points: Includes property area, name, transaction date, size (in square feet), and transaction price.
Focus: This dataset only covers second-hand property sales. It does not include properties sold directly by developers.
For this analysis, I narrowed down the data to properties located in Subang Jaya. This area is particularly interesting to me because I’ve visited it often.

# Why Price Per Square Foot (PSF) is Critical
A key metric in property evaluation is Price Per Square Foot (PSF). It represents the price of the property divided by its size in square feet. Here’s why PSF matters:

Standardized comparison: PSF lets us compare properties of different sizes fairly.
Market trends: It reveals whether a property’s price aligns with typical market values.
Spotting anomalies: High or low PSF values can indicate overpriced or undervalued properties.
In this analysis, PSF is our primary focus for assessing whether a property offers good value.

# Data Preparation
To ensure accurate analysis, the raw data needed some cleaning and preparation. Here’s a summary of the key steps:

Loaded the dataset using Python’s pandas library.
Cleaned up column names and removed unnecessary data like developer-specific metrics.
Standardized formats: Converted dates to a consistent format and transformed prices into numeric values by removing “RM” symbols and commas.

# Basic Data Visualization
Let’s begin with some visualizations to uncover trends:

# 1. PSF by Property Type
This boxplot reveals the price distribution across different property types:

![15 2](https://github.com/user-attachments/assets/ae5c25c6-5de4-4b66-9ba2-3eb4c2c64e0f)

#### What we learned:

Service Apartments: Prices tend to cluster near the lower range, but there’s a significant spread toward higher values (positively skewed). <br/>
SOHO/SOFO/SOVO: Prices cluster in the upper range, indicating premium rates. <br/>
Condominiums & Apartments: These show smaller variability in prices, with tighter ranges around the median. <br/>

# 2. PSF Distribution
A histogram helps us visualize the overall PSF distribution:

![15 3](https://github.com/user-attachments/assets/f9a79414-55f8-4d58-857f-b70549410888)

### What we learned:

Most properties fall within RM 400–600 PSF, with fewer properties at extreme values.

# 3. PSF vs Square Feet
A scatterplot reveals how property size influences PSF:

![15 4](https://github.com/user-attachments/assets/05f2df7a-7b64-4e19-b869-1d6f1499a55a)

#### What we learned:

Larger properties, such as condominiums, often have lower PSF, raising the question: “Are larger properties undervalued?”

Insights and Next Steps
From this initial analysis, we’ve identified interesting trends:

Larger properties tend to have lower PSF.
Different property types exhibit distinct price clusters and spreads.
In the next blog, we’ll take a deeper dive into one specific property in Subang Jaya to answer the critical question:

### Is this property overpriced or underpriced?

Stay tuned as we uncover actionable insights!

Until my next post, you can reach me at kwanqi.yt@gmail.com.
