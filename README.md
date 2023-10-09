
---

# Pivot Pal: Your Ultimate Data Exploration Toolkit 📊

Welcome to **Pivot Pal** - a Python-based toolkit designed to streamline the exploration and analysis of datasets. Whether you're diving into the Titanic's passenger list, analyzing police records, or exploring Airbnb listings, Pivot Pal has got you covered with a suite of powerful tools.

🌐 **For detailed documentation and case studies, visit our official website:** [pythonpivotpal.com](https://www.pythonpivotpal.com/)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Tools](#tools)
  - [Overview](#overview)
  - [Distribution](#distribution)
  - [Range](#range)
  - [Unique](#unique)
  - [Summarise](#summarise)
  - [Missing](#missing)
  - [Zeros](#zeros)
  - [Datatypes](#datatypes)
- [Case Studies](#case-studies)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
pip install pivot-pal
```

## Usage

To start using Pivot Pal, simply import the necessary modules:

```python
import pandas as pd
from IPython.display import display, Markdown
```

## Tools

### Overview

Get a snapshot of your dataset.

```python
pp.overview(df)
```

### Distribution

Analyze the distribution of values for a specific column.

```python
pp.distribution(df, "column_name")
```

### Range

Determine the minimum and maximum values for each column.

```python
pp.range(df)
```

### Unique

Count the unique values for each column.

```python
pp.unique(df)
```

### Summarise

Summarise numeric columns with various statistics.

```python
pp.summarise(df)
```

### Missing

Identify columns with missing data.

```python
pp.missing(df)
```

### Zeros

Highlight columns with zero values.

```python
pp.zeros(df)
```

### Datatypes

Understand the data types present in your dataset.

```python
pp.datatypes(df)
```

## Case Studies

Dive deep into real-world data exploration with our comprehensive case studies:

- [Titanic Data Exploration](https://www.pythonpivotpal.com/case-studies/titanic)
- [Police Records Analysis](https://www.pythonpivotpal.com/case-studies/police)
- [Airbnb Listings Insights](https://www.pythonpivotpal.com/case-studies/airbnb)

## Contributing

Contributions are welcome! Please read our [contributing guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.

---

