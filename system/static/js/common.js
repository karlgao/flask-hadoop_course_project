
function init_chart(chartlist){
    chartlist.forEach(function(value,index,arrary) {
        var elem = value['elem_id'];
        console.log(elem)
        echarts.init(document.getElementById(elem))
    });
}

function flushchart(elem){
    var option = {
        title: {
            text: 'ECharts 入门示例'
        },
        tooltip: {},
        legend: {
            data:['销量']
        },
        xAxis: {
            data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
        },
        yAxis: {},
        series: [{
            name: '销量',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20]
        }]
    };

    // 使用刚指定的配置项和数据显示图表。

    var chart = echarts.getInstanceByDom(document.getElementById(elem));
    chart.setOption(option);
}