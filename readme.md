# End-to-End Azure Data Engineering Real-Time Project

## 📌 Project Overview

This repository contains an **end-to-end Azure Data Engineering real-time project** implemented by following a structured industry-style architecture. The project demonstrates how raw data is ingested from an on-premise source, processed through a **medallion architecture (Bronze, Silver, Gold)**, and finally served for analytics and visualization.

The implementation closely follows a real-world data engineering workflow using Azure-native services and Databricks.

---

## 🏗️ Architecture Overview

**High-level flow:**

1. On-Premise SQL Server (Source)
2. Azure Data Factory (Ingestion)
3. Azure Data Lake Storage Gen2 (Bronze / Silver / Gold layers)
4. Azure Databricks (Transformations)
5. Azure Synapse Analytics (Serving Layer)
6. Power BI (Visualization)

**Architecture Pattern Used:**

* Medallion Architecture
* Incremental / batch processing
* Scalable cloud-native design

---

## 🧰 Tech Stack

* **Azure Data Factory** – Data ingestion & orchestration
* **Azure Data Lake Storage Gen2** – Centralized data storage
* **Azure Databricks (Apache Spark)** – Data transformation
* **Azure Synapse Analytics** – Data warehousing & analytics
* **Power BI** – Dashboard & reporting
* **SQL Server** – Source system
* **GitHub** – Version control

---

## 📂 Project Folder Structure

```
azure-data-engineering-project/
│
├── adf/
│   ├── pipelines/
│   ├── datasets/
│   └── linkedService/
│
├── databricks/
│   ├── bronze to silver transformations.py
│   ├── silver to gold transformations.py
│   └── storagemount.py
│
├── synapse/
│   ├── sql-scripts/
|   ├── pipelines/
│   ├── datasets/
│   └── linkedService/
│
├── powerbi/
│   └── Dashboard 1.pbix
│
├── screenshots/
│   ├── ADF Pipeline.png/
|   ├── Dashboard 1.png/
│   ├── Resource group.png/
│   └── Synapse pipeline.png/
│
└── README.md
```

---

## 🔄 Data Pipeline Details

### 1️⃣ Data Ingestion (ADF)

* Extracts data from on-premise SQL Server
* Uses Copy Activity
* Loads raw data into **Bronze layer** in ADLS Gen2

### 2️⃣ Bronze Layer

* Raw, unprocessed data
* Stored in original schema

### 3️⃣ Silver Layer (Databricks)

* Data cleansing
* Schema enforcement
* Data type corrections
* Deduplication

### 4️⃣ Gold Layer (Databricks)

* Business-level aggregations
* Analytical-ready datasets
* Optimized for reporting

### 5️⃣ Serving Layer (Synapse)

* External / dedicated SQL pools
* Query-ready tables

### 6️⃣ Visualization (Power BI)

* Interactive dashboards
* Business KPIs
* Real-time insights

---

## 🚀 How to Run This Project

### Prerequisites

* Azure Subscription
* SQL Server (on-premise or VM)
* Azure Data Factory
* Azure Databricks Workspace
* Azure Data Lake Storage Gen2
* Azure Synapse Analytics
* Power BI Desktop

### Steps

1. Create Azure resources
2. Configure Linked Services in ADF
3. Run ADF pipelines
4. Execute Databricks notebooks (Bronze → Silver → Gold)
5. Create Synapse tables
6. Connect Power BI to Synapse

---

## 📸 Screenshots 

* ADF pipeline execution
* Synapse pipeline execution
* Power BI dashboard
* Resource group

(Added images inside a `/screenshots` folder)

---

## 📈 Key Learnings

* Real-time Azure data engineering workflow
* Medallion architecture best practices
* End-to-end pipeline orchestration
* Spark-based transformations
* Enterprise-grade analytics setup


## 👤 Author

**Shagun**
Data Engineer
