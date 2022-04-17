import numpy as np
import pandas as pd

fname = "C:/Users/BITS-PC/Desktop/cas_diff.txt"
file1 = open(fname, 'r')

Lines = file1.readlines()
df = pd.DataFrame(columns = ['fname', 'locAdded', 'locRemoved','maxlocAdded','maxlocRemoved','avglocAdded','avglocRemoved','codeChurn'])

avg = dict()

m1 = set()

file = ""
rev = ""
mxAdd = 0
mxRemove = 0

mx_add = {}
mx_rem = {}

cou = {}





for line in Lines:
  lst = line.split()
  if(len(lst) > 0 and lst[0]=="+++"):
  	curr_file = lst[1]
  	curr_rev =  lst[3]
  	file = curr_file
  	rev = curr_rev
  	if(curr_file not in list(df['fname'])):
  		df.loc[len(df.index)] = [curr_file,0,0,0,0,0,0,0]
  
  curr = file + "||" + rev

  if(curr not in m1):
  	mxAdd=0
  	mxRemove=0
  	m1.add(curr)

  if(len(lst) > 0):
  	if(lst[0]=='+'):
  		df.loc[df['fname']== curr_file,'locAdded'] += 1
  		mxAdd += 1
  	elif(lst[0]=='-'):
  	    df.loc[df['fname']== curr_file,'locRemoved'] += 1
  	    mxRemove += 1
  
  
  if(file!=''):
  	if(file not in mx_add):
  		mx_add[file]=0
  	mx_add[file] = max(mx_add[file],mxAdd)
  	if(file not in mx_rem):
  		mx_rem[file] = 0
  	mx_rem[file] = max(mx_rem[file],mxRemove)
  	df.loc[df['fname']== file,'maxlocAdded'] = mx_add[file]
  	df.loc[df['fname']== file,'maxlocRemoved'] = mx_rem[file]

  if(len(lst) > 0 and lst[0]=="+++" and file!=''):
  	if(file not in cou):
  		cou[file]=0
  	cou[file] += 1

  



for i in cou:
	df.loc[df['fname']== i,'avglocAdded'] = float(((float(df.loc[df['fname']== i,'locAdded'])) / float(cou[i])))
	df.loc[df['fname']== i,'avglocRemoved'] =float(((float(df.loc[df['fname']== i,'locRemoved'])) / float(cou[i])))


df[:]['codeChurn'] = df[:]['locAdded'] - df[:]['locRemoved']


fname2 = "C:/Users/BITS-PC/Desktop/cas_log.txt"
file2 = open(fname2, 'r')
Lines2 = file2.readlines()
df1 = pd.DataFrame(columns = ['fname', 'rev', 'date'])
date = ""
revision= ""
curr_file=""
for line in Lines2:
	lst = line.split()
	if(len(lst)>0):
		if(lst[0]=="Revision:"):
			revision=lst[1]
		if(lst[0]=="Date:"):
			date = lst[1]+" "+lst[2]+" "+lst[3]
		if(lst[0]=="Modified"):
			curr_file = lst[2]
			df1.loc[len(df1.index)] = [curr_file,revision,date]
			







df.to_csv("C:/Users/BITS-PC/Desktop/ChangeMetrics.csv")
df1.to_csv("C:/Users/BITS-PC/Desktop/LogMetrics.csv")


  	
