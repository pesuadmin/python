# =============================================================================
# DVT ESA – Power BI
# Important Questions & Answers | Comprehensive Study Guide | 10-Mark Coverage
# MTech Data Science & AI | PES University
# =============================================================================

# =============================================================================
# Q1. What is Power BI?
# =============================================================================

"""
Power BI is a Business Intelligence (BI) and Data Visualization tool developed by Microsoft.
It enables users to connect to multiple data sources, transform data, create interactive
reports and dashboards, and support data-driven decision-making across an organization.
"""

Q1_key_features = [
    "Data visualization with interactive charts and graphs",
    "Interactive dashboards for real-time insights",
    "Real-time analytics and live data connections",
    "Cloud integration via Power BI Service",
    "Data sharing, collaboration, and role-based access",
    "Support for 100+ data connectors (SQL, Excel, Web APIs, etc.)",
]

# =============================================================================
# Q2. Explain the Components of Power BI.
# =============================================================================

"""
Power BI has five major components, each serving a specific purpose in the BI workflow.
"""

# Component | Description
Q2_components = [
    ("Power BI Desktop",       "Windows application to design reports and data models"),
    ("Power BI Service",       "Cloud platform (app.powerbi.com) to publish, share, and collaborate"),
    ("Power BI Mobile",        "iOS/Android apps to view reports on smartphones and tablets"),
    ("Power BI Gateway",       "Secure bridge connecting on-premise data sources to the cloud"),
    ("Power BI Report Server", "On-premise server to host and distribute reports internally"),
]

# =============================================================================
# Q3. What is Power Query?
# =============================================================================

"""
Power Query is a data transformation and preparation tool embedded in Power BI.
It is used to extract, clean, shape, and transform raw data from multiple sources
before loading it into the data model.
"""

Q3_common_operations = [
    "Remove duplicates and null values",
    "Filter rows and columns based on conditions",
    "Merge and append multiple tables",
    "Split columns (e.g., full name into first/last)",
    "Change data types and rename columns",
    "Pivot and unpivot data",
    "Group by and aggregate data",
]

# =============================================================================
# Q4. Explain the ETL Process in Power BI.
# =============================================================================

"""
ETL stands for Extract, Transform, and Load. It is the backbone of data preparation in Power BI.
"""

# Phase | Description
Q4_etl_phases = [
    ("Extract",   "Collect raw data from various sources: databases, Excel, APIs, web"),
    ("Transform", "Clean and reshape data using Power Query Editor"),
    ("Load",      "Load the prepared data into the Power BI data model for reporting"),
]

Q4_benefits = [
    "Improves data quality and consistency",
    "Reduces errors in reporting",
    "Supports data from multiple heterogeneous sources",
    "Automates repetitive data preparation tasks",
]

# =============================================================================
# Q5. Explain Data Modeling in Power BI.
# =============================================================================

"""
Data Modeling is the process of defining relationships between tables so that data
can be efficiently queried and analyzed across multiple tables.
"""

# Type | Description
Q5_relationship_types = [
    ("One-to-One (1:1)",   "Each row in Table A matches exactly one row in Table B"),
    ("One-to-Many (1:N)",  "One row in Table A relates to many rows in Table B (most common)"),
    ("Many-to-Many (M:N)", "Multiple rows on both sides (requires bridge table)"),
]

# Concept | Description
Q5_key_concepts = [
    ("Star Schema",             "Fact table at center connected to dimension tables (recommended)"),
    ("Snowflake Schema",        "Extended star with normalized dimensions"),
    ("Cross-filter direction",  "Single vs. Both (bidirectional filtering)"),
    ("Active vs. Inactive Relationships", "Only one active relationship allowed between two tables at a time"),
]

Q5_benefits = [
    "Enables complex cross-table analysis",
    "Reduces data redundancy",
    "Improves report performance",
]

# =============================================================================
# Q6. Differentiate Between Report and Dashboard.
# =============================================================================

# Feature | Report | Dashboard
Q6_report_vs_dashboard = [
    ("Definition",    "Multi-page detailed analysis document",              "Single-page summary of key metrics"),
    ("Pages",         "Multiple pages",                                     "Single page (canvas)"),
    ("Purpose",       "In-depth data exploration",                          "High-level overview and monitoring"),
    ("Created In",    "Power BI Desktop",                                   "Power BI Service"),
    ("Drill-Down",    "Full drill-down support",                            "Limited drill-down"),
    ("Interactivity", "Highly interactive (slicers, filters)",              "Pinned tiles, less interactive"),
    ("Data Source",   "One dataset per page",                               "Can combine from multiple reports"),
]

# =============================================================================
# Q7. What are Visualizations in Power BI?
# =============================================================================

"""
Visualizations are graphical representations of data that help communicate insights effectively.
Power BI offers 30+ built-in visual types and supports custom visuals from AppSource.
"""

# Visual Type | Purpose
Q7_visual_types = [
    ("Bar Chart / Column Chart", "Compare values across categories"),
    ("Line Chart",               "Show trends over time"),
    ("Pie Chart / Donut Chart",  "Show proportions"),
    ("Scatter Plot",             "Show correlation between two measures"),
    ("Map / Filled Map",         "Geographic data visualization"),
    ("KPI Card",                 "Display a single key metric"),
    ("Gauge Chart",              "Show progress toward a target"),
    ("Matrix / Table",           "Show data in tabular form with totals"),
    ("Waterfall Chart",          "Show cumulative effect of values"),
    ("Treemap",                  "Hierarchical proportional display"),
    ("Funnel Chart",             "Show pipeline/stage conversion"),
]

# =============================================================================
# Q8. What is DAX?
# =============================================================================

"""
DAX (Data Analysis Expressions) is the formula language used in Power BI,
Analysis Services, and Power Pivot. It is used to create calculated columns,
measures, and tables for advanced analytics.
"""

Q8_key_uses = [
    "Creating Measures for dynamic aggregations",
    "Creating Calculated Columns for row-level computations",
    "Time Intelligence functions (YTD, MTD, SAMEPERIODLASTYEAR)",
    "Filter context manipulation (CALCULATE, FILTER, ALL)",
]

# Function | Example | Purpose
Q8_common_functions = [
    ("SUM()",       "SUM(Sales[Amount])",                                          "Adds all values in a column"),
    ("COUNT()",     "COUNT(Orders[OrderID])",                                      "Counts rows with non-blank values"),
    ("AVERAGE()",   "AVERAGE(Sales[Price])",                                       "Calculates average"),
    ("CALCULATE()", "CALCULATE(SUM(Sales[Amount]), Region='South')",               "Evaluates with modified filter context"),
    ("IF()",        "IF(Sales[Amount]>1000, 'High', 'Low')",                       "Conditional logic"),
    ("RELATED()",   "RELATED(Product[Category])",                                  "Fetches value from related table"),
    ("DATEADD()",   "DATEADD(Dates[Date], -1, YEAR)",                              "Time intelligence shift"),
]

Q8_example_measures = """
Total Sales    = SUM(Sales[Amount])
Profit Margin  = DIVIDE([Total Profit], [Total Sales], 0)
YTD Sales      = TOTALYTD(SUM(Sales[Amount]), Dates[Date])
"""

# =============================================================================
# Q9. Difference Between Measure and Calculated Column.
# =============================================================================

# Feature | Measure | Calculated Column
Q9_measure_vs_calc_col = [
    ("Calculation",  "Evaluated dynamically at query time",               "Evaluated row by row at data refresh"),
    ("Storage",      "NOT stored in the model (computed in memory)",       "Stored in the model (occupies memory)"),
    ("Context",      "Responds to report filters and slicers",             "Does not respond to filters dynamically"),
    ("Use Case",     "Aggregations: totals, averages, ratios",             "Row-level logic: profit per row, category flag"),
    ("Example",      "Total Sales = SUM(Sales[Amount])",                   "Profit = Sales[Revenue] - Sales[Cost]"),
    ("Performance",  "Better for large datasets",                          "Increases model size"),
]

# =============================================================================
# Q10. Explain Interactive Dashboards.
# =============================================================================

"""
Interactive Dashboards in Power BI allow users to explore and analyze data dynamically
without needing technical skills. They combine multiple visuals that respond to user actions.
"""

# Feature | Description
Q10_interactive_features = [
    ("Filters",          "Narrow down data displayed across the entire report page"),
    ("Slicers",          "Visual filter controls (dropdown, buttons, date range)"),
    ("Drill-Down",       "Navigate from summary to detail (e.g., Year > Quarter > Month)"),
    ("Drill-Through",    "Jump to a detail page based on selected data point"),
    ("Cross-Filtering",  "Clicking one visual automatically filters all related visuals"),
    ("Bookmarks",        "Save specific view states for storytelling"),
    ("Tooltips",         "Show additional info on hover"),
]

Q10_benefits = [
    "Empowers non-technical users to explore data independently",
    "Supports faster, data-driven decisions",
    "Reduces need for multiple static reports",
]

# =============================================================================
# Q11. What is a Slicer?
# =============================================================================

"""
A Slicer is a visual filter element placed directly on a report page.
It allows users to filter all related visuals on the page interactively by selecting values.
"""

# Type | Description
Q11_slicer_types = [
    ("Dropdown Slicer",      "Select one or multiple values from a list"),
    ("List Slicer",          "Checkboxes for multi-select"),
    ("Between Slicer",       "For numeric or date ranges"),
    ("Relative Date Slicer", "Last N days, this month, this year, etc."),
    ("Tile Slicer",          "Button-style selection"),
]

Q11_use_cases = [
    "Filter sales data by Region, Product Category, or Year",
    "Compare performance across different time periods",
    "Segment customer data by demographics",
]

# =============================================================================
# Q12. Explain Python Integration in Power BI.
# =============================================================================

"""
Power BI supports Python scripting for advanced analytics, custom data transformations,
and machine learning that go beyond Power BI's built-in capabilities.
"""

# Where Python Can Be Used
Q12_python_usage_areas = [
    ("Data Source",    "Use Python scripts to import and generate datasets"),
    ("Power Query",    "Run Python for data transformation and cleaning"),
    ("Visualizations", "Create custom visuals using Python plotting libraries"),
]

# Library | Purpose
Q12_python_libraries = [
    ("Pandas",      "Data manipulation and cleaning (DataFrames)"),
    ("NumPy",       "Numerical computing and array operations"),
    ("Matplotlib",  "Static data visualizations and custom charts"),
    ("Seaborn",     "Statistical visualizations built on Matplotlib"),
    ("Scikit-learn","Machine learning: regression, classification, clustering"),
    ("Plotly",      "Interactive charts and graphs"),
]

Q12_applications = [
    "Predictive Analytics and forecasting",
    "Machine Learning model integration",
    "Statistical analysis (correlation, regression)",
    "Advanced data cleaning and outlier detection",
    "Custom visualizations not available in Power BI natively",
]

# =============================================================================
# Q13. Steps to Integrate Python with Power BI.
# =============================================================================

Q13_integration_steps = [
    "Install Python (version 3.x recommended from python.org)",
    "Install required libraries: pip install pandas matplotlib seaborn scikit-learn",
    "In Power BI Desktop, go to File > Options > Python scripting",
    "Set the Python home directory to your installed Python path",
    "Use Python as a data source: Get Data > Python Script",
    "Use Python in Power Query: Transform > Run Python Script",
    "Use Python visuals: From Visualizations pane, select Python Visual",
    "Write and paste Python script in the script editor area",
    "Press Run to generate the visualization or output",
]

Q13_sample_script = """
import matplotlib.pyplot as plt
import pandas as pd

# 'dataset' is the Power BI DataFrame automatically passed in
fig, ax = plt.subplots()
dataset.groupby('Category')['Sales'].sum().plot(kind='bar', ax=ax)
plt.title('Sales by Category')
plt.tight_layout()
plt.show()
"""

# =============================================================================
# Q14. What is Power BI Gateway? (Bonus)
# =============================================================================

"""
The Power BI Gateway is a software component that acts as a bridge between
on-premise data sources and Power BI cloud services. It enables scheduled refresh
of reports that use local databases, files, or servers.
"""

# Type | Description
Q14_gateway_types = [
    ("On-premises data gateway (Standard mode)", "Supports multiple users and data sources"),
    ("On-premises data gateway (Personal mode)", "For individual use only"),
]

Q14_when_needed = [
    "When connecting to SQL Server, Oracle, or other local databases",
    "When refreshing reports in Power BI Service that use on-premise data",
    "When using DirectQuery with local data sources",
]

# =============================================================================
# Q15. Explain Row-Level Security (RLS) in Power BI.
# =============================================================================

"""
Row-Level Security (RLS) is a feature in Power BI that restricts data access at
the row level based on the logged-in user. Different users see different subsets
of data from the same report.
"""

Q15_how_rls_works = [
    "Define roles in Power BI Desktop using DAX filter expressions",
    "Assign users or groups to those roles in Power BI Service",
    "When the user views the report, filters are applied automatically",
]

Q15_example_dax = "[Region] = USERNAME() OR [Region] = USERPRINCIPALNAME()"

# Type | Description
Q15_rls_types = [
    ("Static RLS",  "Fixed filter values per role"),
    ("Dynamic RLS", "Uses DAX functions like USERNAME() to filter dynamically"),
]

# =============================================================================
# Q16. What is DirectQuery vs Import Mode?
# =============================================================================

# Feature | DirectQuery | Import Mode
Q16_directquery_vs_import = [
    ("Data Storage",  "Data NOT stored in Power BI model",          "Data IS copied into Power BI model"),
    ("Refresh",       "Real-time – queries source directly",         "Scheduled or manual refresh required"),
    ("Performance",   "Slower (depends on source speed)",            "Faster (in-memory processing)"),
    ("Data Size",     "No size limit (large datasets)",              "Limited to ~1 GB compressed"),
    ("DAX Support",   "Limited DAX functions supported",             "Full DAX support"),
    ("Best For",      "Live operational dashboards",                 "Historical reporting and analysis"),
]

# =============================================================================
# Q17. What are KPIs and Cards in Power BI?
# =============================================================================

"""
KPI (Key Performance Indicator) and Card visuals are used to display single,
important numeric values on a dashboard.
"""

Q17_card_visual = [
    "Displays a single number or text value",
    "Example: Total Revenue: $5.2M",
    "Useful for summary statistics at the top of a dashboard",
]

Q17_kpi_visual = [
    "Shows a metric, a target value, and the trend status",
    "Includes indicator (green/red) based on target vs actual",
    "Requires: Value, Target, and Time Trend fields",
]

# =============================================================================
# Q18. Explain the Power BI Report Lifecycle.
# =============================================================================

Q18_report_lifecycle = [
    "Connect to Data Sources (databases, files, APIs)",
    "Transform Data using Power Query (ETL)",
    "Create Data Model (relationships, hierarchies)",
    "Write DAX Measures and Calculated Columns",
    "Build Visuals and Reports in Power BI Desktop",
    "Apply Filters, Slicers, and Drill-Down features",
    "Publish to Power BI Service (cloud)",
    "Share with users, configure Row-Level Security",
    "Schedule Data Refresh",
    "Monitor and maintain reports",
]

# =============================================================================
# Q19. What is the Difference Between Power BI and Traditional BI Tools?
# =============================================================================

"""
Traditional BI tools (like Crystal Reports, Cognos, or MicroStrategy) require
dedicated IT teams and have long development cycles. Power BI democratizes BI
by making it accessible to business users.
"""

# Feature | Traditional BI | Power BI
Q19_traditional_vs_powerbi = [
    ("Development",     "Requires IT/developer involvement",                  "Self-service; business users can build reports"),
    ("Deployment",      "On-premise, complex setup",                          "Cloud-first, rapid deployment"),
    ("Cost",            "High licensing and infrastructure costs",             "Affordable subscription model"),
    ("Refresh",         "Batch processing, periodic",                         "Near real-time refresh possible"),
    ("Collaboration",   "Limited sharing mechanisms",                         "Easy sharing via cloud links and workspaces"),
    ("Learning Curve",  "Steep, requires training",                           "Drag-and-drop interface, Excel-like"),
    ("Data Sources",    "Predefined connectors",                              "100+ connectors including REST APIs"),
]

# =============================================================================
# Q20. Explain the Concept of Data Refresh in Power BI.
# =============================================================================

"""
Data Refresh is the process of updating the dataset in Power BI Service so that
reports reflect the latest data from the source systems. Since Import Mode copies
data into the model, it must be periodically refreshed.
"""

# Type | Description
Q20_refresh_types = [
    ("On-Demand Refresh",     "Manually triggered by the user in Power BI Service"),
    ("Scheduled Refresh",     "Automatically triggered at set intervals (up to 8 times/day on Pro, 48 times/day on Premium)"),
    ("Real-Time Refresh",     "Used with DirectQuery or streaming datasets; no scheduled refresh needed"),
    ("Incremental Refresh",   "Refreshes only new or changed data rows, not the entire dataset (efficient for large data)"),
]

Q20_prerequisites = [
    "Dataset must be published to Power BI Service",
    "Data source credentials must be configured",
    "On-premises Gateway required for local data sources",
]

# =============================================================================
# Q21. What are Workspaces in Power BI?
# =============================================================================

"""
Workspaces are collaborative environments in Power BI Service where teams can
create, share, and manage reports, dashboards, and datasets together.
"""

# Type | Description
Q21_workspace_types = [
    ("My Workspace",           "Personal space for individual users; cannot be shared"),
    ("Shared Workspace",       "Team collaboration space; supports multiple contributors"),
    ("Premium Workspace",      "Backed by dedicated capacity; allows sharing with free-license users"),
]

# Role | Permissions
Q21_workspace_roles = [
    ("Admin",       "Full control: manage members, delete workspace, publish apps"),
    ("Member",      "Create/edit content, publish apps, cannot manage members"),
    ("Contributor", "Create and edit reports and datasets; cannot publish apps"),
    ("Viewer",      "Read-only access to reports and dashboards"),
]

# =============================================================================
# Q22. What is the Role of Aggregations in Power BI?
# =============================================================================

"""
Aggregations in Power BI allow pre-summarized versions of large datasets to be
cached and queried, dramatically improving performance for large-scale analytics.
"""

Q22_how_aggregations_work = [
    "A summarized (aggregated) table is created from the detail table",
    "Power BI automatically routes queries to the aggregated table when possible",
    "If a query requires row-level detail, it falls back to the full detail table",
]

Q22_benefits = [
    "Reduces query time from minutes to seconds on large datasets",
    "Works seamlessly with both Import and DirectQuery modes",
    "Enables analytics on billion-row datasets on Power BI Premium",
]

# =============================================================================
# Q23. Explain Hierarchies in Power BI.
# =============================================================================

"""
A Hierarchy in Power BI is a logical grouping of columns in a specific order
that enables drill-down analysis. It allows users to navigate from a high-level
summary to granular detail.
"""

# Hierarchy | Levels
Q23_hierarchy_examples = [
    ("Date Hierarchy",         "Year > Quarter > Month > Day"),
    ("Geography Hierarchy",    "Country > State > City > Postal Code"),
    ("Product Hierarchy",      "Category > Subcategory > Product Name"),
    ("Organization Hierarchy", "Division > Department > Employee"),
]

Q23_how_to_create = [
    "In the Fields pane, right-click a column > 'New hierarchy'",
    "Drag additional fields into the hierarchy in the desired order",
    "Use the visual's drill-down buttons to navigate the hierarchy in reports",
]

# Action | Description
Q23_drill_actions = [
    ("Drill Down",        "Go one level deeper for the selected data point"),
    ("Drill Up",          "Return to the previous level"),
    ("Expand All Down",   "Expand all data points to the next level simultaneously"),
]

# =============================================================================
# Q24. What is Power BI Embedded?
# =============================================================================

"""
Power BI Embedded is an Azure service that allows developers to integrate Power BI
reports, dashboards, and visuals directly into custom applications, websites, or
portals without requiring users to have a Power BI license.
"""

Q24_key_characteristics = [
    "Reports are embedded via iframes using REST APIs and JavaScript SDK",
    "Authentication handled by the application (embed tokens)",
    "Two embedding modes: Embed for your customers (app owns data) and Embed for your organization (user owns data)",
    "Billed based on Azure capacity (A SKUs), not per user",
]

Q24_use_cases = [
    "SaaS vendors embedding analytics into their product",
    "Portals showing analytics to external clients",
    "Custom enterprise applications with integrated BI",
]

# =============================================================================
# Q25. Explain the Concept of Bookmarks and Report Navigation in Power BI.
# =============================================================================

"""
Bookmarks capture the current state of a report page — including filter selections,
slicer values, visual visibility, and scroll positions — so users can save and
return to specific views.
"""

# Type | Description
Q25_bookmark_types = [
    ("Personal Bookmarks", "Saved by individual viewers in Power BI Service (does not affect others)"),
    ("Report Bookmarks",   "Created by the report author in Desktop; embedded in the report"),
]

Q25_uses = [
    "Data Storytelling – Guide viewers through a narrative with preset views",
    "Toggle Visuals – Show/hide visuals using buttons and bookmarks (e.g., show chart vs table)",
    "Custom Navigation – Build page navigation menus without using the default tab bar",
    "Reset Filters – Create a 'Reset to Default' button using a bookmark",
]

# =============================================================================
# Q26. What is the Difference Between Filter Pane and Slicer?
# =============================================================================

# Feature | Filter Pane | Slicer
Q26_filter_vs_slicer = [
    ("Visibility",    "Hidden panel (can be collapsed)",                      "Visible visual on the report canvas"),
    ("User Access",   "Author-controlled (can restrict)",                     "Always accessible to report viewers"),
    ("Scope",         "Page, report, or visual level filtering",              "Affects all visuals on the page by default"),
    ("Types",         "Basic, Advanced, Top N filtering",                     "Dropdown, list, date range, slider"),
    ("Design",        "Not part of visual layout",                            "Occupies space on the canvas; can be styled"),
    ("Cross-Page",    "Report-level filters apply to all pages",              "Slicers work only on their own page (unless synced)"),
    ("Sync",          "Not applicable",                                       "Slicer Sync panel can sync across pages"),
]

# =============================================================================
# Q27. What are Themes in Power BI?
# =============================================================================

"""
Themes in Power BI allow report authors to apply a consistent color palette, font,
and visual formatting across an entire report in one click. They ensure visual
consistency and support corporate branding.
"""

# Type | Description
Q27_theme_types = [
    ("Built-in Themes",    "Power BI provides default themes like Default, Classic, Colorblind safe, etc."),
    ("Custom JSON Themes", "Authors can define a JSON file specifying colors, fonts, and visual defaults"),
]

Q27_json_example = """
{
    "name": "Corporate Theme",
    "dataColors": ["#1F4E79", "#2E75B6", "#70AD47"],
    "background": "#FFFFFF",
    "foreground": "#333333",
    "tableAccent": "#2E75B6"
}
"""

Q27_benefits = [
    "Maintains brand consistency across all reports",
    "Saves time — applies formatting to all visuals at once",
    "Can be shared across teams as a .json file",
]

# =============================================================================
# Q28. Explain Time Intelligence Functions in DAX.
# =============================================================================

"""
Time Intelligence functions in DAX allow calculations across time periods such as
year-to-date totals, month-over-month comparisons, and rolling averages.
They require a properly marked Date table in the data model.
"""

Q28_prerequisites = [
    "A dedicated Date/Calendar table in the data model",
    "The Date table must be marked as a 'Date Table' in Power BI",
    "The Date column must be of Date data type with no gaps",
]

# Function | Example | Purpose
Q28_time_intelligence_functions = [
    ("TOTALYTD()",          "TOTALYTD(SUM(Sales[Amount]), Dates[Date])",                              "Year-to-date total"),
    ("TOTALQTD()",          "TOTALQTD([Total Sales], Dates[Date])",                                   "Quarter-to-date total"),
    ("TOTALMTD()",          "TOTALMTD([Total Sales], Dates[Date])",                                   "Month-to-date total"),
    ("SAMEPERIODLASTYEAR()", "CALCULATE([Total Sales], SAMEPERIODLASTYEAR(Dates[Date]))",             "Same period in prior year"),
    ("DATEADD()",           "CALCULATE([Total Sales], DATEADD(Dates[Date], -1, MONTH))",              "Shift by N periods"),
    ("DATESYTD()",          "CALCULATE([Sales], DATESYTD(Dates[Date]))",                              "All dates from year start to current"),
]

# =============================================================================
# Q29. What is a Star Schema and Why is it Preferred in Power BI?
# =============================================================================

"""
A Star Schema is a data modeling pattern where a central Fact table is surrounded
by multiple Dimension tables, resembling a star shape. It is the recommended data
model pattern for Power BI.
"""

Q29_components = [
    ("Fact Table",       "Contains measurable, quantitative data (sales amount, quantity, revenue). Has foreign keys pointing to dimension tables."),
    ("Dimension Tables", "Contain descriptive attributes (customer name, product category, date). Usually smaller, denormalized tables."),
]

# Table | Columns
Q29_example_star_schema = [
    ("Fact_Sales",    "SalesID, DateKey, ProductKey, CustomerKey, Amount, Quantity"),
    ("Dim_Date",      "DateKey, Year, Quarter, Month, Day"),
    ("Dim_Product",   "ProductKey, ProductName, Category, Subcategory"),
    ("Dim_Customer",  "CustomerKey, CustomerName, Region, Segment"),
]

Q29_why_preferred = [
    "Simpler relationships — Power BI's DAX engine is optimized for it",
    "Faster query performance due to fewer joins",
    "Easier to understand and maintain for report authors",
    "Enables powerful filter propagation across dimensions",
]

# =============================================================================
# Q30. What is the CALCULATE Function in DAX?
# =============================================================================

"""
CALCULATE is the most powerful and important function in DAX.
It evaluates an expression in a modified filter context, allowing you to override
or add filters to change what data is included in the calculation.

Syntax: CALCULATE(Expression, Filter1, Filter2, ...)
"""

Q30_key_concepts = [
    "Filter Context – The set of filters currently applied to the data model",
    "CALCULATE can ADD new filters, REPLACE existing ones, or REMOVE them using ALL()",
    "It is used to build virtually every non-trivial DAX measure",
]

Q30_examples = """
# Sales only for the South region
South_Sales = CALCULATE(SUM(Sales[Amount]), Region[Region] == "South")

# Sales ignoring all filters (grand total)
All_Sales = CALCULATE(SUM(Sales[Amount]), ALL(Sales))

# % of total contribution
Sales_Pct = DIVIDE(Total_Sales, CALCULATE(Total_Sales, ALL(Sales)), 0)
"""

# Modifier Function | Description
Q30_modifier_functions = [
    ("ALL()",          "Removes all filters from a table or column"),
    ("ALLEXCEPT()",    "Removes all filters except specified columns"),
    ("FILTER()",       "Applies a row-by-row Boolean filter"),
    ("KEEPFILTERS()",  "Adds filter without replacing existing context"),
]

# =============================================================================
# END OF FILE
# DVT ESA – Power BI Study Guide | 30 Questions | MTech Theoretical Coverage
# =============================================================================
