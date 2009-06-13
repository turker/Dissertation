import sqlite3 as db
from pylab import *

def connectToDB():
    dbcon = db.connect("XDAQSim.sqlite")
    cur = dbcon.cursor()
    return cur

def getThroughput(dbcursor):
    SELECT = "select value from Results where metricName = 'Throughput'"
    res = dbcursor.execute(SELECT)
    throughput = []
    for row in dbcursor:
        throughput.append(row[0])
    return throughput

def getMetric(dbcursor, name, range, negProbe, posProbe):
    SELECT = "select testID, value from Results where metricName = '" + name + "'" + " AND negativeEnd = '" + negProbe + "'" + " AND  positiveENd = '" + posProbe + "'"
	print SELECT
    dbcursor.execute(SELECT)
    result = []
    for row in dbcursor:
        result.append(row[0])
    return result

def plotversus (xdata, ydata, xlbl, ylbl, name):
    plot(xdata, ydata, linewidth=1.0)            
    xlabel(xlbl)
    ylabel(ylbl)
    title(name)
    grid(True)
    show()

def plotdata (xdata, xlbl, ylbl, name):
    plot(xdata,linewidth=1.0)            
    xlabel(xlbl)
    ylabel(ylbl)
    title(name)
    grid(True)

if __name__=='__main__':
	range = 1
	negProbe = "BU_in"
	posProbe = "BU_out"
	dbcur = connectToDB()
	throughput = getMetric(dbcur,'Throughput', range, negProbe, posProbe)
	average_event_size = getMetric(dbcur, 'Average Event Size', range, negProbe, posProbe)
	average_event_cycle = getMetric(dbcur, 'Latency', range, negProbe, posProbe)
	nb_evts_built = getMetric(dbcur, 'Number of Events', range, negProbe, posProbe)
	print throughput
	#print average_event_cycle
	#print average_event_size
	#print nb_evts_built
	#plotversus(average_event_cycle, throughput,'Average Event Cycle',
	#	    'Throughput', 'Average Event Cycle(Latency) vs. Throughput')
	#plotdata(average_event_cycle, 'Average Event Cycle','Tests', 
	#	    'Average Event Cycle(Latency)')
	#show()