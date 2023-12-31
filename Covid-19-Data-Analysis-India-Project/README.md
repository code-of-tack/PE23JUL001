# COVID-19-Data-Analysis-in-India
Explore COVID-19 data trends and insights in India through data analysis and visualizations. This project uses Python and various data analysis & visualization libraries to uncover valuable information about the pandemic's impact on different regions in India.
# Covid-19 Data Dive: Illuminating India’s Insights

## Table of Contents
1. [Introduction](#introduction)
2. [Data Sources](#data-sources)
3. [Technologies Used](#technologies-used)
4. [Project Purpose and Significance](#project-purpose-and-significance)
5. [Project Objectives](#project-objectives)
6. [Project Structure](#project-structure)
7. [Data Loading and Preprocessing](#data-loading-and-preprocessing)
8. [Temporal Analysis](#temporal-analysis)
9. [Regional Distribution](#regional-distribution)
10. [Outcome Insights](#outcome-insights)
11. [Category Analysis](#category-analysis)
12. [Geospatial Understanding](#geospatial-understanding)
13. [Conclusion](#conclusion)
14. [How to Use](#how-to-use)
15. [How to Contribute](#how-to-contribute)
16. [Contributors](#contributors)


## Introduction

In the wake of the unprecedented global pandemic caused by the novel coronavirus, this project harnesses the power of data analysis & data visualization to understand the patterns and impact of the disease in India. Through exploratory data analysis (EDA), valuable insights, trends, and implications associated with the pandemic's progression within the nation are uncovered.

## Data Sources

- [COVID-19 Dataset](https://github.com/abhisarahuja/Covid-19-Data-Analysis-Project-Using-Python-And-Tableau/blob/main/covid_19_india.csv)
- [India State Boundary Shapefile](https://drive.google.com/file/d/1Ib89r1HiUGrPtuPn5pXKhfZYdpLu1TOt/view?usp=sharing)

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- PyODBC
- GeoPandas
- DateTime
- SQL Server

## Project Purpose and Significance

This analysis serves the dual purpose of unraveling regional nuances of the COVID-19 impact in India and extracting actionable insights to guide strategies for managing the pandemic. It provides valuable guidance to decision-makers, healthcare professionals, and policymakers for formulating effective interventions.

## Project Objectives

1. Temporal Analysis
2. Regional Distribution
3. Outcome Insights
4. Category Analysis
5. Geospatial Understanding

## Project Structure

The project structure includes data loading and preprocessing, followed by individual analyses and visualization sections for each of the objectives listed above.

## Data Loading and Preprocessing

The dataset is loaded from a specified URL, and data integrity is ensured through preprocessing steps. The data is then loaded into an SQL Server database, allowing for efficient data management and analysis.

## Temporal Analysis

A dynamic line chart showcases the trajectory of COVID-19 cases over time, visualizing the temporal evolution of the outbreak.

## Regional Distribution

Bar charts display the total confirmed cases per state/union territory, providing a snapshot of the geographical variations in the pandemic's impact.

## Outcome Insights

A pie chart depicts the distribution between recovered cases and fatalities, elucidating the outcomes of the pandemic.

## Category Analysis

Stacked area charts distinguish between Indian and Foreign nationals in terms of total confirmed cases, offering insights into demographic trends in the outbreak.

## Geospatial Understanding

A choropleth map visually communicates outbreak severity across different states/union territories.

## Conclusion

This project, has successfully employed exploratory data analysis and visualization techniques to uncover regional dynamics, demographic trends, and geospatial severity patterns of the pandemic in India.

## How to Use

Follow these steps to set up and run this project on your local machine:

### Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed (https://www.python.org/downloads/)
- Jupyter Notebook installed (https://jupyter.org/install)
- SQL Server installed (https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
- Git installed (https://git-scm.com/downloads)

### Installation

1. Clone the repository to your local machine using Git.
2. Install the required Python libraries.
3. Install SQL Server and set up a dedicated database named 'Covid-19 Data' (or anything as per your requirements).

### Running the Analysis

1. Open the Jupyter Notebook
2. Navigate to the project folder and open the Covid-19 Data Analysis.ipynb file.
3. Execute the notebook cells one by one to perform data analysis and generate visualizations.

That's it! You can now explore the insights and visualizations generated by the project.

## How to Contribute

Contributions to this project are welcome and encouraged. To get started, follow these steps:

1. **Fork the Repository**: Click the "Fork" button in the top right corner of this repository's page to create your own copy.

2. **Clone the Repository**: Clone your forked repository to your local machine using the following command. Replace `<your-username>` with your GitHub username.

    ```bash
    git clone https://github.com/<your-username>/your-repository.git
    ```

3. **Create a Branch**: Create a new branch to work on your feature or bug fix.

    ```bash
    git checkout -b branch-name
    ```

4. **Make Changes**: Make your desired changes to the codebase.

5. **Test Changes**: If applicable, test your changes thoroughly to ensure they work as expected.

6. **Commit Changes**: Commit your changes with a clear and concise commit message.

    ```bash
    git commit -m "Add feature or fix bug"
    ```

7. **Push Changes**: Push your changes to your forked repository on GitHub.

    ```bash
    git push origin branch-name
    ```

8. **Create a Pull Request**

9. **Review and Discuss**: Your pull request will be reviewed, and any necessary discussions or adjustments will be made.

10. **Merge Pull Request**: Once your changes are approved, your pull request will be merged into the main project.

Thank you for contributing to this project!

## Contributors

- Anuvansh Kumar (owner)
