# %%
import pandas as pd

# %%
from IPython.display import display, Markdown

# %% [markdown]
# # **Intro & Helper**

# %%
import pandas as pd
from IPython.display import display, Markdown

def helper(value=None):
    descriptions = {
        "pp.distribution(df, \"column_name\")": "Displays the distribution of values for a given column.",
        "pp.range(df)": "Shows the minimum and maximum values for each column in the dataset.",
        "pp.unique(df)": "Provides a count of unique values for each column.",
        "pp.summarise(df)": "Summarizes numeric columns with count, sum, mean, median, max, and min values.",
        "pp.missing(df)": "Provides a summary of missing values for each column in the dataset.",
        "pp.zeros(df)": "Summarizes columns with zero values and their respective counts.",
    }

    if not value:
        functions_list = "\n".join([f"- {func}" for func in descriptions.keys()])
        standard_message = f"""
---
# Pivot Pal Helper:
---
## Welcome to 'Pivot Pal' Helper!
To get detailed descriptions of specific functions, provide a keyword inside the parentheses.
Example: `pivot_pal.help('value')` will show functions related to value statistics.
---
### Available Functions:
{functions_list}
---
### Try searching with keywords like 'missing', 'value', 'duplicate', etc.
"""
        display(Markdown(standard_message))
        helper_df = pd.DataFrame({
            'Function Signature': list(descriptions.keys()),
            'Description': list(descriptions.values())
        })
        return helper_df

    # Filter the descriptions based on the provided value
    filtered_descriptions = {k: v for k, v in descriptions.items() if value in k}
    if not filtered_descriptions:
        display(Markdown(f"## No functions found for the keyword '{value}'.\n\nTry another keyword."))
        return
    message = f"## Helper: '{value}'\n---\n\n"
    for func, desc in filtered_descriptions.items():
        message += f"### **{func}**:\n\n    {desc}\n\n"
    display(Markdown(message))



# %%
helper()

# %%
def overview(df):
    # Total number of rows
    total_rows = len(df)

    # Total number of columns
    total_columns = len(df.columns)

    # Total duplicate rows
    total_duplicate_rows = df.duplicated().sum()

    # Most frequent data type
    most_frequent_dtype = df.dtypes.value_counts().idxmax()

    # Number of columns with binary values
    binary_cols = (df.nunique() == 2).sum()

    # Number of columns with missing values
    missing_values_count = df.isnull().sum()
    missing_cols = len(missing_values_count[missing_values_count > 0])

    # Number of columns with zero values
    zero_counts = (df == 0).sum()
    zero_cols = len(zero_counts[zero_counts > 0])

    # Number of unique data types
    unique_dtypes = len(df.dtypes.value_counts())

    # Number of numeric columns
    numeric_cols = len(df.select_dtypes(include=[float, int]).columns)

    # Number of non-numeric columns
    non_numeric_cols = total_columns - numeric_cols

    # Create a DataFrame to display the results
    overview_df = pd.DataFrame({
        'Description': ['Total Rows', 'Total Columns', 'Columns with Missing Values','Total Duplicate Rows', 'Most Frequent Data Type', 'Columns with Binary Values',  'Columns with Zero Values', 'Unique Data Types', 'Numeric Columns', 'Non-Numeric Columns'],
        'Count': [total_rows, total_columns, missing_cols, total_duplicate_rows, most_frequent_dtype, binary_cols, zero_cols, unique_dtypes, numeric_cols, non_numeric_cols]
    })

    # Notifications list
    notifications = []

    # Check for significant columns with missing values
    significant_missing_threshold = 0.1  # 10% of the total rows
    significant_missing_cols = missing_values_count[missing_values_count > significant_missing_threshold * total_rows]

    # Add notifications based on findings
    if len(significant_missing_cols) > 0:
        notifications.append(f"There are {len(significant_missing_cols)} columns with more than {significant_missing_threshold * 100}% missing values. It's recommended to use the **pp.missing(df)** tool to investigate further.")
    if total_duplicate_rows > 0:
        notifications.append(f"There are {total_duplicate_rows: ,} duplicate rows in the dataset. Consider investigating or removing them.")
    if zero_cols > 0:
        notifications.append(f"There are {zero_cols} columns with zero values. Use **pp.zeros(df)** to investigate further.")
    if binary_cols > 0:
        notifications.append(f"There are {binary_cols} columns with binary values in the dataset.")

    markdown_output = "# Dataset Overview\n\n"

    # General Statistics
    markdown_output += "## General Statistics:\n"
    markdown_output += f"- **Total Rows**: {total_rows:,}\n"  # Format with commas
    markdown_output += f"- **Total Columns**: {total_columns:,}\n"  # Format with commas
    markdown_output += f"- **Most Frequent Data Type**: {most_frequent_dtype}\n"
    markdown_output += f"- **Unique Data Types**: {unique_dtypes:,}\n"  # Format with commas
    markdown_output += f"- **Numeric Columns**: {numeric_cols:,}\n"  # Format with commas
    markdown_output += f"- **Non-Numeric Columns**: {non_numeric_cols:,}\n\n"  # Format with commas

    # Data Quality Insights
    markdown_output += "## Data Quality Insights\n\n"
    for note in notifications:
        # Format numbers in notifications with commas
        note = note.format(**{k: f"{v:,}" for k, v in locals().items() if isinstance(v, (int, float))})
        markdown_output += f"- {note}\n\n"

    # Recommendations
    markdown_output += "## Recommendations\n"
    markdown_output += "- Investigate columns with significant missing values to determine if they can be imputed or if the columns should be dropped.\n"
    markdown_output += "- Check the columns with zero values to determine if zeros are valid or placeholders for missing data.\n"
    markdown_output += "- For binary columns, ensure that the encoding is consistent and meaningful.\n"

    # Display the markdown
    display(Markdown(markdown_output))

    # Return the overview DataFrame
    overview_df = pd.DataFrame({
        'Description': ['Total Rows', 'Total Columns', 'Columns with Missing Values', 'Total Duplicate Rows', 'Most Frequent Data Type', 'Columns with Binary Values', 'Columns with Zero Values', 'Unique Data Types', 'Numeric Columns', 'Non-Numeric Columns'],
        'Count': [f"{total_rows:,}", f"{total_columns:,}", f"{missing_cols:,}", f"{total_duplicate_rows:,}", most_frequent_dtype, f"{binary_cols:,}", f"{zero_cols:,}", f"{unique_dtypes:,}", f"{numeric_cols:,}", f"{non_numeric_cols:,}"]  # Format with commas
    })

    return overview_df

# %% [markdown]
# ---
# # **Dataset**
# ---
# 

# %% [markdown]
# ###**Value Distribution Table:** `pp.distribution(df)`
# - Column Name, Count and Distribution
# 

# %%
def distribution(df, column_name):

    # Count Values of column
    counts = df[column_name].value_counts()

    # Calculate % distribution
    percentages = ((counts / len(df)) * 100).round(2)

    return pd.DataFrame({

        column_name: counts.index,
        'count': counts.values,
        '%': percentages.values,

    }).sort_values(by='count', ascending=False)

# %% [markdown]
# ###**Value Distribution Table:** `pp.missing(df)`
# 

# %%
def range(df):

    return pd.DataFrame({'Min Value': df.min(), 'Max Value': df.max()})

# %%
def unique(df):

    unique_counts = df.nunique()
    unique_df = pd.DataFrame({
        'Column Name': unique_counts.index,
        'Unique Count': unique_counts.values
    })
    return unique_df.sort_values(by='Unique Count', ascending=False)


# %%
def summarise(df):

    numeric_df = df.select_dtypes(include=[float, int])  # Select only numeric columns

    summary = pd.DataFrame({
        'Column Name': numeric_df.columns,
        'Count': numeric_df.count().values,
        'Sum': numeric_df.sum().values,
        'Mean': numeric_df.mean().values,
        'Median': numeric_df.median().values,
        'Max': numeric_df.max().values,
        'Min': numeric_df.min().values
    })

    # Reordering the columns for better readability
    column_order = ['Column Name', 'Count', 'Sum', 'Mean', 'Median', 'Max', 'Min']
    summary = summary[column_order]

    return summary


# %% [markdown]
# ---
# # **Missing**
# ---
# 
# 

# %% [markdown]
# ---
# **Missing Stats Table:** `cc.missing(df)`
# - Column Name, Count and Distribution
# ---

# %%
def missing(df):

    # Calculate the number of missing values for each column
    missing_values_count = df.isnull().sum()

    # Calculate the percentage of missing values for each column
    missing_percentage = round((missing_values_count / len(df)) * 100, 0)

    # Create a DataFrame to display the results
    statistics_df = pd.DataFrame({

        'Column Name': missing_values_count.index,
        'Missing Count': missing_values_count.values,
        'Missing %': missing_percentage.values

    })

    # Filter out columns with no missing values and sort by percentage
    statistics_df = statistics_df[statistics_df['Missing Count'] > 0].sort_values(by='Missing %', ascending=False)

    return statistics_df

# %% [markdown]
# ---
# # **Zeros**
# ---

# %% [markdown]
# **Duplicated Rows Table:** `cc.zeros`
# 

# %%
def zeros(df):

    # Find values equal to zero
    zero_counts = (df == 0).sum()

    # Calculate the distribution of zero values
    zero_percentage = (zero_counts / len(df) * 100).round(2)

    # Create a DataFrame with the results
    result_df = pd.DataFrame({'Zero Count': zero_counts, 'Zero %': zero_percentage})

    # Filter out columns with no zero values
    result_df = result_df[result_df['Zero Count'] > 0]

    # Sorting the DataFrame by 'Zero %' in descending order
    result_df = result_df.sort_values(by='Zero %', ascending=False)

    return result_df


# %% [markdown]
# # **Datatypes**

# %%
def datatypes(df):
    # Get data types for each column
    dtypes = df.dtypes

    # Count the occurrences of each data type
    dtypes_count = dtypes.value_counts()

    # Calculate % distribution
    dtypes_percentage = (dtypes_count / len(dtypes) * 100).round()

    # Create a DataFrame for the pivot table-like layout
    pivot_df = pd.DataFrame({
        'Data Type': dtypes_count.index,
        'Column Count': dtypes_count.values,
        '% Distribution': dtypes_percentage.values
    })

    return pivot_df



