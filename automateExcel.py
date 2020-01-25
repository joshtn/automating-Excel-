import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file_1 = "shift-data.xlsx"
excel_file_2 = "shift-data-third.xlsx"

df_first_shift = pd.read_excel(excel_file_1, sheet_name="first")
df_second_shift = pd.read_excel(excel_file_1, sheet_name="second")
df_third_shift = pd.read_excel(excel_file_2)

print(df_first_shift)
print(df_first_shift['Product'])

# combining data from multiple excel sheets
df_all = pd.concat([df_first_shift, df_second_shift, df_third_shift])
print(df_all)

# calculations
pivot = df_all.groupby(["Shift"]).mean()
shift_productivity = pivot.loc[:,
                               "Production Run Time (Min)":"Products Produced (Units)"]
# output is shown below, can see that 3rd shift was most productive.
print(shift_productivity)

#        Production Run Time (Min)  Products Produced (Units)
# Shift
# 1                      44.689655                  54.482759
# 2                      43.689655                  80.103448
# 3                      43.034483                 128.448276

# graphing the results
shift_productivity.plot(kind="bar")
plt.show()

# exporting to a excel sheet
df_all.to_excel("df_all_output.xlsx")
