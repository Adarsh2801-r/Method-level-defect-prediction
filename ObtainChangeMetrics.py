import CK_metricsGenerator
import numpy as np
import pandas as pd
import os






directory=input("Enter ChangeScript directory name : ")
path = input("Enter absolute path of folder where csv files are to be stored: ")
for filename in os.listdir(directory):
  print("Processing "+filename+"...")
  df = pd.DataFrame(columns = ['method', 'changes', 'STATEMENT_INSERT','STATEMENT_DELETE','CONDITION_EXPRESSION_CHANGE','ALTERNATIVE_PART_INSERT','ALTERNATIVE_PART_DELETE','METHOD_RENAMING','PARAMETER_RENAMING','PARAMETER_INSERT','PARAMETER_DELETE','PARAMETER_ORDERING_CHANGE','PARAMETER_TYPE_CHANGE'])
  f = os.path.join(directory,filename)
  file = open(f, 'r')
  tokens = CK_metricsGenerator.run(file.read())
  LIST_CHANGES=['STATEMENT_INSERT','STATEMENT_DELETE','CONDITION_EXPRESSION_CHANGE','ALTERNATIVE_PART_INSERT','ALTERNATIVE_PART_DELETE','METHOD_RENAMING','PARAMETER_RENAMING','PARAMETER_INSERT','PARAMETER_DELETE','PARAMETER_ORDERING_CHANGE','PARAMETER_TYPE_CHANGE']
  #method_change_history = []
  for i in range(len(tokens)):
     #print(tokens[i][1])
    if tokens[i] == 'root:':
        if tokens[i+4] in LIST_CHANGES:
          method_change_history =([tokens[i + 1], tokens[i + 4]])
          method = method_change_history[0]
          method_Change_type = method_change_history[1]
          if (method in list(df['method'])):
            df.loc[df['method'] == method,'changes'] += 1
            df.loc[df['method'] == method,method_Change_type]  += 1
          else:
            df.loc[len(df.index)]=[method,1,0,0,0,0,0,0,0,0,0,0,0]
            df.loc[df['method'] == method,method_Change_type]  = 1  
    df.to_csv(os.path.join(path,filename+"_ChangeMetrics.csv"))

