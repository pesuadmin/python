# PART 1 — POWER BI
# =============================================================================


# =============================================================================
# Q1. What is Power BI?
# =============================================================================

# Power BI is a Business Intelligence (BI) and Data Visualization tool developed by Microsoft.
# It enables users to connect to multiple data sources, transform data, create interactive
# reports and dashboards, and support data-driven decision-making across an organization.
# It converts raw data into meaningful, interactive dashboards and reports.

# Key Features:
# - Data visualization with interactive charts and graphs
# - Interactive dashboards for real-time insights
# - Real-time analytics and live data connections
# - Cloud integration via Power BI Service
# - Data sharing, collaboration, and role-based access
# - Support for 100+ data connectors (SQL, Excel, Web APIs, etc.)


# =============================================================================
# Q2. Explain the Components / Architecture of Power BI.
# =============================================================================

# Power BI has the following major components, each serving a specific purpose:

# Power BI Desktop       : Free Windows application to design reports and data models
# Power BI Service       : Cloud platform (app.powerbi.com) to publish, share, and collaborate
# Power BI Mobile        : iOS/Android apps to view and annotate reports on the go
# Power BI Gateway       : On-premises bridge; refreshes on-prem data sources from cloud service
# Power BI Embedded      : API/developer tool to embed Power BI reports into custom apps
# Power BI Report Server : On-premises server to host reports on local infrastructure
# Power BI Premium       : Licensing tier for dedicated capacity, paginated reports, AI features

# Architecture Layers:
# 1. Data Layer           : Connects to 100+ sources (Excel, SQL Server, Azure, web APIs, Salesforce)
#                           via connectors. Data is imported into an in-memory columnar engine (VertiPaq).
# 2. Transformation Layer : Data is cleaned, shaped, and transformed using Power Query Editor (M Language).
#                           Steps are recorded and reproducible.
# 3. Data Modeling Layer  : Relationships between tables are defined.
#                           DAX is used to create calculated columns, measures, and KPIs.
# 4. Visualization Layer  : Interactive charts, tables, maps, and custom visuals are built in Desktop.
# 5. Service/Sharing Layer: Reports published to Power BI Service (cloud); workspaces, dashboards,
#                           and scheduled refresh managed. Row-Level Security controls access.
# 6. Consumption Layer    : End users consume reports via browser (Power BI Service) or Mobile apps.

# Underlying Engine:
# - VertiPaq: a columnar, in-memory compression engine.
#   Data is compressed column-by-column allowing extremely fast aggregations.
#   Uses dictionary encoding + run-length encoding; often achieves 10:1 compression ratios.


# =============================================================================
# Q3. What is Power BI Embedded?
# =============================================================================

# Power BI Embedded is a Microsoft Azure service that allows developers to embed interactive
# Power BI reports and dashboards into custom web or mobile applications,
# without requiring users to have a Power BI license.
# It uses REST APIs and JavaScript SDK.

# Key Characteristics:
# - Reports are embedded via iframes using REST APIs and JavaScript SDK
# - Authentication handled by the application (embed tokens)
# - Two embedding modes:
#   - Embed for your customers (app owns data)
#   - Embed for your organization (user owns data)
# - Billed based on Azure capacity (A SKUs), not per user

# Use Cases:
# - SaaS vendors embedding analytics into their product
# - Portals showing analytics to external clients
# - Custom enterprise applications with integrated BI


# =============================================================================
# Q4. What is Power Query? What is it used for?
# =============================================================================

# Power Query is the data transformation and preparation tool embedded in Power BI.
# It is used to extract, clean, shape, and transform raw data from multiple sources
# before loading it into the data model.
# It operates as a graphical ETL (Extract, Transform, Load) tool.
# Every transformation step is recorded as M language (Power Query Formula Language) code,
# visible in the Applied Steps pane.

# Common Power Query Operations:
# - Remove duplicates and null values
# - Filter rows and columns based on conditions
# - Merge and append multiple tables
# - Split columns (e.g., full name into first/last)
# - Change data types and rename columns
# - Pivot and unpivot data
# - Group by and aggregate data
# - Fill Down/Up: propagates non-null values to fill blanks in a column
# - Replace Values: finds and replaces specific text/numbers
# - Custom Column: add calculated column using M syntax, e.g., [Price] * [Quantity]

# M Language Examples:
# = Table.AddColumn(Source, "FullName", each [FirstName] & " " & [LastName])
# = Table.SelectRows(Source, each [Sales] > 1000)

# Merge vs Append:
# - Merge  : combines tables horizontally (like SQL JOIN) – matches rows based on a key
# - Append : combines tables vertically (like SQL UNION ALL) – stacks rows one below the other


# =============================================================================
# Q5. Explain the ETL Process in Power BI.
# =============================================================================

# ETL stands for Extract, Transform, and Load. It is the backbone of data preparation in Power BI.

# Extract   : Collect raw data from various sources: databases, Excel, APIs, web
# Transform : Clean and reshape data using Power Query Editor
# Load      : Load the prepared data into the Power BI data model for reporting

# Benefits of ETL in Power BI:
# - Improves data quality and consistency
# - Reduces errors in reporting
# - Supports data from multiple heterogeneous sources
# - Automates repetitive data preparation tasks


# =============================================================================
# Q6. Explain Data Modeling in Power BI.
# =============================================================================

# Data Modeling is the process of defining relationships between tables so that data
# can be efficiently queried and analyzed across multiple tables.

# Types of Relationships:
# - One-to-One (1:1)   : Each row in Table A matches exactly one row in Table B. Rare.
# - One-to-Many (1:N)  : One row in Table A relates to many rows in Table B (most common)
#                        e.g., one Customer -> many Orders
# - Many-to-One (*:1)  : Same as above, viewed from the other side
# - Many-to-Many (M:N) : Multiple rows on both sides; requires bridge table or special handling

# Key Concepts:
# - Star Schema           : Fact table at center connected to dimension tables (recommended)
# - Snowflake Schema      : Extended star with normalized dimensions
# - Cross-filter Direction: Single vs. Both (bidirectional filtering)
#   - Single: Filters flow from one side only (from 1 side to * side). Standard and recommended.
#   - Both:   Filters propagate in both directions. Can cause ambiguous filter paths. Use cautiously.
# - Active vs. Inactive Relationships: Only one active relationship allowed between two tables at a time

# Fact Table vs Dimension Table:
# - Fact Table      : Stores measurable, quantitative data (sales amount, quantity ordered, revenue).
#                     Has many rows and contains foreign keys to dimension tables.
# - Dimension Table : Stores descriptive, categorical attributes (Customer Name, Product Category, Date).
#                     Smaller, fewer rows, provides context to the facts.

# Star Schema Example:
# - Fact_Sales   : SalesID, DateKey, ProductKey, CustomerKey, Amount, Quantity
# - Dim_Date     : DateKey, Year, Quarter, Month, Day
# - Dim_Product  : ProductKey, ProductName, Category, Subcategory
# - Dim_Customer : CustomerKey, CustomerName, Region, Segment

# Why Star Schema is Preferred:
# - Simpler relationships — Power BI's DAX engine is optimized for it
# - Faster query performance due to fewer joins
# - Easier to understand and maintain for report authors
# - Enables powerful filter propagation across dimensions

# Benefits of Data Modeling:
# - Enables complex cross-table analysis
# - Reduces data redundancy
# - Improves report performance


# =============================================================================
# Q7. What is DAX? Explain key functions.
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
# - SUM()        : SUM(Sales[Amount])                                  --> Adds all values in a column
# - COUNT()      : COUNT(Orders[OrderID])                              --> Counts rows with non-blank values
# - AVERAGE()    : AVERAGE(Sales[Price])                               --> Calculates average
# - CALCULATE()  : CALCULATE(SUM(Sales[Amount]), Region='South')       --> Evaluates with modified filter context
# - IF()         : IF(Sales[Amount]>1000, 'High', 'Low')               --> Conditional logic
# - RELATED()    : RELATED(Product[Category])                          --> Fetches value from related table
# - DATEADD()    : DATEADD(Dates[Date], -1, YEAR)                      --> Time intelligence shift
# - DIVIDE()     : DIVIDE([Profit], [Sales], 0)                        --> Safe division (avoids divide-by-zero)
# - RANKX()      : RANKX(ALL(Products[Product]), [Total Sales])        --> Rank measure across a table
# - ALL()        : ALL(Products)                                        --> Removes all filters from a table/column
# - ALLEXCEPT()  : ALLEXCEPT(Sales, Sales[Region])                     --> Removes all filters except specified columns
# - FILTER()     : FILTER(Sales, Sales[Amount] > 1000)                 --> Row-by-row Boolean filter
# - KEEPFILTERS(): KEEPFILTERS(Sales[Region] = "South")                --> Adds filter without replacing existing context

# Example DAX Measures:
# Total Sales    = SUM(Sales[Amount])
# Profit Margin  = DIVIDE([Total Profit], [Total Sales], 0)
# YTD Sales      = TOTALYTD(SUM(Sales[Amount]), Dates[Date])
# LY Sales       = CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Dates[Date]))
# YoY Growth %   = DIVIDE([Total Sales] - [LY Sales], [LY Sales], 0)
# Running Total  = CALCULATE(SUM(Sales[Amount]), FILTER(ALL(Dates), Dates[Date] <= MAX(Dates[Date])))
# Sales Rank     = RANKX(ALL(Products[Product]), [Total Sales])
# % of Total     = DIVIDE([Total Sales], CALCULATE([Total Sales], ALL(Products)))


# =============================================================================
# Q8. Difference Between Measure and Calculated Column in DAX.
# =============================================================================

# Calculation:
# - Measure           : Evaluated dynamically at query time
# - Calculated Column : Evaluated row by row at data refresh

# Storage:
# - Measure           : NOT stored in the model (computed in memory)
# - Calculated Column : Stored in the model (occupies memory)

# Context:
# - Measure           : Responds to report filters and slicers
# - Calculated Column : Does not respond to filters dynamically

# Use Case:
# - Measure           : Aggregations: totals, averages, ratios
# - Calculated Column : Row-level logic: profit per row, category flag

# Example:
# - Measure           : Total Sales = SUM(Sales[Amount])
# - Calculated Column : Profit = Sales[Revenue] - Sales[Cost]

# Performance:
# - Measure           : Better for large datasets
# - Calculated Column : Increases model size

# Key Rule: Use measures for aggregations; use calculated columns for row-level attributes.


# =============================================================================
# Q9. Explain Filter Context and Row Context in DAX.
# =============================================================================

# Row Context:
# - Exists when DAX iterates over a table row by row.
# - Automatically available in calculated columns and iterator functions (SUMX, AVERAGEX).
# - At each row, the current row's values are accessible.
# - Example: Profit = Sales[Revenue] - Sales[Cost]  (references current row values)

# Filter Context:
# - The set of active filters applied to the data at any point in time.
# - Comes from slicers, visual filters, row/column headers in a matrix, CALCULATE modifiers.
# - A measure always evaluates within the current filter context.
# - Example: Total Sales = SUM(Sales[Amount])
#   If report filtered to "Region = West", the measure only sums West sales.

# CALCULATE – The Most Important DAX Function:
# - Evaluates an expression in a modified filter context.
# - It can ADD new filters, REPLACE existing ones, or REMOVE them using ALL()
# - Example: South Sales = CALCULATE(SUM(Sales[Amount]), Region[Region] = "South")
#   This overrides any existing Region filter and applies only the South filter.
# - Powers: (1) override existing filters, (2) add new filters,
#   (3) row context to filter context transition (CONTEXT TRANSITION),
#   (4) all time intelligence functions and complex business logic.

# SUMX vs SUM:
# - SUM([Column])         : Simply adds values in a single column.
# - SUMX(Table, Expression): Iterates row by row, evaluates expression per row, then sums results.
#   Example: Total Revenue = SUMX(Sales, Sales[Quantity] * Sales[UnitPrice])
#   Use when the value must be computed per row first before summing.

# ALL() in DAX:
# - Removes filters from a table or column, spanning the full dataset.
# - Example: Market Share = DIVIDE([Sales], CALCULATE([Sales], ALL(Products)))
#   The denominator uses ALL(Products) to get total sales across all products.
# - Essential for % of total, rankings, and ratio calculations.


# =============================================================================
# Q10. Explain Time Intelligence Functions in DAX.
# =============================================================================

# Time Intelligence functions allow calculations across time periods.
# They require a properly marked Date table in the data model.

# Prerequisites:
# - A dedicated Date/Calendar table in the data model
# - The Date table must be marked as a 'Date Table' in Power BI
# - The Date column must be of Date data type with no gaps

# Functions:
# - TOTALYTD()            : TOTALYTD(SUM(Sales[Amount]), Dates[Date])                          --> Year-to-date total
# - TOTALQTD()            : TOTALQTD([Total Sales], Dates[Date])                               --> Quarter-to-date total
# - TOTALMTD()            : TOTALMTD([Total Sales], Dates[Date])                               --> Month-to-date total
# - SAMEPERIODLASTYEAR()  : CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Dates[Date]))          --> Same period prior year
# - DATEADD()             : CALCULATE([Total Sales], DATEADD(Dates[Date], -1, MONTH))          --> Shift by N periods
# - DATESYTD()            : CALCULATE([Sales], DATESYTD(Dates[Date]))                          --> All dates from year start
# - PARALLELPERIOD()      : Shifts entire period (e.g., whole prior month)
# - DATESINPERIOD()       : Returns dates in a rolling window

# Mnemonic: "DS PPTT DD"
# Dates, Same Period, Parallel Period, Total YTD/MTD/QTD, Dates YTD, DatesinPeriod


# =============================================================================
# Q11. What are Visualizations in Power BI?
# =============================================================================

# Visualizations are graphical representations of data that communicate insights effectively.
# Power BI offers 30+ built-in visual types and supports custom visuals from AppSource.

# Visual Type         | Best Used For                   | Notes
# Bar / Column Chart  : Comparing categories             | Bar = horizontal; Column = vertical
# Line Chart          : Trends over time                 | Use with date/time axis
# Pie / Donut Chart   : Part-to-whole proportions        | Max 5-6 slices; avoid for many categories
# Scatter Plot        : Correlation between two measures | Add play axis for animated over time
# Map / Filled Map    : Geographical data                | Requires location data (country, city, lat/long)
# Matrix              : Cross-tabulation (pivot table)   | Rows, Columns, Values; drill-down enabled
# Card / Multi-row    : Single KPI display               | Great for executive summaries
# Gauge               : Progress toward a target         | Needs min, max, target values
# Treemap             : Hierarchical proportion          | Good for nested categories
# Waterfall           : Incremental changes (P&L)        | Shows increases/decreases from a baseline
# Funnel              : Process stages / conversion      | Sales pipeline, recruitment funnel
# Decomposition Tree  : AI-powered root cause analysis   | Drills into drivers automatically
# Key Influencers     : AI – what drives a metric        | Uses ML to identify influencing factors

# Slicer:
# - A visual filter control that allows report users to interactively filter all connected visuals.
# - Can be configured as: dropdown, list, date range slider, tile (button-style).
# - Slicers can be synced across multiple report pages using the "Sync Slicers" feature.

# Types of Slicers:
# - Dropdown Slicer      : Select one or multiple values from a list
# - List Slicer          : Checkboxes for multi-select
# - Between Slicer       : For numeric or date ranges
# - Relative Date Slicer : Last N days, this month, this year, etc.
# - Tile Slicer          : Button-style selection


# =============================================================================
# Q12. Drill-Down vs Drill-Through in Power BI.
# =============================================================================

# Drill-Down:
# - Navigates from a higher level of a hierarchy to a lower level within the SAME visual.
# - Example: Date hierarchy (Year -> Quarter -> Month -> Day).
#   Clicking on a year drills down to show quarters within the same chart.
# - Visual stays on the same page but shows more granular data.

# Drill-Through:
# - Navigates from one report page to a DIFFERENT detail page, carrying filter context.
# - Example: Right-click on a customer in a summary page
#   -> "Drill through to Customer Detail" page, which shows all orders for that customer.
# - Target page must have Drill-through fields configured. A back button is auto-generated.

# Key Difference:
# - Drill-down  : Same visual, different hierarchy level.
# - Drill-through: Different page with detail for a selected value.


# =============================================================================
# Q13. Differentiate Between Report and Dashboard in Power BI.
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
# - Report    : Power BI Desktop or Power BI Service
# - Dashboard : Power BI Service only

# Drill-Down:
# - Report    : Full drill-down support
# - Dashboard : Limited drill-down

# Interactivity:
# - Report    : Highly interactive (slicers, filters, cross-filtering)
# - Dashboard : Pinned tiles, less interactive

# Data Source:
# - Report    : One dataset per page
# - Dashboard : Can combine tiles from multiple reports/datasets

# Tiles:
# - Report    : Not applicable
# - Dashboard : Pinned visuals become "tiles"

# Sharing:
# - Report    : Share via workspace, app, link
# - Dashboard : Share directly

# Alerts:
# - Report    : Not supported
# - Dashboard : Data alerts on KPI tiles

# Pinning:
# - Pinning is the process of adding a visual from a report to a Dashboard as a tile.
# - Multiple visuals from different reports can be pinned to the same dashboard.


# =============================================================================
# Q14. Explain Interactive Dashboards in Power BI.
# =============================================================================

# Interactive Dashboards allow users to explore and analyze data dynamically
# without needing technical skills. Multiple visuals respond to user actions.

# Key Interactive Features:
# - Filters         : Narrow down data displayed across the entire report page
# - Slicers         : Visual filter controls (dropdown, buttons, date range)
# - Drill-Down      : Navigate from summary to detail (e.g., Year > Quarter > Month)
# - Drill-Through   : Jump to a detail page based on selected data point
# - Cross-Filtering : Clicking one visual automatically filters all related visuals
# - Bookmarks       : Save specific view states for storytelling
# - Tooltips        : Show additional info on hover

# Bookmarks:
# - Capture the current state of a report page (filter selections, slicer values,
#   visual visibility, scroll positions).
# - Personal Bookmarks : Saved by individual viewers in Service (does not affect others)
# - Report Bookmarks   : Created by report author in Desktop; embedded in the report
# - Uses: Data Storytelling, Toggle Visuals, Custom Navigation, Reset Filters button

# Benefits:
# - Empowers non-technical users to explore data independently
# - Supports faster, data-driven decisions
# - Reduces need for multiple static reports


# =============================================================================
# Q15. What are KPIs and Cards in Power BI?
# =============================================================================

# Card Visual:
# - Displays a single number or text value
# - Example: Total Revenue: $5.2M
# - Useful for summary statistics at the top of a dashboard

# KPI Visual:
# - Shows a metric, a target value, and the trend status
# - Includes indicator (green/red) based on target vs actual
# - Requires: Value, Target, and Time Trend fields


# =============================================================================
# Q16. What are Data Sources & Connectivity Modes in Power BI?
# =============================================================================

# Power BI supports three data connectivity modes: Import, DirectQuery, and Live Connection.

# Import Mode:
# - Data is COPIED into Power BI's in-memory VertiPaq engine.
# - Reports are extremely fast (queries run on in-memory data).
# - Full DAX features and transformations supported.
# - Refresh must be scheduled (up to 8/day for Pro, 48/day for Premium).
# - Suitable when dataset is under 1GB (Pro) or 10GB (Premium).
# - Best for: historical reporting, analysis.

# DirectQuery Mode:
# - Data is NOT stored locally. Every visual interaction sends a live query to the source.
# - Always shows current data.
# - Slower due to network round trips; fewer transformations supported; limited DAX.
# - No size limit (large datasets).
# - Best for: live operational dashboards, real-time data.

# Live Connection:
# - Connects to SSAS, Power BI datasets; no local copy made.
# - No additional modeling allowed in Desktop.
# - Best for: centralized enterprise models.

# Composite Model:
# - Combines Import and DirectQuery tables in a single report.
# - Example: large fact table on DirectQuery (freshness) + small dimension tables imported (speed).

# Key Difference:
# - Import    : speed + full features; data not always current
# - DirectQuery: live data + no storage limits; slower performance


# =============================================================================
# Q17. What is Scheduled Refresh? What is the Gateway?
# =============================================================================

# Scheduled Refresh:
# - Automated process of re-importing data from source systems at set intervals.
# - Keeps reports up-to-date without manual intervention.
# - Power BI Pro    : up to 8 refreshes/day
# - Power BI Premium: up to 48 refreshes/day
# - Requires a Gateway if data is on-premises.

# Types of Refresh:
# - On-Demand Refresh   : Manually triggered by the user in Power BI Service
# - Scheduled Refresh   : Automatically triggered at set intervals
# - Real-Time Refresh   : Used with DirectQuery or streaming datasets; no scheduled refresh needed
# - Incremental Refresh : Refreshes only new or changed data rows; efficient for large data

# Prerequisites for Scheduled Refresh:
# - Dataset must be published to Power BI Service
# - Data source credentials must be configured
# - On-premises Gateway required for local data sources

# On-premises Data Gateway:
# - Acts as a bridge between Power BI Service (cloud) and on-premises data sources.
# - Personal Mode Gateway   : Single-user; only for Import datasets; not shareable
# - Standard Mode (Enterprise) Gateway: Shared across organization;
#   supports DirectQuery, Live Connection, Import; enterprise deployments

# When is Gateway Needed?
# - When connecting to SQL Server, Oracle, or other local databases
# - When refreshing reports in Power BI Service that use on-premise data
# - When using DirectQuery with local data sources


# =============================================================================
# Q18. Explain Row-Level Security (RLS) in Power BI.
# =============================================================================

# Row-Level Security (RLS) restricts data access at the row level based on the logged-in user.
# Different users see different subsets of data from the same report.
# Defined using DAX filter expressions applied to table roles.

# How RLS Works:
# - Step 1: In Power BI Desktop, go to Modeling -> Manage Roles -> Create Role.
# - Step 2: Define a DAX filter on a table.
#   Example: [Region] = "South"  (this role only sees South region data)
# - Step 3: For dynamic RLS, use USERPRINCIPALNAME() to match the logged-in user's email.
#   Example: [Email] = USERPRINCIPALNAME()
# - Step 4: Publish to Power BI Service -> dataset settings -> assign users/groups to roles.

# Example DAX Filter for RLS:
# [Region] = USERNAME() OR [Region] = USERPRINCIPALNAME()

# Types of RLS:
# - Static RLS  : Fixed filter values per role (hardcoded region/department).
#                 New users must be manually assigned to roles.
# - Dynamic RLS : Uses USERPRINCIPALNAME() to look up the logged-in user in a mapping table
#                 and filter data accordingly — far more scalable for hundreds of users.


# =============================================================================
# Q19. What are Workspaces in Power BI? What is a Power BI App?
# =============================================================================

# Workspaces are collaborative environments in Power BI Service where teams store
# and work with datasets, reports, and dashboards together.

# Types of Workspaces:
# - My Workspace      : Personal sandbox for individual development. Not shareable.
# - App Workspace     : Collaborative space for teams. Supports role-based access.
# - Premium Workspace : Backed by dedicated capacity; allows sharing with free-license users.

# Workspace Roles:
# - Admin       : Full control: manage members, delete workspace, publish apps
# - Member      : Create/edit content, publish apps, cannot manage members
# - Contributor : Create and edit reports and datasets; cannot publish apps
# - Viewer      : Read-only access to reports and dashboards

# Power BI Apps:
# - A bundled, read-only collection of dashboards and reports published from a workspace.
# - Recommended way to distribute finished content to end users.
# - Workspace members work on the content; app consumers only see the published version.
# - Apps can be updated without disrupting consumers.

# Dataflow:
# - A cloud-based ETL artifact created in Power BI Service using Power Query Online.
# - Centralizes and reuses data preparation logic across multiple datasets.
# - Stored in Azure Data Lake. Multiple datasets can connect to the same dataflow.


# =============================================================================
# Q20. What is the Difference Between Power BI and Traditional BI Tools?
# =============================================================================

# Traditional BI tools (Crystal Reports, Cognos, MicroStrategy) require dedicated IT teams.
# Power BI democratizes BI by making it accessible to business users.

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
# Q21. What are Hierarchies in Power BI?
# =============================================================================

# A Hierarchy is a logical grouping of columns in a specific order that enables drill-down analysis.
# Allows users to navigate from high-level summary to granular detail.

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
# Q22. What is the Role of Aggregations in Power BI?
# =============================================================================

# Aggregations allow pre-summarized versions of large datasets to be cached and queried,
# dramatically improving performance for large-scale analytics.

# How Aggregations Work:
# - A summarized (aggregated) table is created from the detail table.
# - Power BI automatically routes queries to the aggregated table when possible.
# - If a query requires row-level detail, it falls back to the full detail table.

# Benefits:
# - Reduces query time from minutes to seconds on large datasets
# - Works seamlessly with both Import and DirectQuery modes
# - Enables analytics on billion-row datasets on Power BI Premium


# =============================================================================
# Q23. What is the Difference Between Filter Pane and Slicer?
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
# - Slicer      : Work only on their own page (unless synced with Slicer Sync panel)

# Sync:
# - Filter Pane : Not applicable
# - Slicer      : Slicer Sync panel can sync across pages


# =============================================================================
# Q24. What are Themes in Power BI?
# =============================================================================

# Themes allow report authors to apply a consistent color palette, font, and visual formatting
# across an entire report in one click. Ensures visual consistency and supports corporate branding.

# Types of Themes:
# - Built-in Themes    : Default, Classic, Colorblind safe, etc.
# - Custom JSON Themes : Authors define a JSON file specifying colors, fonts, and visual defaults

# Theme JSON Structure:
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
# Q25. Explain Python Integration in Power BI.
# =============================================================================

# Power BI supports Python scripting for advanced analytics, custom data transformations,
# and machine learning beyond Power BI's built-in capabilities.

# Where Python Can Be Used:
# - Data Source    : Use Python scripts to import and generate datasets (Get Data > Python Script)
# - Power Query    : Run Python for data transformation and cleaning (Transform > Run Python Script)
# - Visualizations : Create custom visuals using Python plotting libraries (Python Visual)

# Steps to Integrate Python:
# - Step 1 : Install Python (version 3.x recommended from python.org)
# - Step 2 : Install required libraries: pip install pandas matplotlib seaborn scikit-learn
# - Step 3 : In Power BI Desktop, go to File > Options > Python scripting
# - Step 4 : Set the Python home directory to your installed Python path
# - Step 5 : Use Python as a data source: Get Data > Python Script
# - Step 6 : Use Python in Power Query: Transform > Run Python Script
# - Step 7 : Use Python visuals: From Visualizations pane, select Python Visual
# - Step 8 : Write and paste Python script in the script editor area
# - Step 9 : Press Run to generate the visualization or output

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

# Sample Python Visual Script:
# import matplotlib.pyplot as plt
# import pandas as pd
# fig, ax = plt.subplots()
# dataset.groupby('Category')['Sales'].sum().plot(kind='bar', ax=ax)
# plt.title('Sales by Category')
# plt.tight_layout()
# plt.show()


# =============================================================================
# Q26. Explain the Power BI Report Lifecycle.
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


# PART 2 — TABLEAU



# =============================================================================
# Q27. What is Tableau? Explain its Architecture.
# =============================================================================

# Tableau is a leading data visualization and business intelligence platform that enables
# users to connect to virtually any data source and create interactive, shareable visualizations.
# Known for its drag-and-drop interface, speed, and VizQL query language.

# VizQL (Visual Query Language):
# - Tableau's proprietary technology that automatically translates drag-and-drop actions on
#   the canvas into SQL-like queries sent to the data source.
# - When a user drags a field to Rows or Columns, VizQL generates the necessary query.
# - Makes Tableau highly intuitive — no SQL knowledge required for basic analysis.

# Architecture Layers:
# 1. Data Layer          : Connects to 80+ data sources via native connectors.
#                          Data can be extracted (.hyper files) or queried live.
# 2. VizQL Engine        : Core engine that translates visual interactions into optimized queries.
#                          Manages communication between frontend canvas and data layer.
# 3. Application Server  : In Tableau Server/Online: handles authentication, permissions,
#                          scheduling, and API requests.
# 4. Data Server         : Manages centralized Published Data Sources so multiple workbooks
#                          share one connection definition.
# 5. Repository (PostgreSQL): Stores metadata: workbook definitions, user permissions, schedules.
# 6. Presentation Layer  : Interactive worksheets, dashboards, and stories rendered in
#                          Tableau Desktop, Tableau Server, or Tableau Online (browser).


# =============================================================================
# Q28. Explain the Tableau Product Family.
# =============================================================================

# Tableau Desktop             : Primary authoring tool. Create workbooks, dashboards, stories.
#                               Available as Creator or Explorer license.
# Tableau Public              : Free version. Workbooks saved to Tableau Public cloud (publicly accessible).
#                               No private storage.
# Tableau Server              : On-premises enterprise platform for publishing, sharing, managing workbooks.
# Tableau Online (Tableau Cloud): Cloud-hosted version of Tableau Server. No infrastructure management.
# Tableau Prep Builder        : ETL tool for data cleaning and shaping. Creates Prep Flows (.tfl/.tflx).
# Tableau CRM (Einstein Analytics): AI-powered analytics for Salesforce data. Now called CRM Analytics.
# Tableau Reader              : Free viewer for .twbx files. Cannot create or edit.
# Tableau Mobile              : iOS/Android app for viewing published content from Server/Online.

# .twb vs .twbx:
# - .twb  (Tableau Workbook)          : Contains only the workbook definition (XML), no data.
#                                       Requires connection to data source to open. Small file size.
# - .twbx (Tableau Packaged Workbook) : Contains workbook + all data extracts and images bundled.
#                                       Self-contained; shareable without access to original source.
#                                       Use .twbx for sharing with external users.


# =============================================================================
# Q29. Explain Live Connection vs Extract in Tableau.
# =============================================================================

# Live Connection:
# - Tableau directly queries the data source in real time.
# - Every interaction sends a query to the database.
# - Always reflects the latest data.
# - Performance depends on the source database.
# - Best for small to medium databases with fast query response and real-time freshness needs.

# Extract (.hyper file):
# - A snapshot of data is copied into Tableau's highly optimized columnar store (.hyper engine).
# - Queries run on the local extract, making it extremely fast.
# - Can be filtered to include only relevant data (reducing size).
# - Must be refreshed (manually or on schedule) to reflect new data.
# - Best for large or slow data sources, or when working offline.

# Key Decision:
# - Live    : Always current; speed depends on source.
# - Extract : Fast performance; not always current.

# Hyper Extract:
# - Tableau's .hyper format (introduced in Tableau 10.5) is a high-performance in-memory
#   columnar data store. Replaced the older .tde format.
# - Supports incremental extract refresh (only new/changed rows added).
# - Handles billions of rows efficiently.
# - Allows full and incremental refresh modes.


# =============================================================================
# Q30. Explain Dimensions, Measures, and the Tableau Interface.
# =============================================================================

# Dimensions (Blue Pills):
# - Categorical or discrete fields used for grouping/filtering.
# - Examples: Customer Name, Category, Region, Date (as discrete).
# - Produces headers in the view; adds a categorical axis.

# Measures (Green Pills):
# - Numeric fields that can be aggregated.
# - Examples: Sales, Profit, Quantity.
# - Produces an axis with a range of values.

# Discrete vs Continuous:
# - Discrete (Blue) : Finite set of distinct values. Creates headers/labels.
#                     Example: Region, Quarter (as text), Customer Segment.
# - Continuous (Green): Infinite range on a number line. Creates axes with min-max scale.
#                     Example: Sales, Date (as continuous timeline).
# - Right-click any pill to switch between discrete/continuous.

# Tableau Interface Elements:
# - Rows Shelf    : Fields placed here define the rows/y-axis of the view
# - Columns Shelf : Fields placed here define the columns/x-axis of the view
# - Marks Card    : Controls Color, Size, Label, Detail, Tooltip, Shape of marks
#   - Adding a dimension to Color: each value gets a distinct color
#   - Adding a measure to Size: marks larger/smaller based on value
# - Pages Shelf   : Creates an animated sequence of views; one per value of the field
# - Filters Shelf : Restricts which data is included in the view
# - Show Me       : Smart recommendation panel suggesting appropriate chart types


# =============================================================================
# Q31. Explain Calculated Fields, Table Calculations, and LOD Expressions in Tableau.
# =============================================================================

# 3 Types of Calculations in Tableau:
# - Basic Calculated Fields : Row-level; computed at the data source level
# - Table Calculations      : Computed on aggregated viz data (front end, not database)
# - LOD Expressions         : Control the granularity of aggregation

# Calculated Field:
# - A new field created using a formula in Tableau's formula editor.
# - Example: Profit Ratio = SUM([Profit]) / SUM([Sales])
# - Can be dimensions or measures; appear in the Data Pane for reuse.

# LOD (Level of Detail) Expressions:
# - Let you compute aggregations at a different granularity than the current view.

# FIXED:
# - Computes at a specific dimension, completely ignoring the view's level of detail
#   and most filters (except context filters).
# - Example: {FIXED [Customer ID] : SUM([Sales])}
#   Gives total sales per customer, regardless of what's on the view.
# - Most common: customer lifetime value, first purchase date, cohort analysis.

# INCLUDE:
# - Computes at a finer granularity than the view by including an additional dimension.
# - Example: {INCLUDE [Order ID] : AVG([Sales])}
#   Average sales per order, even if Order ID isn't in the view.

# EXCLUDE:
# - Computes at a coarser granularity by removing a dimension from the current level.
# - Example: {EXCLUDE [Region] : SUM([Sales])}
#   Grand total sales ignoring Region; useful to compute % of total.

# LOD Examples:
# {FIXED [Customer ID] : MIN([Order Date])}                       --> Customer first purchase date
# SUM([Sales]) / {EXCLUDE [Region] : SUM([Sales])}               --> Sales as proportion
# {INCLUDE [Order ID] : AVG([Profit])}                           --> Average order profit

# Table Calculations:
# - Computed on the aggregated data already in the view; run in Tableau's front end.
# - Running Total     : Cumulative sum along rows/columns
# - Percent of Total  : Each value as % of the grand total
# - Difference / % Difference: Change from previous value (month-over-month)
# - Rank              : Assigns ordinal rank to values
# - Moving Average    : Rolling average over N periods
# - Index / Size      : Row number within a partition
# - Scope: controlled by "compute along" (Table, Pane, Cell, specific dimension)


# =============================================================================
# Q32. Explain the Order of Operations (Filter Order) in Tableau.
# =============================================================================

# Tableau evaluates filters in this strict order:
# 1. Extract Filters          : Limits rows/columns included in .hyper extract
# 2. Data Source Filters      : Applied at connection level; affects all sheets
# 3. Context Filters          : Creates a temp table; highest priority regular filter
# 4. FIXED LOD Filters        : Respect context filters; ignore dimension filters
# 5. Dimension Filters        : Filters categorical values (include/exclude categories)
# 6. Measure Filters          : Filters on aggregated numeric ranges
# 7. Table Calculation Filters: Applied last — see all data

# Mnemonic: "Every Data Can Filter Dimensions Methodically Through Carefully"
# Extract -> Data Source -> Context -> FIXED LOD -> Dimension -> Measure -> Table Calc

# Context Filter:
# - A filter Tableau processes before all other filters, creating a temporary dataset.
# - Needed when combining a Top N filter with a dimension filter.
# - Without context: Top N is computed from all data, then dimension filter applied,
#   possibly giving fewer than N results.
# - With context: Top N is computed from the filtered subset — correct behavior.
# - Also speeds up performance with large datasets.

# Types of Filters in Tableau:
# - Extract Filter            : Limits rows/columns in .hyper extract; reduces extract size
# - Data Source Filter        : Applied at connection level; organization-wide row restriction
# - Context Filter            : Creates temporary table; makes Top N + filter work correctly
# - Dimension Filter          : Filters categorical values; show only specific regions, products
# - Measure Filter            : Filters on aggregated numeric ranges; Sales > 10,000
# - Table Calculation Filter  : Filters after table calcs are computed; hide ranks above threshold
# - Quick Filter (Filter Card): Interactive filter on dashboard for end-user control


# =============================================================================
# Q33. Explain Chart Types in Tableau and the Dual-Axis Chart.
# =============================================================================

# Chart Type           | Requires                     | Purpose
# Bar Chart            : 1 dim + 1 measure             | Compare categories
# Line Chart           : Date + measure                 | Trends over time
# Scatter Plot         : 2 measures                     | Correlation analysis
# Pie Chart            : 1 dim + 1 measure              | Part-to-whole (< 5 slices)
# Heat Map             : 2 dims + 1 measure             | Cross-tabular magnitude
# Tree Map             : 1+ dim + 1 measure             | Proportional hierarchies
# Bubble Chart         : 2 measures + 1 dim             | 3-variable comparison
# Box & Whisker        : 1 measure + dimension          | Statistical distribution
# Gantt Chart          : Date + measure (duration)      | Project timelines
# Bullet Chart         : Measure + reference            | Actual vs target KPI
# Symbol / Filled Map  : Geographic field + measure     | Geographic distribution
# Dual Axis Chart      : 2 measures on same axis        | Compare two metrics on one chart
# Combined Axis        : Multiple measures              | Same scale, different marks

# Heat Map vs Treemap:
# - Heat Map  : Grid layout; color intensity encodes a measure; requires two dimensions.
# - Treemap   : Nested rectangles; size AND color encode measures; works with one or more dimensions.

# How to Create a Dual-Axis Chart:
# - Step 1: Drag first measure (e.g., Sales) to Rows -> creates a bar chart.
# - Step 2: Drag second measure (e.g., Profit) to Rows -> two separate charts appear.
# - Step 3: Right-click the second pill on Rows -> select "Dual Axis".
# - Step 4: Right-click the right Y-axis -> "Synchronize Axis" (optional).
# - Step 5: On the Marks card, change one measure's mark type to Line; keep other as Bar.
# - Use cases: Sales (bar) vs Profit Margin % (line) over months; Units Sold vs Average Price.


# =============================================================================
# Q34. Explain Dashboards and Stories in Tableau. What are Dashboard Actions?
# =============================================================================

# Dashboard:
# - A collection of multiple worksheets arranged on a single canvas.
# - Enables side-by-side comparison and cross-filtering.

# Story:
# - A sequence of dashboard/worksheet snapshots with narrative text ("story points").
# - Used to present a data-driven narrative — like a slideshow with data.

# Dashboard vs Story:
# - Dashboard : Single interactive canvas; simultaneous analysis of multiple sheets.
# - Story     : Series of story points with captions; guides viewer through a narrative.

# Dashboard Actions:
# - Let users interact with dashboards by clicking or hovering to drive changes in other sheets.
# - Trigger on: Hover, Select, or Menu.

# 1. Filter Action        : Clicking a mark in one sheet filters data in another sheet.
# 2. Highlight Action     : Clicking a mark highlights related marks in other sheets
#                           without removing other data. Non-matching data dims.
# 3. URL Action           : Opens a web page or custom URL when a mark is clicked.
# 4. Go to Sheet Action   : Navigates to another sheet or dashboard in the workbook.
# 5. Change Parameter Action: Updates a parameter value based on a mark clicked.
# 6. Set Action           : Dynamically assigns values to a Set based on user interaction;
#                           powerful for relative-to-selection analysis.


# =============================================================================
# Q35. Explain Joins, Unions, and Data Blending in Tableau.
# =============================================================================

# How:
# - Joins        : Combined at database level before loading
# - Data Blending: Combined in Tableau front-end at aggregate level
# - Unions       : Stacks identical tables vertically

# Sources:
# - Joins        : Same data source
# - Data Blending: Different data sources
# - Unions       : Same source, same structure

# Result:
# - Joins        : Single table
# - Data Blending: Two queries linked by common dimension
# - Unions       : Single tall table

# Performance:
# - Joins        : Better
# - Data Blending: Slower (two queries + merge)
# - Unions       : Same source, efficient

# Link Field:
# - Joins        : Primary key / Foreign key
# - Data Blending: Common dimension (linking field)
# - Unions       : Matching column names

# Types of Joins in Tableau:
# - Inner Join      : Only matching rows from both tables
# - Left Outer Join : All rows from left + matching from right
# - Right Outer Join: All rows from right + matching from left
# - Full Outer Join : All rows from both; NULLs where no match

# Data Blending:
# - Tableau's method for combining data from two DIFFERENT data sources.
# - Sends separate queries to each source; aggregates each separately.
# - Combines results in the view using a common "linking field."
# - Primary source provides the granularity; secondary source data appears as aggregated values.
# - Secondary source always shown with a chain-link icon.
# - Secondary fields with no matching primary data show as asterisks (*).
# - vs Join: Joins combine row-level data before aggregation; blending combines post-aggregation.
# - Note: Relationships (introduced in Tableau 2020.2) have largely replaced Data Blending.

# Relationships (Tableau 2020.2+):
# - Define how tables are related WITHOUT physically joining them.
# - Deferred: Tableau generates appropriate JOIN at query time based on fields used in view.
# - Do not create a fixed single table.
# - Preserve row granularity of each table.
# - Avoid duplicate row problems from many-to-many joins.
# - Support multi-fact analysis.
# - Recommended modern approach over joins for most scenarios.


# =============================================================================
# Q36. What is Tableau Server? Explain its Components.
# =============================================================================

# Tableau Server is an enterprise platform for publishing, sharing, and managing Tableau content.

# Components:
# 1. Gateway (Load Balancer)      : Entry point for all client requests; distributes load.
# 2. Application Server (Vizportal): Handles web UI, REST API, authentication, permissions.
# 3. VizQL Server                 : Processes view requests; generates VizQL queries; renders visuals.
# 4. Data Server                  : Manages Published Data Sources; handles data source queries.
# 5. Backgrounder                 : Runs scheduled tasks: extract refreshes, subscriptions, alerts.
# 6. Cache Server (Memcached)     : Stores query results to avoid redundant database hits.
# 7. File Store                   : Stores workbook and extract files across cluster nodes.
# 8. Repository (PostgreSQL)      : Stores metadata: user accounts, permissions, workbooks, schedules.

# Published Data Source:
# - A shared data connection stored centrally on Tableau Server/Online.
# - Multiple workbooks can connect to a single published data source.
# - Ensures consistent data definitions, security, and calculations.
# - Supports Row-Level Security via data source filters.


# =============================================================================
# Q37. Explain Tableau Prep Builder and its Step Types.
# =============================================================================

# Tableau Prep Builder is a visual ETL tool for data cleaning and shaping.
# Creates Prep Flows that can be scheduled on Tableau Server.
# It is Tableau's equivalent of Power BI's Power Query.

# Step Types:
# 1. Input Step     : Connect to data sources (databases, files, cloud). Configure filters.
# 2. Clean Step     : Main transformation step. Remove nulls, rename fields, change data types,
#                     split columns, group similar values (fuzzy grouping), create calculated fields.
# 3. Aggregate Step : Group rows and compute aggregations (SUM, AVG, COUNT). Reduces granularity.
# 4. Pivot Step     : Converts columns to rows (unpivot) or rows to columns (pivot).
#                     Essential for reshaping wide tables to long format for analysis.
# 5. Join Step      : Merges two flows based on matching fields (Inner, Left, Right, Full Outer,
#                     Left Only, Right Only).
# 6. Union Step     : Combines multiple flows of the same structure vertically.
# 7. Script Step    : Run R or Python scripts for advanced transformations.
# 8. Output Step    : Save as Tableau Extract (.hyper), Published Data Source on Server,
#                     or external database.


# =============================================================================
# Q38. What are Sets and Groups in Tableau?
# =============================================================================

# Group:
# - Permanently combines dimension members into a higher-level category.
# - Example: Group "NY" and "NJ" into "Northeast".
# - Groups are STATIC and become a new dimension field.

# Set:
# - Defines a subset of members based on a condition.
# - Example: "Top 10 Customers by Sales".
# - Sets can be DYNAMIC — updating automatically as data changes.
# - Return binary In/Out membership.
# - Enabling relative comparisons and advanced calculations.
# - Can be combined using Set Control or Set Actions.

# Key Difference:
# - Group : Static; permanently merges members; creates a new dimension.
# - Set   : Dynamic; condition-based; binary In/Out; used for relative analysis.


# =============================================================================
# Q39. What is a Parameter in Tableau?
# =============================================================================

# A Parameter is a user-controlled input variable that can change the behavior
# of calculations, filters, or reference lines.

# Types of Parameter Controls:
# - Slider, Dropdown list, Type-in text box

# How it works:
# - Create a parameter (Data pane -> right-click -> Create Parameter).
# - Reference the parameter in a calculated field using IF/CASE logic.
# - Show the parameter control on the dashboard for user interaction.

# Example:
# IF [Discount Rate] = [Discount Parameter] THEN 'Match' ELSE 'No Match' END

# Use Case: "What-if" scenario analysis.
# Example: change a discount rate slider to see how profit changes dynamically.


# PART 3 — POWER BI vs TABLEAU COMPARISON
# =============================================================================


# =============================================================================
# Q40. Compare Power BI and Tableau across key parameters.
# =============================================================================

# Vendor:
# - Power BI : Microsoft
# - Tableau  : Salesforce (acquired 2019)

# Primary Users:
# - Power BI : Business analysts, Microsoft ecosystem users
# - Tableau  : Data analysts, advanced analytics users

# Pricing:
# - Power BI : Free Desktop; Pro ~$10/user/month; Premium ~$20+/user/month
# - Tableau  : Creator ~$75/user/month; Explorer ~$42; Viewer ~$15

# Ease of Use:
# - Power BI : Very beginner-friendly; Excel-like interface
# - Tableau  : Moderate learning curve; powerful drag-and-drop

# Data Transformation:
# - Power BI : Power Query (M language) — very powerful; built into Desktop
# - Tableau  : Tableau Prep (separate tool) / calculated fields

# Calculation Language:
# - Power BI : DAX — very powerful for complex relational models and filter context
# - Tableau  : Tableau formulas + LOD expressions for granularity control

# Visualization Flexibility:
# - Power BI : Good; 30+ native visuals + AppSource custom visuals
# - Tableau  : Excellent; highly customizable; fine pixel-level control

# Data Volume:
# - Power BI : Import limited (1GB Pro, 10GB Premium); DirectQuery unlimited
# - Tableau  : Hyper extracts handle billions of rows efficiently

# Data Connections:
# - Power BI : 300+ connectors (strong Microsoft Azure integration)
# - Tableau  : 80+ connectors; strong database support

# AI / ML Features:
# - Power BI : Key Influencers, Decomposition Tree, Azure ML integration, Copilot
# - Tableau  : Explain Data, Ask Data (Einstein), Tableau AI

# Collaboration:
# - Power BI : Power BI Service + Microsoft Teams integration
# - Tableau  : Tableau Server / Online

# Mobile:
# - Power BI : Power BI Mobile app
# - Tableau  : Tableau Mobile app

# Scripting:
# - Power BI : Python/R via Power BI Service (limited)
# - Tableau  : R & Python in Tableau Prep and calculated fields (TabPy)

# Licensing Model:
# - Power BI : Per user (Pro/Premium) or capacity (Premium)
# - Tableau  : Per user (Creator/Explorer/Viewer)

# Deployment:
# - Power BI : Cloud (Service), On-prem (Report Server), Embedded
# - Tableau  : Desktop, Server (on-prem), Online (cloud)

# Free Option:
# - Power BI : Yes — Power BI Desktop (full feature creation)
# - Tableau  : Yes — Tableau Public (public data only, no privacy)

# Best For:
# - Power BI : Microsoft-centric orgs, self-service BI, affordability
# - Tableau  : Advanced visualization, large data, data professionals


# =============================================================================
# QUICK-FIRE VIVA QUESTIONS
# =============================================================================


# =============================================================================
# Q41. What is Tableau Explain Data?
# =============================================================================

# Explain Data is an AI-powered feature in Tableau that automatically analyzes
# a selected data point and explains why that value might be unusual or noteworthy.
# It uses statistical analysis (outlier detection, regression) to surface potential
# explanatory factors from other fields in the data.
# - Right-click any mark -> "Explain Data" to trigger it.
# - Available in Tableau 2019.3+.


# =============================================================================
# Q42. What is Power BI Copilot?
# =============================================================================

# Power BI Copilot is Microsoft's AI-powered natural language interface for Power BI
# (integrated with Microsoft 365 Copilot).
# - Allows users to ask questions in plain English to generate report pages.
# - Automatically creates DAX measures from natural language descriptions.
# - Summarizes data insights without manually building visuals.
# - Requires Power BI Premium or Fabric capacity.


# =============================================================================
# Q43. What is Microsoft Fabric and how does it relate to Power BI?
# =============================================================================

# Microsoft Fabric (launched 2023) is an end-to-end data analytics platform that unifies:
# - Data engineering, Data factory, Data science, Real-time analytics, and Power BI
#   under a single SaaS experience.
# Power BI is the reporting and analytics layer within Fabric.
# Fabric adds:
# - OneLake       : A unified data lake
# - Lakehouse     : Combined data lake + data warehouse
# - Data Warehouse
# - Data Factory
# - Synapse components
# Positions Microsoft as a competitor to Databricks and Snowflake ecosystems.


# =============================================================================
# Q44. What is TabPy in Tableau?
# =============================================================================

# TabPy (Tableau Python Server) is an API extension that allows Tableau to execute
# Python scripts as part of a calculated field.
# - Enables advanced analytics: clustering, regression, NLP, custom ML models.
# - Results returned directly into Tableau visualizations.
# - Configured under Help -> Settings -> External Services.


# =============================================================================
# Q45. What is the ETL process in Tableau (Tableau Prep) vs Power BI (Power Query)?
# =============================================================================

# Power BI ETL (Power Query):
# - Extract  : Connect to 300+ sources (Excel, SQL, APIs, cloud).
# - Transform: Power Query Editor with 300+ transformation steps.
#              All steps recorded in "Applied Steps" panel as M language.
# - Load     : Cleaned data loaded into VertiPaq in-memory model (Import mode).
#              Can publish to Dataflows for reuse.

# Tableau ETL (Tableau Prep):
# - Extract  : Connect to databases, files, or existing published data sources.
# - Transform: Visual flow with Input, Clean, Aggregate, Pivot, Join, Union, Script steps.
#              Shows row-level data profiles for instant quality insights.
# - Load     : Save as .hyper extract or Publish to Tableau Server as a Data Source.
#              Can schedule on Server Backgrounder.

# Key Difference:
# - Power Query is EMBEDDED in Power BI Desktop (no separate tool).
# - Tableau Prep is a SEPARATE standalone product.
