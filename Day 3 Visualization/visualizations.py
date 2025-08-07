# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 16:19:17 2025

@author: saqlain.shah
"""

"""
Box Plot:
    Whisker Plot, Good for measuring data distribution. Plots median values, outliers and quartiles. identifies outliers
    1. Minimum is shown at far left of the chart, at the end of the left whisker
    2. First quartile, Q1 is the far left of the box (left whisker)
    3. The median is shown as a line in the center of the box
    4. Third quartile, Q3, shown at the far right of the box (right whisker)
    5. The maximum is at the far right of the box
    A box plot is used to visualize the distribution of a variable. Seaborn's boxplot() function provides a simple way to create box plots
    
Violin Plot:
    A violin plot is similar to a box plot, but provides a more detailed view of the distribution of the data. Seaborn's violinplot() function provides a simple way to create violin plots.

Scatter Plot:
    Relied on dots to represents individual pieces of data. Useful to see if two variables are correlated
    A scatter plot is used to visualize the relationship between two variables. Seaborn's scatterplot() function provides a simple way to create scatter plots.

Line Plot:
    A line plot is used to visualize the trend of a variable over time. Seaborn's lineplot() function provides a simple way to create line plots.

Histogram:
    Displays count of data and are hence similar to bar chart. Histograms are univariate while bar chart are bivariate
    Histogram displays the same categorical variables in bins
    A histogram is used to visualize the distribution of a variable. Seaborn's histplot() function provides a simple way to create histograms.
    
Countplot:
    plot between categorical and a continuous variable. 
    
Correlation Plot:
    Multivariable analysis, to look into relationships with data points. Correlation could be defined as the affect which one variable has over the other.
    Can be between two variables or it could be one versus many.
    
HeatMaps:
    Multivariable data representation. Color intensity in heat map displays becomes an important factor to understand the affect of data points
    A heatmap is used to visualize the correlation between different variables. Seaborn's heatmap() function provides a simple way to create heatmaps.
    
Pie Chart:
    For Univariate analysis. Used to show percentage or proportional data.

Error Bars:
    Line through a point on a graph, parallel to one of the axes, which represents uncertainty or error of the corresponding coordinate of the point.
    Help to understand and analyze the deviations from the target. 
    Deviation of data points from the threshold could be easily captured.
    Easily captuers deviations from larger set of data points
    It identifies underlying data.

Pairplot:
    A pairplot is used to visualize the relationship between multiple variables. Seaborn's pairplot() function provides a simple way to create pairplots.
    
Density plots:
    Density plots, also known as kernel density plots, are a type of data visualization that display the distribution of a continuous variable. They are similar to histograms, but instead of representing the data as bars, density plots use a smooth curve to estimate the density of the data. In Seaborn, density plots can be created using the kdeplot() function.
"""
#%%
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("iris")

sns.histplot(data=tips, x= "petal_length", bins = 20, kde = True, color= "green")

plt.xlabel("Petal Length (cm)")
plt.ylabel("Frequency")
plt.title("Distribution of Petal Length in Iris Flowers")
plt.show()
#%%
#Scatter Plot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.scatterplot(x = "total_bill", y = "tip", data = tips, hue = "sex", size = "size", sizes = (50, 200))

plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.title("Relationship between Total Bill and Tip")

plt.show()

#%%
# Lineplot
import seaborn as sns

fmri = sns.load_dataset("fmri")
sns.lineplot(x = "timepoint", y = "signal", data = fmri, hue = "event", style = "region", markers = True, dashes = False)

plt.xlabel("Timepoint")
plt.ylabel("Signal Intensity")
plt.title("Changes in Signal Intensity over time")

plt.show()

#%%
#Bar plots
import seaborn as sns

titanic = sns.load_dataset("titanic")

sns.barplot(x = "class", y = "fare", data = titanic, hue= "sex", ci = None, palette = 'muted')
plt.xlabel("Class")
plt.ylabel("Fare")
plt.title("Average fare by class and gender on the Titanic")
plt.show()

#%%
# Density Plots
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.kdeplot(data = tips, x = "total_bill", hue = "time", fill = True, alpha = 0.6, linewidth = 1.5)

plt.xlabel("Total Bill ($)")
plt.ylabel("Density")
plt.title("Density Plot of Total Bill by Meal Time")
plt.show()

#%%
# Box Plot
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.boxplot(x = "day", y = "total_bill", data = tips, hue = "time", palette = "Set3", linewidth=1.5, fliersize = 4)
plt.title("Box Plot of Total Bill by day and Meal Time")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")

plt.show()

#%%
# Violin Plots
import seaborn as sns

iris = sns.load_dataset("iris")

sns.violinplot(x="species", y="petal_length", data=iris)

plt.show()

#%%
# Pairplot
import seaborn as sns
iris = sns.load_dataset("iris")
sns.pairplot(data=iris)

plt.show()