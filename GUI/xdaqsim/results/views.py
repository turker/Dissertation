# Create your views here.

from django.shortcuts import render_to_response
from xdaqsim.results.models import Tests, Results, Parameters, Plot
from django.http import HttpResponse
from django.template import Context, loader
from django.utils import simplejson
import gviz_api

from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import XYLineChart
from pygooglechart import Axis
from pygooglechart import ScatterChart
from pygooglechart import StackedVerticalBarChart

import math


def index(request):
    all_tests = Tests.objects.all()

    #create data for visualization
    description = { "ID": ("number", "Test Id"),
                    "name": ("string", "Test Name"),
                    "created": ("datetime", "Created"),
                    "comment": ("string", "Comment"),
                    "localId": ("number", "Local Id"),
                    "details": ("string", "")}
    data = []
    for t in all_tests:
        row = {} 
        row["ID"] = t.id
        row["name"] = t.name
        row["created"] = t.created
        row["comment"] = t.comment
        row["localId"] = t.localId
        row["details"] = 'tests/' + str(t.id)  + '/'
        #row["details"] = '<a href="http://google.com">Details</a>'
        data.append(row)

    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    #Create the JSon string
    json = data_table.ToJSon(columns_order=("ID", "name", "created", "comment", "localId","details"),
            order_by="created")
                    
    return render_to_response('tests/index.html',
            {'all_tests': all_tests,
             'json': json }
            )


def all(request):
    all_results = Results.objects.all()
    all_params = Parameters.objects.all()
    #Create the data for visualization
    description_res = { "testID": ("number", "TestID"),
                    "metricName": ("string", "Metric"),
                    "value": ("number", "Value"),
                    "negativeEnd": ("string", "Negative End"),
                    "positiveEnd": ("string", "Positive End") }
    data_res = []
    for r in all_results:
        row = {}
        row["testID"] = r.testID
        row["metricName"] = r.metricName
        row["value"] = r.value
        row["negativeEnd"] = r.negativeEnd
        row["positiveEnd"] = r.positiveEnd
        data_res.append(row)
    
    data_table_res = gviz_api.DataTable(description_res)
    data_table_res.LoadData(data_res)

    description_param = { "testID": ("number", "TestID"),
                    "name": ("string", "Metric"),
                    "value": ("number", "Value") }
    data_param = []
    for p in all_params:
        row = {}
        row["testID"] = p.testID
        row["name"] = p.name
        row["value"] = p.value
        data_param.append(row)
    
    data_table_param = gviz_api.DataTable(description_param)
    data_table_param.LoadData(data_param)

    #Create the JSon strings
    json_res = data_table_res.ToJSon(columns_order=("testID", "metricName", "value",
        "negativeEnd", "positiveEnd"), order_by="testID")
    json_param = data_table_param.ToJSon(columns_order=("testID", "name", "value"), order_by="testID")

    return render_to_response('tests/all.html',
            {'all_results': all_results,
             'json_res': json_res,
             'json_param': json_param }
            )


def detail(request, test_id):
#    return HttpResponse("You are looking at test %s." %test_id)
    test_info = Tests.objects.filter(id=test_id)
    all_results = Results.objects.filter(testID=test_id)
    all_params = Parameters.objects.filter(testID=test_id)
    all_plots = Plot.objects.all()
    #Create the data for vizualization
    description_res = { "testID": ("number", "TestID"),
                    "metricName": ("string", "Metric"),
                    "value": ("number", "Value"),
                    "negativeEnd": ("string", "Negative End"),
                    "positiveEnd": ("string", "Positive End") }
    data_res = []
    for r in all_results:
        row = {}
        row["testID"] = r.testID
        row["metricName"] = r.metricName
        row["value"] = r.value
        row["negativeEnd"] = r.negativeEnd
        row["positiveEnd"] = r.positiveEnd
        data_res.append(row)
    
    data_table_res = gviz_api.DataTable(description_res)
    data_table_res.LoadData(data_res)

    description_param = { "testID": ("number", "TestID"),
                    "name": ("string", "Metric"),
                    "value": ("number", "Value") }
    data_param = []
    for p in all_params:
        row = {}
        row["testID"] = p.testID
        row["name"] = p.name
        row["value"] = p.value
        data_param.append(row)
    
    data_table_param = gviz_api.DataTable(description_param)
    data_table_param.LoadData(data_param)

    #Create the JSon strings
    json_res = data_table_res.ToJSon(columns_order=("testID", "metricName", "value",
        "negativeEnd", "positiveEnd"), order_by="testID")
    json_param = data_table_param.ToJSon(columns_order=("testID", "name", "value"), order_by="testID")
    
    #Determine related plots
    for p in all_plots:
        sid = p.startTestID
        eid = p.endTestID
        k = int(test_id) 
        if k in range(sid, eid+1):
            related_plots = all_plots.filter(startTestID=sid).distinct()
            related_plots = related_plots.filter(endTestID=eid).distinct()
            break
    
    plots = []
    for rp in related_plots:
        if rp.imageName not in plots:
            plots.append(rp.imageName)

    return render_to_response('tests/detail.html',
            {'test_id': test_id,
            'all_results': all_results,
            'test_info': test_info,
            'json_res': json_res,
            'related_plots': related_plots,
            'plots': plots,
            'json_param': json_param }
            )

def select(request):
    id = request.POST['post_data']
    range = id
    results = Results.objects.filter(testID=id)
    parameters = Parameters.objects.filter(testID=id)

    description = { 
                    "metricName": ("string", "Metric"),
                    "negativeEnd": ("string", "Negative End"),
                    "positiveEnd": ("string", "Positive End") }
    data = []
    for r in results:
        row = {}
        row["metricName"] = r.metricName
        row["negativeEnd"] = r.negativeEnd
        row["positiveEnd"] = r.positiveEnd
        data.append(row)

    params = []
    for p in parameters:
        params.append(p.name)
    
        
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    metric_json = data_table.ToJSon(columns_order=("metricName", "negativeEnd", "positiveEnd"), order_by="metricName")
    response = {}
    response["response_text"] = metric_json 
    response["range"] = range
    response["params"] = params
    response_json = simplejson.dumps(response)
    return HttpResponse(response_json, mimetype="application/json")

def plot(request):

    #Get plot parameters
    metY = []
    metX = request.POST['metX']
    negX = request.POST['negX']
    posX = request.POST['posX']
    negY = request.POST['negY']
    posY = request.POST['posY']
    idrangeStart = request.POST['rangeStart']
    idrangeEnd = request.POST['rangeEnd']
    chartType = request.POST['chartType']
    overlay = request.POST['overlay']
    xIsParam = request.POST['xIsParam']

    #Handle Y axis metrics differently
    nbmetY = request.POST['numberY']
    for i in range(int(nbmetY)):
        postKey = 'metY_' + str(i)
        print postKey
        metY.append(request.POST[postKey])

    
    print xIsParam

    if xIsParam == "false":
        metXValues = Results.objects.filter(metricName=metX)
        metXValues = metXValues.filter(testID__gte=idrangeStart)
        metXValues = metXValues.filter(testID__lte=idrangeEnd)
        metXValues = metXValues.filter(negativeEnd=negX)
        metXValues = metXValues.filter(positiveEnd=posX)
    else:
        metXValues = Parameters.objects.filter(name=metX)
        

    metYValues = {}
    for my in metY:
        metYValues[my] = Results.objects.filter(metricName=my)
        metYValues[my] = metYValues[my].filter(testID__gte=idrangeStart)
        metYValues[my] = metYValues[my].filter(testID__lte=idrangeEnd)
        metYValues[my] = metYValues[my].filter(negativeEnd=negY)
        metYValues[my] = metYValues[my].filter(positiveEnd=posY)
    
    xdata = []
    ydata = {}
    if metX == "Tests":
        r1 = int(idrangeStart)
        r2 = int(idrangeEnd)
        r2 = r2 + 1
        for i in range(r1, r2):
            xdata.append(i)
    else:
        for mx in metXValues:
            xdata.append(mx.value)

    temp = []
    for my in metYValues:
        for y in metYValues[my]:
            temp.append(y.value)
        ydata[my] = temp
        temp = []


    #form x-axis data
    sxdata = []
    if metX == "Tests":
        sxdata = xdata
    else:
        for sx in xdata:
            sxdata.append(round(sx / math.pow(10,0),3))

    max_x = max(sxdata)

    #form y-axis data
    temp = []
    sydata = {} 
    yaxis = []
    for sy in ydata:
        yaxis.append(sy)
        for y in ydata[sy]:
            temp.append(round(y / math.pow(10,0), 3))
            sydata[sy] = temp
        temp = []
        #Also determine max_y in this loop
        if overlay == "1":
            max_y = max(sydata[sy])

    imageNames = []
    if overlay == "1":
        print 'in overlay = 1'
        #Plot all data points on one chart
        chart = plotChart(sxdata, sydata, overlay, max_x, max_y, chartType)
        print "got chart"
        #Set chart name and other chart information
        yname = ""
        for yx in yaxis:
            if yname == "":
                yname = yx
            else:
                yname = yname + '_' + yx
        imageName = yname + '_vs_' + metX + '.png'
        imageNames.append(imageName)
        fileName = 'results/plots/'+ imageName
        chart.set_legend(yaxis)
        chartTitle = yname + ' vs. ' + metX
        chart.set_title(chartTitle)
        index_x = chart.set_axis_labels(Axis.BOTTOM, sxdata)
        #tempy = sydata['Throughput']
        #index_y = chart.set_axis_labels(Axis.LEFT, sydata)
        #chart.set_axis_labels(Axis.RIGHT, sydata['Latency'])
        chart.set_axis_style(index_x, '202020', font_size=10, alignment=0)
        #chart.set_axis_style(index_y, '202020', font_size=10, alignment=0)
        #chart.download(fileName)
        print 'saving plot'
        p = Plot(startTestID = idrangeStart, endTestID = idrangeEnd, imageName=imageName)
        p.save()
        print 'chart will be downloaded'
        print 'filename= ' + fileName
        chart.download(fileName)
        print 'chart downloaded'
        #response = {}
        #response["imagename"] = imageNames
        #response["response_text"] = "image downloaded"

    else:
        print 'in overlay = 0'
        #Generate individual plots as many as number of y-axis data
        for yx in yaxis:
            max_y = max(sydata[yx])
            chart = plotChart(sxdata, sydata[yx], overlay, max_x, max_y, chartType)
            print "got chart"
            imageName = yx + '_vs_' + metX + '.png'
            imageNames.append(imageName)
            fileName = 'results/plots/' + imageName
            chart.set_legend([yx])
            chartTitle = yx + ' vs. ' + metX
            chart.set_title(chartTitle)
            index_x = chart.set_axis_labels(Axis.BOTTOM, sxdata)
            chart.set_axis_style(index_x, '202020', font_size=10, alignment=0)
            p = Plot(startTestID = idrangeStart, endTestID = idrangeEnd, imageName=imageName)
            p.save()
            chart.download(fileName)
        
    response = {}
    print imageNames
    response["imagenames"] = imageNames
    response["response_text"] = "image downloaded"

    return HttpResponse(simplejson.dumps(response), mimetype="image/png")

def plotChart(xdata, ydata, overlay, max_x=0, max_y=0, type='SimpleLineChart'):
    print "in plotChart"
    if type == "SimpleLineChart":
        chart = SimpleLineChart(600, 250, y_range=(0,max_y))
        if overlay == "1":
            for y in ydata:
                chart.add_data(ydata[y])
        else:
            print ydata
            chart.add_data(ydata)
        #chart.set_colours(['646464', '153ABC', 'A43434'])

    elif type == "XYLineChart":
        chart = XYLineChart(600, 250, x_range=(0,max_x), y_range=(0, max_y))
        for y in ydata:
            chart.add_data(xdata)
	    print 'Adding ' + y + ' data'
	    print ydata[y]
            chart.add_data(ydata[y])
            #chart.add_data([0] * 2)
        #chart.set_colours(['EEEEEE', '000000'])

    elif type == "StackedVerticalBarChart":
        chart = StackedVerticalBarChart(600, 250, x_range=(0,max_x), y_range=(0, max_y))
        print ydata
        for y in ydata:
            chart.add_data(ydata[y])
            #chart.add_data([0] * 2)
            #chart.set_colours(['4D89F9', 'C6D9FD'])
    return chart


