# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

print("Hello World")

# COMMAND ----------

# MAGIC %md <i18n value="5f2cfc0b-1998-4182-966d-8efed6020eb2"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC # Getting Started with the Databricks Platform
# MAGIC 
# MAGIC This notebook provides a hands-on review of some of the basic functionality of the Databricks Data Science and Engineering Workspace.
# MAGIC 
# MAGIC ## Learning Objectives
# MAGIC By the end of this lab, you should be able to:
# MAGIC - Rename a notebook and change the default language
# MAGIC - Attach a cluster
# MAGIC - Use the **`%run`** magic command
# MAGIC - Run Python and SQL cells
# MAGIC - Create a Markdown cell

# COMMAND ----------

# MAGIC %md <i18n value="05dca5e4-6c50-4b39-a497-a35cd6d99434"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC # Renaming a Notebook
# MAGIC 
# MAGIC Changing the name of a notebook is easy. Click on the name at the top of this page, then make changes to the name. To make it easier to navigate back to this notebook later in case you need to, append a short test string to the end of the existing name.

# COMMAND ----------

# MAGIC %md <i18n value="f07b8dd7-436d-4719-9c17-18cd47f493fe"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC # Attaching a cluster
# MAGIC 
# MAGIC Executing cells in a notebook requires computing resources, which is provided by clusters. The first time you execute a cell in a notebook, you will be prompted to attach to a cluster if one is not already attached.
# MAGIC 
# MAGIC Attach a cluster to this notebook now by clicking the dropdown near the top-left corner of this page. Select the cluster you created previously. This will clear the execution state of the notebook and connect the notebook to the selected cluster.
# MAGIC 
# MAGIC Note that the dropdown menu provides the option of starting or restarting the cluster as needed. You can also detach and re-attach to a cluster in a single movement. This is useful for clearing the execution state when needed.

# COMMAND ----------

# MAGIC %md <i18n value="68805a5e-3b2c-4f79-819f-273d4ca95137"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC # Using %run
# MAGIC 
# MAGIC Complex projects of any type can benefit from the ability to break them down into simpler, reusable components.
# MAGIC 
# MAGIC In the context of Databricks notebooks, this facility is provided through the **`%run`** magic command.
# MAGIC 
# MAGIC When used this way, variables, functions and code blocks become part of the current programming context.
# MAGIC 
# MAGIC Consider this example:
# MAGIC 
# MAGIC **`Notebook_A`** has four commands:
# MAGIC   1. **`name = "John"`**
# MAGIC   2. **`print(f"Hello {name}")`**
# MAGIC   3. **`%run ./Notebook_B`**
# MAGIC   4. **`print(f"Welcome back {full_name}`**
# MAGIC 
# MAGIC **`Notebook_B`** has only one commands:
# MAGIC   1. **`full_name = f"{name} Doe"`**
# MAGIC 
# MAGIC If we run **`Notebook_B`** it will fail to execute because the variable **`name`** is not defined in **`Notebook_B`**
# MAGIC 
# MAGIC Likewise, one might think that **`Notebook_A`** would fail becase it uses the variable **`full_name`** which is likewise not defined in **`Notebook_A`**, but it doesn't!
# MAGIC 
# MAGIC What actually happens is that the two notebooks are merged together as we see below and **then** executed:
# MAGIC 1. **`name = "John"`**
# MAGIC 2. **`print(f"Hello {name}")`**
# MAGIC 3. **`full_name = f"{name} Doe"`**
# MAGIC 4. **`print(f"Welcome back {full_name}")`**
# MAGIC 
# MAGIC And thus providing the expected behavior:
# MAGIC * **`Hello John`**
# MAGIC * **`Welcome back John Doe`**

# COMMAND ----------

# MAGIC %md <i18n value="260e99b3-4126-41b7-8210-b6ff01b98790"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC The folder that contains this notebook contains a subfolder named **`ExampleSetupFolder`**, which in turn contains a notebook called **`example-setup`**. 
# MAGIC 
# MAGIC This simple notebook declares the variable **`my_name`**, sets it to **`None`** and then creates a DataFrame called **`example_df`**. 
# MAGIC 
# MAGIC Open the example-setup notebook and modify it so that name is not **`None`** but rather your name (or anyone's name) enclosed in quotes, and so that the following two cells execute without throwing an **`AssertionError`**.
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_24.png"> You will see additional references **`_utility-methods`** and **`DBAcademyHelper`** which are used to this configure  courseware and should be ignored for this exercise.

# COMMAND ----------

# MAGIC %run ./ExampleSetupFolder/example-setup

# COMMAND ----------

assert my_name is not None, "Name is still None"
print(my_name)

# COMMAND ----------

# MAGIC %md <i18n value="ece094f7-d013-4b24-aa54-e934f4ab7dbd"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC ## Run a Python cell
# MAGIC 
# MAGIC Run the following cell to verify that the **`example-setup`** notebook was executed by displaying the **`example_df`** Dataframe. This table consists of 16 rows of increasing values.

# COMMAND ----------

display(example_df)

# COMMAND ----------

# MAGIC %md <i18n value="ce392afd-2e73-4a51-adc4-7d654dad6215"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC # Change Language
# MAGIC 
# MAGIC Notice that the default language for this notebook is set to Python. Change this by clicking the **Python** button to the right of the notebook name. Change the default language to SQL.
# MAGIC 
# MAGIC Notice that the Python cells are automatically prepended with a <strong><code>&#37;python</code></strong> magic command to maintain validity of those cells. Notice that this operation also clears the execution state.

# COMMAND ----------

# MAGIC %md <i18n value="dfce7fd1-08e8-4cc3-92ac-a2eb74f804ef"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC # Create a Markdown Cell
# MAGIC 
# MAGIC Add a new cell below this one. Populate with some Markdown that includes at least the following elements:
# MAGIC * A header
# MAGIC * Bullet points
# MAGIC * A link (using your choice of HTML or Markdown conventions)

# COMMAND ----------

# MAGIC %md <i18n value="a54470bc-2a69-4a34-acbb-fe28c4dee284"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC ## Run a SQL cell
# MAGIC 
# MAGIC Run the following cell to query a Delta table using SQL. This executes a simple query against a table is backed by a Databricks-provided example dataset included in all DBFS installations.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM delta.`${DA.paths.datasets}/nyctaxi-with-zipcodes/data`

# COMMAND ----------

# MAGIC %md <i18n value="7499c6b6-b3f3-4641-88d9-5a260d3c11f8"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC Execute the following cell to view the underlying files backing this table.

# COMMAND ----------

files = dbutils.fs.ls(f"{DA.paths.datasets}/nyctaxi-with-zipcodes/data")
display(files)

# COMMAND ----------

# MAGIC %md <i18n value="a17b5667-53bc-4f8a-8601-5599f4ebb819"/>
# MAGIC 
# MAGIC 
# MAGIC # Clearing notebook state
# MAGIC 
# MAGIC Sometimes it is useful to clear all variables defined in the notebook and start from the begining.  This can be useful when you want to test cells in isolation, or you simply want to reset the execution state.
# MAGIC 
# MAGIC Visit the **Clear** menu and select the **Clear State & Cell Outputs**.
# MAGIC 
# MAGIC Now try running the cell below and notice the variables defined earlier are no longer defined, until you rerun the earlier cells above.

# COMMAND ----------

print(my_name)

# COMMAND ----------

# MAGIC %md <i18n value="8bff18c2-3ecf-484a-9a8c-dadab7eaf0a1"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC # Review Changes
# MAGIC 
# MAGIC Assuming you have imported this material into your workspace using a Databricks Repo, open the Repo dialog by clicking the **`published`** branch button at the top-left corner of this page. You should see three changes:
# MAGIC 1. **Removed** with the old notebook name
# MAGIC 1. **Added** with the new notebook name
# MAGIC 1. **Modified** for creating a markdown cell above
# MAGIC 
# MAGIC Use the dialog to revert the changes and restore this notebook to its original state.

# COMMAND ----------

# MAGIC %md <i18n value="cb3c335a-dd4c-4620-9f10-6946250f2e02"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC ## Wrapping Up
# MAGIC 
# MAGIC By completing this lab, you should now feel comfortable manipulating notebooks, creating new cells, and running notebooks within notebooks.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2022 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
