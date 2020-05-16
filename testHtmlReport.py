class TestHtmlReport:
    HTMLSCRIPt = """
function show(obj){
    var ele_log = document.getElementsByName('log');
    var ele_detail = document.getElementsByName("detail");
    var i = ele_log.length;
    while (i--) {
        if (ele_detail[i] ==obj) {
            break
        }
    }
    if (ele_log[i].hasAttribute("hidden")){
          ele_log[i].removeAttribute("hidden");
          ele_detail[i].innerHTML="收起";
    }else {
          ele_detail[i].innerHTML="详细";
          ele_log[i].setAttribute("hidden","true");
    }
}
function show_pass() {
    if (document.getElementById("pass").checked) {
        var eles = document.getElementsByName("rpass")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
           eles[index].removeAttribute("hidden")
        }
    }
    else {
        var eles = document.getElementsByName("rpass")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
            eles[index].setAttribute("hidden", "true")
        }
    }
}
function show_unpass() {
    if (document.getElementById("unpass").checked) {
        var eles = document.getElementsByName("runpass")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
           eles[index].removeAttribute("hidden")
        }
    }
    else {
        var eles = document.getElementsByName("runpass")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
            eles[index].setAttribute("hidden", "true")
        }
    }
}
function show_error() {
    if (document.getElementById("error").checked) {
        var eles = document.getElementsByName("rerror")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
           eles[index].removeAttribute("hidden")
        }
    }
    else {
        var eles = document.getElementsByName("rerror")
        var len = eles.length
        var index = 0
        for (index; index < len; index++) {
            eles[index].setAttribute("hidden", "true")
        }
    }
}
    """
    HTMLHEAD = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试报告</title>
    <script language="javascript">
{}
</script>
</head>
<body>
 <h1>自动化测试报告</h1>
 <p class ="attribute"><strong>浏览器环境：{}</strong></p>
 <p class ="attribute"><strong>测试地址：{}</strong></p>
 <p class ="attribute"><strong>用例开始执行时间：{}</strong></p>
 <p class ="attribute"><strong>总计耗时：{}</strong></p>
 <p class ="attribute"><strong>测试结果：{}</strong></p>
 <p class ="attribute"><strong>用例执行情况：</strong></p>
 <label style="background-color: green;"><input id="pass" checked onclick="show_pass()" type="checkbox" value="" />用例通过 : {}&nbsp&nbsp&nbsp </label>
 <label style="background-color: yellow;"><input id="unpass" checked onclick="show_unpass()" type="checkbox" value="" />用例不通过 : {}&nbsp&nbsp </label>
 <label style="background-color: red;"><input id="error" checked onclick="show_error()" type="checkbox" value="" />用例异常 : {}&nbsp&nbsp&nbsp </label>
 <table id="result_table" style="text-align: center" width="100%" border="1" cellpadding="2" cellspacing="1">
     <colgroup>
         <col align="left">
         <col align="right">
         <col align="right">
         <col align="right">
         <col align="right">
     </colgroup>
     <tr id ="header_row" style="font-weight: bold;font-size: 16px;">
         <td>所属模块</td>
         <td>用例标题</td>
         <td>日志记录</td>
         <td>耗费时间</td>
         <td>结果</td>
     </tr>
    """
    HTMLROWPASS = """
     <tr name="rpass">
         <td>{}</td>
         <td>{}</td>
         <td><a href="javascript:void(0)" onclick="show(this)" style="text-align: center" name="detail">详细</a>
             <pre name="log" style="text-align: left" hidden="true">
{}
         </pre>
         </td>
         <td>{}</td>
         <td style="background-color: green">{}</td>
     </tr>
     """
    HTMLROWUNPASS = """
<tr name="runpass">
         <td>{}</td>
         <td>{}</td>
         <td><a href="javascript:void(0)" onclick="show(this)" style="text-align: center" name="detail">详细</a>
             <pre name="log" style="text-align: left" hidden="true">
{}
         </pre>
         </td>
         <td>{}</td>
         <td style="background-color: yellow">{}</td>
     </tr>
    """
    HTMLROWERROR = """
<tr name="rerror">
         <td>{}</td>
         <td>{}</td>
         <td><a href="javascript:void(0)" onclick="show(this)" style="text-align: center" name="detail">详细</a>
             <pre name="log" style="text-align: left" hidden="true">
{}
         </pre>
         </td>
         <td>{}</td>
         <td style="background-color: red">{}</td>
     </tr>
    """
    HTMLEND = """
 </table>
</body>
</html>
    """
