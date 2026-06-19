rbi qa · PY
# =============================================================================
# DVT ESA – Power BI
# Important Questions & Answers | Comprehensive Study Guide | 10-Mark Coverage
# MTech Data Science & AI | PES University
# =============================================================================
 
 
# =============================================================================
# Q1. What is Power BI?
# =============================================================================
 
# Power BI is a Business Intelligence (BI) and Data Visualization tool developed by Microsoft.
# It enables users to connect to multiple data sources, transform data, create interactive
# reports and dashboards, and support data-driven decision-making across an organization.
 
# Key Features:
# - Data visualization with interactive charts and graphs
# - Interactive dashboards for real-time insights
# - Real-time analytics and live data connections
# - Cloud integration via Power BI Service
# - Data sharing, collaboration, and role-based access
# - Support for 100+ data connectors (SQL, Excel, Web APIs, etc.)
 
 
# =============================================================================
# Q2. Explain the Components of Power BI.
# =============================================================================
 
# Power BI has five major components, each serving a specific purpose in the BI workflow.
 
# Components:
# - Power BI Desktop       : Windows application to design reports and data models
# - Power BI Service       : Cloud platform (app.powerbi.com) to publish, share, and collaborate
# - Power BI Mobile        : iOS/Android apps to view reports on smartphones and tablets
# - Power BI Gateway       : Secure bridge connecting on-premise data sources to the cloud
# - Power BI Report Server : On-premise server to host and distribute reports internally
 
 
# =============================================================================
# Q3. What is Power Query?
# =============================================================================
 
# Power Query is a data transformation and preparation tool embedded in Power BI.
# It is used to extract, clean, shape, and transform raw data from multiple sources
# before loading it into the data model.
 
# Common Power Query Operations:
# - Remove duplicates and null values
# - Filter rows and columns based on conditions
# - Merge and append multiple tables
# - Split columns (e.g., full name into first/last)
# - Change data types and rename columns
# - Pivot and unpivot data
# - Group by and aggregate data
 
 
# =============================================================================
# Q4. Explain the ETL Process in Power BI.
# =============================================================================
 
# ETL stands for Extract, Transform, and Load. It is the backbone of data preparation in Power BI.
 
# ETL Phases:
# - Extract   : Collect raw data from various sources: databases, Excel, APIs, web
# - Transform : Clean and reshape data using Power Query Editor
# - Load      : Load the prepared data into the Power BI data model for reporting
 
# Benefits of ETL in Power BI:
# - Improves data quality and consistency
# - Reduces errors in reporting
# - Supports data from multiple heterogeneous sources
# - Automates repetitive data preparation tasks
 
 
# =============================================================================
# Q5. Explain Data Modeling in Power BI.
# =============================================================================
 
# Data Modeling is the process of defining relationships between tables so that data
# can be efficiently queried and analyzed across multiple tables.
 
# Types of Relationships:
# - One-to-One (1:1)   : Each row in Table A matches exactly one row in Table B
# - One-to-Many (1:N)  : One row in Table A relates to many rows in Table B (most common)
# - Many-to-Many (M:N) : Multiple rows on both sides (requires bridge table)
 
# Key Concepts:
# - Star Schema            : Fact table at center connected to dimension tables (recommended)
# - Snowflake Schema       : Extended star with normalized dimensions
# - Cross-filter direction : Single vs. Both (bidirectional filtering)
# - Active vs. Inactive Relationships : Only one active relationship allowed between two tables at a time
 
# Benefits of Data Modeling:
# - Enables complex cross-table analysis
# - Reduces data redundancy
# - Improves report performance
 
 
# =============================================================================
# Q6. Differentiate Between Report and Dashboard.
# =============================================================================
 
# Definition:
# - Report    : Multi-page detailed analysis document
# - Dashboard : Single-page summary of key metrics
 
# Pages:
# - Report    : Multiple pages
# - Dashboard : Single page (canvas)
 
# Purpose:
# - Report    : In-depth data exploration
# - Dashboard : High-level overview and monitoring
 
# Created In:
# - Report    : Power BI Desktop
# - Dashboard : Power BI Service
 
# Drill-Down:
# - Report    : Full drill-down support
# - Dashboard : Limited drill-down
 
# Interactivity:
# - Report    : Highly interactive (slicers, filters)
# - Dashboard : Pinned tiles, less interactive
 
# Data Source:
# - Report    : One dataset per page
# - Dashboard : Can combine from multiple reports
 
 
# =============================================================================
# Q7. What are Visualizations in Power BI?
# =============================================================================
 
# Visualizations are graphical representations of data that help communicate insights effectively.
# Power BI offers 30+ built-in visual types and supports custom visuals from AppSource.
 
# Common Visualization Types:
# - Bar Chart / Column Chart : Compare values across categories
# - Line Chart               : Show trends over time
# - Pie Chart / Donut Chart  : Show proportions
# - Scatter Plot             : Show correlation between two measures
# - Map / Filled Map         : Geographic data visualization
# - KPI Card                 : Display a single key metric
# - Gauge Chart              : Show progress toward a target
# - Matrix / Table           : Show data in tabular form with totals
# - Waterfall Chart          : Show cumulative effect of values
# - Treemap                  : Hierarchical proportional display
# - Funnel Chart             : Show pipeline/stage conversion
 
 
# =============================================================================
# Q8. What is DAX?
# =============================================================================
 
# DAX (Data Analysis Expressions) is the formula language used in Power BI,
# Analysis Services, and Power Pivot. It is used to create calculated columns,
# measures, and tables for advanced analytics.
 
# Key Uses of DAX:
# - Creating Measures for dynamic aggregations
# - Creating Calculated Columns for row-level computations
# - Time Intelligence functions (YTD, MTD, SAMEPERIODLASTYEAR)
# - Filter context manipulation (CALCULATE, FILTER, ALL)
 
# Common DAX Functions:
# - SUM()       : SUM(Sales[Amount])                                  --> Adds all values in a column
# - COUNT()     : COUNT(Orders[OrderID])                              --> Counts rows with non-blank values
# - AVERAGE()   : AVERAGE(Sales[Price])                               --> Calculates average
# - CALCULATE() : CALCULATE(SUM(Sales[Amount]), Region='South')       --> Evaluates with modified filter context
# - IF()        : IF(Sales[Amount]>1000, 'High', 'Low')               --> Conditional logic
# - RELATED()   : RELATED(Product[Category])                          --> Fetches value from related table
# - DATEADD()   : DATEADD(Dates[Date], -1, YEAR)                      --> Time intelligence shift
 
# Example DAX Measures:
# Total Sales   = SUM(Sales[Amount])
# Profit Margin = DIVIDE([Total Profit], [Total Sales], 0)
# YTD Sales     = TOTALYTD(SUM(Sales[Amount]), Dates[Date])
 
 
# =============================================================================
# Q9. Difference Between Measure and Calculated Column.
# =============================================================================
 
# Calculation:
# - Measure            : Evaluated dynamically at query time
# - Calculated Column  : Evaluated row by row at data refresh
 
# Storage:
# - Measure            : NOT stored in the model (computed in memory)
# - Calculated Column  : Stored in the model (occupies memory)
 
# Context:
# - Measure            : Responds to report filters and slicers
# - Calculated Column  : Does not respond to filters dynamically
 
# Use Case:
# - Measure            : Aggregations: totals, averages, ratios
# - Calculated Column  : Row-level logic: profit per row, category flag
 
# Example:
# - Measure            : Total Sales = SUM(Sales[Amount])
# - Calculated Column  : Profit = Sales[Revenue] - Sales[Cost]
 
# Performance:
# - Measure            : Better for large datasets
# - Calculated Column  : Increases model size
 
 
# =============================================================================
# Q10. Explain Interactive Dashboards.
# =============================================================================
 
# Interactive Dashboards in Power BI allow users to explore and analyze data dynamically
# without needing technical skills. They combine multiple visuals that respond to user actions.
 
# Key Interactive Features:
# - Filters         : Narrow down data displayed across the entire report page
# - Slicers         : Visual filter controls (dropdown, buttons, date range)
# - Drill-Down      : Navigate from summary to detail (e.g., Year > Quarter > Month)
# - Drill-Through   : Jump to a detail page based on selected data point
# - Cross-Filtering : Clicking one visual automatically filters all related visuals
# - Bookmarks       : Save specific view states for storytelling
# - Tooltips        : Show additional info on hover
 
# Benefits:
# - Empowers non-technical users to explore data independently
# - Supports faster, data-driven decisions
# - Reduces need for multiple static reports
 
 
# =============================================================================
# Q11. What is a Slicer?
# =============================================================================
 
# A Slicer is a visual filter element placed directly on a report page.
# It allows users to filter all related visuals on the page interactively by selecting values.
 
# Types of Slicers:
# - Dropdown Slicer      : Select one or multiple values from a list
# - List Slicer          : Checkboxes for multi-select
# - Between Slicer       : For numeric or date ranges
# - Relative Date Slicer : Last N days, this month, this year, etc.
# - Tile Slicer          : Button-style selection
 
# Common Use Cases:
# - Filter sales data by Region, Product Category, or Year
# - Compare performance across different time periods
# - Segment customer data by demographics
 
 
# =============================================================================
# Q12. Explain Python Integration in Power BI.
# =============================================================================
 
# Power BI supports Python scripting for advanced analytics, custom data transformations,
# and machine learning that go beyond Power BI's built-in capabilities.
 
# Where Python Can Be Used in Power BI:
# - Data Source    : Use Python scripts to import and generate datasets
# - Power Query    : Run Python for data transformation and cleaning
# - Visualizations : Create custom visuals using Python plotting libraries
 
# Common Python Libraries Used:
# - Pandas       : Data manipulation and cleaning (DataFrames)
# - NumPy        : Numerical computing and array operations
# - Matplotlib   : Static data visualizations and custom charts
# - Seaborn      : Statistical visualizations built on Matplotlib
# - Scikit-learn : Machine learning: regression, classification, clustering
# - Plotly       : Interactive charts and graphs
 
# Applications:
# - Predictive Analytics and forecasting
# - Machine Learning model integration
# - Statistical analysis (correlation, regression)
# - Advanced data cleaning and outlier detection
# - Custom visualizations not available in Power BI natively
 
 
# =============================================================================
# Q13. Steps to Integrate Python with Power BI.
# =============================================================================
 
# Step 1  : Install Python (version 3.x recommended from python.org)
# Step 2  : Install required libraries: pip install pandas matplotlib seaborn scikit-learn
# Step 3  : In Power BI Desktop, go to File > Options > Python scripting
# Step 4  : Set the Python home directory to your installed Python path
# Step 5  : Use Python as a data source: Get Data > Python Script
# Step 6  : Use Python in Power Query: Transform > Run Python Script
# Step 7  : Use Python visuals: From Visualizations pane, select Python Visual
# Step 8  : Write and paste Python script in the script editor area
# Step 9  : Press Run to generate the visualization or output
 
# Sample Python Visual Script:
#
# import matplotlib.pyplot as plt
# import pandas as pd
#
# # 'dataset' is the Power BI DataFrame automatically passed in
# fig, ax = plt.subplots()
# dataset.groupby('Category')['Sales'].sum().plot(kind='bar', ax=ax)
# plt.title('Sales by Category')
# plt.tight_layout()
# plt.show()
 
 
# =============================================================================
# Q14. What is Power BI Gateway?
# =============================================================================
 
# The Power BI Gateway is a software component that acts as a bridge between
# on-premise data sources and Power BI cloud services. It enables scheduled refresh
# of reports that use local databases, files, or servers.
 
# Types of Gateways:
# - On-premises data gateway (Standard mode) : Supports multiple users and data sources
# - On-premises data gateway (Personal mode) : For individual use only
 
# When is Gateway Needed?
# - When connecting to SQL Server, Oracle, or other local databases
# - When refreshing reports in Power BI Service that use on-premise data
# - When using DirectQuery with local data sources
 
 
# =============================================================================
# Q15. Explain Row-Level Security (RLS) in Power BI.
# =============================================================================
 
# Row-Level Security (RLS) is a feature in Power BI that restricts data access at
# the row level based on the logged-in user. Different users see different subsets
# of data from the same report.
 
# How RLS Works:
# - Define roles in Power BI Desktop using DAX filter expressions
# - Assign users or groups to those roles in Power BI Service
# - When the user views the report, filters are applied automatically
 
# Example DAX Filter for RLS:
# [Region] = USERNAME() OR [Region] = USERPRINCIPALNAME()
 
# Types of RLS:
# - Static RLS  : Fixed filter values per role
# - Dynamic RLS : Uses DAX functions like USERNAME() to filter dynamically
 
 
# =============================================================================
# Q16. What is DirectQuery vs Import Mode?
# =============================================================================
 
# Data Storage:
# - DirectQuery  : Data NOT stored in Power BI model
# - Import Mode  : Data IS copied into Power BI model
 
# Refresh:
# - DirectQuery  : Real-time – queries source directly
# - Import Mode  : Scheduled or manual refresh required
 
# Performance:
# - DirectQuery  : Slower (depends on source speed)
# - Import Mode  : Faster (in-memory processing)
 
# Data Size:
# - DirectQuery  : No size limit (large datasets)
# - Import Mode  : Limited to ~1 GB compressed
 
# DAX Support:
# - DirectQuery  : Limited DAX functions supported
# - Import Mode  : Full DAX support
 
# Best For:
# - DirectQuery  : Live operational dashboards
# - Import Mode  : Historical reporting and analysis
 
 
# =============================================================================
# Q17. What are KPIs and Cards in Power BI?
# =============================================================================
 
# KPI (Key Performance Indicator) and Card visuals are used to display single,
# important numeric values on a dashboard.
 
# Card Visual:
# - Displays a single number or text value
# - Example: Total Revenue: $5.2M
# - Useful for summary statistics at the top of a dashboard
 
# KPI Visual:
# - Shows a metric, a target value, and the trend status
# - Includes indicator (green/red) based on target vs actual
# - Requires: Value, Target, and Time Trend fields
 
 
# =============================================================================
# Q18. Explain the Power BI Report Lifecycle.
# =============================================================================
 
# Step 1  : Connect to Data Sources (databases, files, APIs)
# Step 2  : Transform Data using Power Query (ETL)
# Step 3  : Create Data Model (relationships, hierarchies)
# Step 4  : Write DAX Measures and Calculated Columns
# Step 5  : Build Visuals and Reports in Power BI Desktop
# Step 6  : Apply Filters, Slicers, and Drill-Down features
# Step 7  : Publish to Power BI Service (cloud)
# Step 8  : Share with users, configure Row-Level Security
# Step 9  : Schedule Data Refresh
# Step 10 : Monitor and maintain reports
 
 
# =============================================================================
# Q19. What is the Difference Between Power BI and Traditional BI Tools?
# =============================================================================
 
# Traditional BI tools (like Crystal Reports, Cognos, or MicroStrategy) require
# dedicated IT teams and have long development cycles. Power BI democratizes BI
# by making it accessible to business users.
 
# Development:
# - Traditional BI : Requires IT/developer involvement
# - Power BI       : Self-service; business users can build reports
 
# Deployment:
# - Traditional BI : On-premise, complex setup
# - Power BI       : Cloud-first, rapid deployment
 
# Cost:
# - Traditional BI : High licensing and infrastructure costs
# - Power BI       : Affordable subscription model
 
# Refresh:
# - Traditional BI : Batch processing, periodic
# - Power BI       : Near real-time refresh possible
 
# Collaboration:
# - Traditional BI : Limited sharing mechanisms
# - Power BI       : Easy sharing via cloud links and workspaces
 
# Learning Curve:
# - Traditional BI : Steep, requires training
# - Power BI       : Drag-and-drop interface, Excel-like
 
# Data Sources:
# - Traditional BI : Predefined connectors
# - Power BI       : 100+ connectors including REST APIs
 
 
# =============================================================================
# Q20. Explain the Concept of Data Refresh in Power BI.
# =============================================================================
 
# Data Refresh is the process of updating the dataset in Power BI Service so that
# reports reflect the latest data from the source systems. Since Import Mode copies
# data into the model, it must be periodically refreshed.
 
# Types of Refresh:
# - On-Demand Refresh   : Manually triggered by the user in Power BI Service
# - Scheduled Refresh   : Automatically triggered at set intervals (up to 8 times/day on Pro, 48 times/day on Premium)
# - Real-Time Refresh   : Used with DirectQuery or streaming datasets; no scheduled refresh needed
# - Incremental Refresh : Refreshes only new or changed data rows, not the entire dataset (efficient for large data)
 
# Prerequisites for Scheduled Refresh:
# - Dataset must be published to Power BI Service
# - Data source credentials must be configured
# - On-premises Gateway required for local data sources
 
 
# =============================================================================
# Q21. What are Workspaces in Power BI?
# =============================================================================
 
# Workspaces are collaborative environments in Power BI Service where teams can
# create, share, and manage reports, dashboards, and datasets together.
 
# Types of Workspaces:
# - My Workspace       : Personal space for individual users; cannot be shared
# - Shared Workspace   : Team collaboration space; supports multiple contributors
# - Premium Workspace  : Backed by dedicated capacity; allows sharing with free-license users
 
# Workspace Roles:
# - Admin       : Full control: manage members, delete workspace, publish apps
# - Member      : Create/edit content, publish apps, cannot manage members
# - Contributor : Create and edit reports and datasets; cannot publish apps
# - Viewer      : Read-only access to reports and dashboards
 
 
# =============================================================================
# Q22. What is the Role of Aggregations in Power BI?
# =============================================================================
 
# Aggregations in Power BI allow pre-summarized versions of large datasets to be
# cached and queried, dramatically improving performance for large-scale analytics.
 
# How Aggregations Work:
# - A summarized (aggregated) table is created from the detail table
# - Power BI automatically routes queries to the aggregated table when possible
# - If a query requires row-level detail, it falls back to the full detail table
 
# Benefits:
# - Reduces query time from minutes to seconds on large datasets
# - Works seamlessly with both Import and DirectQuery modes
# - Enables analytics on billion-row datasets on Power BI Premium
 
 
# =============================================================================
# Q23. Explain Hierarchies in Power BI.
# =============================================================================
 
# A Hierarchy in Power BI is a logical grouping of columns in a specific order
# that enables drill-down analysis. It allows users to navigate from a high-level
# summary to granular detail.
 
# Common Hierarchy Examples:
# - Date Hierarchy         : Year > Quarter > Month > Day
# - Geography Hierarchy    : Country > State > City > Postal Code
# - Product Hierarchy      : Category > Subcategory > Product Name
# - Organization Hierarchy : Division > Department > Employee
 
# How to Create a Hierarchy:
# - In the Fields pane, right-click a column > 'New hierarchy'
# - Drag additional fields into the hierarchy in the desired order
# - Use the visual's drill-down buttons to navigate the hierarchy in reports
 
# Drill Actions:
# - Drill Down      : Go one level deeper for the selected data point
# - Drill Up        : Return to the previous level
# - Expand All Down : Expand all data points to the next level simultaneously
 
 
# =============================================================================
# Q24. What is Power BI Embedded?
# =============================================================================
 
# Power BI Embedded is an Azure service that allows developers to integrate Power BI
# reports, dashboards, and visuals directly into custom applications, websites, or
# portals without requiring users to have a Power BI license.
 
# Key Characteristics:
# - Reports are embedded via iframes using REST APIs and JavaScript SDK
# - Authentication handled by the application (embed tokens)
# - Two embedding modes: Embed for your customers (app owns data) and Embed for your organization (user owns data)
# - Billed based on Azure capacity (A SKUs), not per user
 
# Use Cases:
# - SaaS vendors embedding analytics into their product
# - Portals showing analytics to external clients
# - Custom enterprise applications with integrated BI
 
 
# =============================================================================
# Q25. Explain the Concept of Bookmarks and Report Navigation in Power BI.
# =============================================================================
 
# Bookmarks capture the current state of a report page — including filter selections,
# slicer values, visual visibility, and scroll positions — so users can save and
# return to specific views.
 
# Types of Bookmarks:
# - Personal Bookmarks : Saved by individual viewers in Power BI Service (does not affect others)
# - Report Bookmarks   : Created by the report author in Desktop; embedded in the report
 
# Uses of Bookmarks:
# - Data Storytelling  : Guide viewers through a narrative with preset views
# - Toggle Visuals     : Show/hide visuals using buttons and bookmarks (e.g., show chart vs table)
# - Custom Navigation  : Build page navigation menus without using the default tab bar
# - Reset Filters      : Create a 'Reset to Default' button using a bookmark
 
 
# =============================================================================
# Q26. What is the Difference Between Filter Pane and Slicer?
# =============================================================================
 
# Visibility:
# - Filter Pane : Hidden panel (can be collapsed)
# - Slicer      : Visible visual on the report canvas
 
# User Access:
# - Filter Pane : Author-controlled (can restrict)
# - Slicer      : Always accessible to report viewers
 
# Scope:
# - Filter Pane : Page, report, or visual level filtering
# - Slicer      : Affects all visuals on the page by default
 
# Types:
# - Filter Pane : Basic, Advanced, Top N filtering
# - Slicer      : Dropdown, list, date range, slider
 
# Design:
# - Filter Pane : Not part of visual layout
# - Slicer      : Occupies space on the canvas; can be styled
 
# Cross-Page:
# - Filter Pane : Report-level filters apply to all pages
# - Slicer      : Slicers work only on their own page (unless synced)
 
# Sync:
# - Filter Pane : Not applicable
# - Slicer      : Slicer Sync panel can sync across pages
 
 
# =============================================================================
# Q27. What are Themes in Power BI?
# =============================================================================
 
# Themes in Power BI allow report authors to apply a consistent color palette, font,
# and visual formatting across an entire report in one click. They ensure visual
# consistency and support corporate branding.
 
# Types of Themes:
# - Built-in Themes    : Power BI provides default themes like Default, Classic, Colorblind safe, etc.
# - Custom JSON Themes : Authors can define a JSON file specifying colors, fonts, and visual defaults
 
# Theme JSON Structure (Key Elements):
# {
#     "name": "Corporate Theme",
#     "dataColors": ["#1F4E79", "#2E75B6", "#70AD47"],
#     "background": "#FFFFFF",
#     "foreground": "#333333",
#     "tableAccent": "#2E75B6"
# }
 
# Benefits:
# - Maintains brand consistency across all reports
# - Saves time — applies formatting to all visuals at once
# - Can be shared across teams as a .json file
 
 
# =============================================================================
# Q28. Explain Time Intelligence Functions in DAX.
# =============================================================================
 
# Time Intelligence functions in DAX allow calculations across time periods such as
# year-to-date totals, month-over-month comparisons, and rolling averages.
# They require a properly marked Date table in the data model.
 
# Prerequisites:
# - A dedicated Date/Calendar table in the data model
# - The Date table must be marked as a 'Date Table' in Power BI
# - The Date column must be of Date data type with no gaps
 
# Common Time Intelligence Functions:
# - TOTALYTD()           : TOTALYTD(SUM(Sales[Amount]), Dates[Date])                          --> Year-to-date total
# - TOTALQTD()           : TOTALQTD([Total Sales], Dates[Date])                               --> Quarter-to-date total
# - TOTALMTD()           : TOTALMTD([Total Sales], Dates[Date])                               --> Month-to-date total
# - SAMEPERIODLASTYEAR() : CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Dates[Date]))          --> Same period in prior year
# - DATEADD()            : CALCULATE([Total Sales], DATEADD(Dates[Date], -1, MONTH))          --> Shift by N periods
# - DATESYTD()           : CALCULATE([Sales], DATESYTD(Dates[Date]))                          --> All dates from year start to current
 
 
# =============================================================================
# Q29. What is a Star Schema and Why is it Preferred in Power BI?
# =============================================================================
 
# A Star Schema is a data modeling pattern where a central Fact table is surrounded
# by multiple Dimension tables, resembling a star shape. It is the recommended data
# model pattern for Power BI.
 
# Components:
# - Fact Table       : Contains measurable, quantitative data (sales amount, quantity, revenue).
#                      Has foreign keys pointing to dimension tables.
# - Dimension Tables : Contain descriptive attributes (customer name, product category, date).
#                      Usually smaller, denormalized tables.
 
# Example Star Schema:
# - Fact_Sales   : SalesID, DateKey, ProductKey, CustomerKey, Amount, Quantity
# - Dim_Date     : DateKey, Year, Quarter, Month, Day
# - Dim_Product  : ProductKey, ProductName, Category, Subcategory
# - Dim_Customer : CustomerKey, CustomerName, Region, Segment
 
# Why Star Schema is Preferred in Power BI:
# - Simpler relationships — Power BI's DAX engine is optimized for it
# - Faster query performance due to fewer joins
# - Easier to understand and maintain for report authors
# - Enables powerful filter propagation across dimensions
 
 
# =============================================================================
# Q30. What is the CALCULATE Function in DAX?
# =============================================================================
 
# CALCULATE is the most powerful and important function in DAX.
# It evaluates an expression in a modified filter context, allowing you to override
# or add filters to change what data is included in the calculation.
 
# Syntax:
# CALCULATE(Expression, Filter1, Filter2, ...)
 
# Key Concepts:
# - Filter Context : The set of filters currently applied to the data model
# - CALCULATE can ADD new filters, REPLACE existing ones, or REMOVE them using ALL()
# - It is used to build virtually every non-trivial DAX measure
 
# Examples:
# Sales only for the South region:
# South Sales = CALCULATE(SUM(Sales[Amount]), Region[Region] = "South")
#
# Sales ignoring all filters (grand total):
# All Sales = CALCULATE(SUM(Sales[Amount]), ALL(Sales))
#
# % of total contribution:
# Sales % = DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Sales)), 0)
 
# Common Modifier Functions Used with CALCULATE:
# - ALL()         : Removes all filters from a table or column
# - ALLEXCEPT()   : Removes all filters except specified columns
# - FILTER()      : Applies a row-by-row Boolean filter
# - KEEPFILTERS() : Adds filter without replacing existing context
 
 
# =============================================================================
# END OF FILE
# DVT ESA – Power BI Study Guide | 30 Questions | MTech Theoretical Coverage
# =============================================================================
