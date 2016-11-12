#Use the pandas module to answer the following questions about the EPA-HTTP data set.
#Print the result of each part to the console.  Use pandas as much as you can;
#this includes the data structure and the analysis.
#Use any other tools or techniques you need to create an efficient program.
#These include scipy, numpy, regex, Tkinter, etc.

import numpy
import pandas as pd
import datetime

epa_url = 'https://raw.githubusercontent.com/chrisgmartin/DATA602/master/epa-http.txt'
#import the text file as a table
epa_tab = pd.read_table(epa_url, header=None, squeeze=True)
#remove extra quotation mark
epa_tab = epa_tab.str.replace('gifalt\=\"', 'gifalt\=')
#extract first two columns
epa_df = pd.DataFrame(epa_tab.str.split(' ', 2).tolist(), columns=['host','datetime','rest'])
#extract third column
epa_df['request'] = epa_df['rest'].str.extract('\"(.+?)\"', expand=False)
#extract last two columns
epa_df['reply'] = epa_df['rest'].str.split(' ').str[-2]
epa_df['bytes'] = epa_df['rest'].str.split(' ').str[-1]
#drop relation column
epa_df = epa_df.drop('rest',1)

#data cleaning
#replace - (dash) in bytes column with zeros
epa_df['bytes'] = epa_df['bytes'].replace(to_replace='-', value=0)
#convert bytes to integer
epa_df['bytes'] = epa_df['bytes'].apply(pd.to_numeric)
#remove brackets from date column
epa_df['datetime'] = epa_df['datetime'].str.strip('[]')
#convert date column to date and time
epa_df['datetime'] =  '2015:08:' + epa_df['datetime']
epa_df['datetime'] = pd.to_datetime(epa_df['datetime'], format='%Y:%m:%d:%H:%M:%S')


#Which hostname or IP address made the most requests?
maxhost = epa_df['host']
maxhost = maxhost.groupby(maxhost).count()
maxhost = maxhost.sort_values(ascending=False)
print "The most requests went to %s with %d requests" %(maxhost.index[0], maxhost[0])


#Which hostname or IP address received the most total bytes from the server?  How many bytes did it receive?
hostbytes = {'host': epa_df['host'],'bytes': epa_df['bytes']}
hostbytes = pd.DataFrame(hostbytes)
totalbytes = hostbytes.groupby('host', sort=True).sum()
totalbytes = totalbytes.sort_values(by='bytes', ascending=False)
print "The hostname/IP address with the most bytes received was %s with %d bytes" %(totalbytes.index[0], totalbytes.iloc[0])


#During what hour was the server the busiest in terms of requests?  (You can do this by grouping each hour period e.g. 13:00 – 14:00. Then count the number of requests in each hour) 
time = epa_df['datetime'].dt.hour
time = time.groupby(time).count()
time = time.sort_values(ascending=False)
print "The busiest hour in terms of requests was hour %d" %(time.index[0])


#Which .gif image was downloaded the most during the day? 
giflist = epa_df['request']
giflist = giflist.str.extract('([A-Za-z0-9 ._]+.gif)', expand=False)
giflist = giflist.groupby(giflist).count()
giflist = giflist.sort_values(ascending=False)
print "The .gif with the most downloads was %s with %d downloads" %(giflist.index[0], giflist.iloc[0])

#If day times are 9am to 6pm
giflist2 = epa_df
giflist2['hour'] =  giflist2['datetime'].dt.hour
giflist2 = giflist2[(giflist2['hour']>8) & (giflist2['hour']<18)]
giflist2 = giflist2['request']
giflist2 = giflist2.str.extract('([A-Za-z0-9 ._]+.gif)', expand=False)
giflist2 = giflist2.groupby(giflist2).count()
giflist2 = giflist2.sort_values(ascending=False)
print "The .gif with the most daytime (9am-6pm) downloads was %s with %d downloads" %(giflist2.index[0], giflist2.iloc[0])


#What HTTP reply codes were sent other than 200?
replycodes = epa_df['reply'].unique()
replycodes = replycodes[(replycodes != '200')]
print "The HTTP reply codes other than 200 are %s" %(list(replycodes))