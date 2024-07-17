{% docs __overview__ %}

### DBT-Core Project README

# DBT-Core Project for Commodities Data Warehouse

This project uses DBT (Data Build Tool) to manage and transform data from a commodities Data Warehouse (DW). The goal is to create a robust and efficient data pipeline that processes and organizes commodities data and their movements for analysis.

## Project Structure

### 1. Seeds

Seeds are static data that are loaded into the Data Warehouse from CSV files. In this project, we use seeds to load commodities movement data.

### 2. Models

Models define data transformations using SQL. They are divided into two main layers: staging and datamart.

#### Staging

The staging layer is responsible for preparing and cleaning the data before it is loaded into the final analysis tables.

- **stg_commodities.sql**: Processes and formats commodities data extracted from the API.
- **stg_movimentacao_commodities.sql**: Processes and formats commodities movement data.

#### Datamart

The datamart layer is where the final analysis data is stored. They are based on the data prepared by the staging layer.

- **dm_commodities.sql**: Integrates processed commodities and movement data, creating a final data model for analysis.

### 3. Sources

Sources are the tables or files from which DBT pulls data to perform transformations.

### 4. Snapshots

Snapshots are used to maintain a historical record of how data changes over time.

## Directory Structure

```plaintext
├── models
│   ├── staging
│   │   ├── stg_commodities.sql
│   │   └── stg_movimentacao_commodities.sql
│   └── datamart
│       └── dm_commodities.sql
├── seeds
│   └── movimentacao_commodities.csv
├── dbt_project.yml
└── README.md

## Running the Project

### Requirements

- Python 3.7+
- DBT

### Execution Steps

1. **Clone the Repository:*:
   ```bash
   git clone <Repository-URL>
   cd <Repository-Name>
   ```

2. **Install DBT:**:
   ```bash
   pip install dbt-core dbt-postgres
   ```

3. **onfigure DBT**:
   - Configure the `profiles.yml` file to connect to your Data Warehouse. The file should be in the `~/.dbt/` directory or the directory specified by the `DBT_PROFILES_DIR` environment variable.

    Example `profiles.yml`:
   ```yaml
   databasesales:
     target: dev
     outputs:
       dev:
         type: postgres
         host: <DB_HOST_PROD>
         user: <DB_USER_PROD>
         password: <DB_PASS_PROD>
         port: <DB_PORT_PROD>
         dbname: <DB_NAME_PROD>
         schema: <DB_SCHEMA_PROD>
         threads: 1
   ```

4. **Run DBT Seeds*:
   ```bash
   dbt seed
   ```

5. **Run DBT Transformations**:
   ```bash
   dbt run
   ```

6. **Check Project Status**:
   ```bash
   dbt test
   ```

## Contribution

To contribute to the project, please fork the repository and submit a pull request with your changes.

---

### Models Description

#### stg_commodities.sql

This model is responsible for processing and formatting commodities data extracted from the API. It performs the necessary cleaning and transformation to prepare the data for the datamart.

#### stg_commodity_movements.sql

This model is responsible for processing and formatting commodities movement data. It performs the necessary cleaning and transformation to prepare the data for the datamart.

#### dm_commodities.sql

This model integrates processed commodities and movement data, creating a final data model for analysis. It calculates metrics and aggregates the data to facilitate analysis in the dashboard.

{% enddocs %}