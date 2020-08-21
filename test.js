
<link href="css/default_text.css" rel="stylesheet" />



    <!DOCTYPE html PUBLIC "-//W3C//DTD html 4.0 Transitional//EN" >
        <html>
            <head>
                <title>RegistForm</title>
                <meta content="Microsoft Visual Studio .NET 7.1" name="GENERATOR" />
                <meta content="C#" name="CODE_LANGUAGE" />
                <meta content="JavaScript" name="vs_defaultClientScript" />
                <meta content="http://schemas.microsoft.com/intellisense/ie5" name="vs_targetSchema" />
                <meta http-equiv="Page-Enter" content="blendTrans(duration=0.1)" />
                <meta http-equiv="Page-Exit" content="blendTrans(duration=0.1)" />
                <style type="text/css">
                    .columnname {
                        font - weight: bold;
            text-align: right;
            font-family: 'Microsoft JhengHei';
            height: 35px;
            vertical-align: middle;
        }

        .style1 {
                        width: 196px;
        }

        .style2 {
                        width: 113px;
        }

        .style3 {
                        width: 278px;
        }

        .button {
                    }

        .auto-style1 {
                        height: 35px;
        }
    </style>
                <script type="text/javascript" src="JavaScript/jquery-1.10.2.js"></script>
                <script type="text/javascript">
                    $(document).ready(function () {
                        $(".cc_number").change(function () {
                            if (isNaN($(this).val())) {
                                $(this).val("");
                                $("#labPatBaseError2").html($(this).attr("title") + "，煩請輸入數值，謝謝！");
                            }
                        });

            $(".cc_exercise").click(function () {
                        $("#tb_ec04").attr("disabled", true);
                $("#tb_ec05").attr("disabled", true);
                $("#cb_ec06").attr("disabled", true);
                // 判斷 CheckBox是否有多一層span的物件
                if ($("#cb_ec06").closest("span").length == 1)
                    $("#cb_ec06").parent().attr("disabled", true);
                switch ($(this).find("input[type=radio]").attr("id")) {
                    case "rbl_ec01":
                    case "rbl_ec02":
                    case "rbl_ec03":
                        break;
                    case "rbl_ec04":
                        $("#tb_ec04").attr("disabled", false);
                        $("#tb_ec05").attr("disabled", false);
                        $("#cb_ec06").attr("disabled", false);
                        if ($("#cb_ec06").closest("span").length == 1)
                            $("#cb_ec06").parent().attr("disabled", false);
                        break;
                }
            });

            $("#cb_f508").click(function () {
                if (!$(this).prop("checked"))
                    $("#tb_f508").val("");

                $("#tb_f508").prop("disabled", !$(this).prop("checked"));
            });

            $("#cb_f504").click(function () {
                if (!$(this).prop("checked"))
                    $("#tb_f504").val("");

                $("#tb_f504").prop("disabled", !$(this).prop("checked"));
            });

            $("#cb_f509").click(function () {
                if (!$(this).prop("checked"))
                    $("#tb_f509").val("");

                $("#tb_f509").prop("disabled", !$(this).prop("checked"));
            });

            $("#cb_f50c").click(function () {
                if (!$(this).prop("checked"))
                    $("#tb_f50c").val("");

                $("#tb_f50c").prop("disabled", !$(this).prop("checked"));
            });

            $("#cb_f50d").click(function () {
                if (!$(this).prop("checked"))
                    $("#tb_f50d").val("");

                $("#tb_f50d").prop("disabled", !$(this).prop("checked"));
            });

            $("#cb_f50e").click(function () {
                if (!$(this).prop("checked"))
                    $("#tb_f50e").val("");

                $("#tb_f50e").prop("disabled", !$(this).prop("checked"));
            });

            $("#cb_f50o").click(function () {
                if (!$(this).prop("checked"))
                    $("#tb_f50o").val("");

                $("#tb_f50o").prop("disabled", !$(this).prop("checked"));
            });

            $("#cb_f30c").click(function () {
                if ($(this).prop("checked"))
                    $("#tb_f30c").val("");

                $("#tb_f30c").prop("disabled", $(this).prop("checked"));
            });

            $("#cb_f30d").click(function () {
                if ($(this).prop("checked"))
                    $("#tb_f30d").val("");

                $("#tb_f30d").prop("disabled", $(this).prop("checked"));
            });

            $("#cb_f506").click(function () {
                if ($(this).prop("checked")) {
                        $("#cb_f507").prop("checked", !$(this).prop("checked"))
                    $("#cb_f508").prop("checked", !$(this).prop("checked"))
                    $("#cb_f504").prop("checked", !$(this).prop("checked"))
                    $("#cb_f509").prop("checked", !$(this).prop("checked"))
                    $("#cb_f50a").prop("checked", !$(this).prop("checked"))
                    $("#cb_f50b").prop("checked", !$(this).prop("checked"))
                    $("#cb_f50c").prop("checked", !$(this).prop("checked"))
                    $("#cb_f50d").prop("checked", !$(this).prop("checked"))
                    $("#cb_f503").prop("checked", !$(this).prop("checked"))
                    $("#cb_f50e").prop("checked", !$(this).prop("checked"))
                    $("#cb_f50o").prop("checked", !$(this).prop("checked"))

                    $("#tb_f508").val("");
                    $("#tb_f504").val("");
                    $("#tb_f509").val("");
                    $("#tb_f50c").val("");
                    $("#tb_f50d").val("");
                    $("#tb_f50e").val("");
                    $("#tb_f50o").val("");
                }

                $("#cb_f507").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f507").closest("span").length == 1)
                    $("#cb_f507").parent().prop("disabled", $(this).prop("checked"));

                $("#cb_f508").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f508").closest("span").length == 1)
                    $("#cb_f508").parent().prop("disabled", $(this).prop("checked"));

                $("#tb_f508").prop("disabled", true);

                $("#cb_f504").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f504").closest("span").length == 1)
                    $("#cb_f504").parent().prop("disabled", $(this).prop("checked"));

                $("#tb_f504").prop("disabled", true);

                $("#cb_f509").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f509").closest("span").length == 1)
                    $("#cb_f509").parent().prop("disabled", $(this).prop("checked"));

                $("#tb_f509").prop("disabled", true);

                $("#cb_f50a").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f50a").closest("span").length == 1)
                    $("#cb_f50a").parent().prop("disabled", $(this).prop("checked"));

                $("#cb_f50b").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f50b").closest("span").length == 1)
                    $("#cb_f50b").parent().prop("disabled", $(this).prop("checked"));

                $("#cb_f50c").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f50c").closest("span").length == 1)
                    $("#cb_f50c").parent().prop("disabled", $(this).prop("checked"));

                $("#tb_f50c").prop("disabled", true);

                $("#cb_f50d").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f50d").closest("span").length == 1)
                    $("#cb_f50d").parent().prop("disabled", $(this).prop("checked"));

                $("#tb_f50d").prop("disabled", true);

                $("#cb_f503").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f503").closest("span").length == 1)
                    $("#cb_f503").parent().prop("disabled", $(this).prop("checked"));

                $("#cb_f50e").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f50e").closest("span").length == 1)
                    $("#cb_f50e").parent().prop("disabled", $(this).prop("checked"));

                $("#tb_f50e").prop("disabled", true);

                $("#cb_f50o").prop("disabled", $(this).prop("checked"));
                if ($("#cb_f50o").closest("span").length == 1)
                    $("#cb_f50o").parent().prop("disabled", $(this).prop("checked"));

                $("#tb_f50o").prop("disabled", true);
            });
        });
    </script>
            </head>
            <body>
                <div class="ABCClass">
                    <form name="Form1" method="post" action="RegistForm.aspx?newx=UwBlAHIAdgBpAGMAZQBJAEQAUwBFAD0ANAAzADEAOAAxADUAMwAmAEUAbgBjAHIAeQBwAHQAQwBvAGQAZQA9AFQAMABTAFUAUgBHADAAOQAyADAAMgAwADAAOQAwADIAJgB1AHMAZQBEAHIAUgBlAHMAdABDAG4AdAA9AG4A0" id="Form1">
                        <input type="hidden" name="scrollLeft" id="scrollLeft" value="0" />
                        <input type="hidden" name="scrollTop" id="scrollTop" value="163.1999969482422" />
                        <input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
                        <input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
                        <input type="hidden" name="__LASTFOCUS" id="__LASTFOCUS" value="" />
                        <input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKLTg5ODA5MjQ5OA9kFgICAg9kFgICAQ9kFgoCBw9kFgICAw9kFgpmD2QWAgIBD2QWAgIBDw8WAh4EVGV4dAUYMTA5LjkuMiDmmJ/mnJ/kuIkg5LiK5Y2IZGQCAQ9kFgICAQ9kFgICAQ8PFgIfAAUJ5aSW56eR6YOoZGQCAg9kFgICAQ9kFgICAQ8PFgIfAAUp5pmu6YCa6ZaA6Ki6IOesrDA56Ki6ICjku6PnorzvvJogMTAzMjA5IClkZAIDD2QWAgIBD2QWAgIBDw8WAh8ABRHpmbPnn7PmsaAgIOmGq+W4q2RkAgQPZBYCAgEPZBYCAgEPDxYCHwAFFee4vemZouWNgC3opb/lnYAtMeaok2RkAgkPZBYCAgUPZBYKZg9kFgRmD2QWAgIDDxBkZBYBAgFkAgEPZBYGAgEPDxYEHgdWaXNpYmxlaB8AZWRkAgMPDxYCHwFnZGQCBQ8PFgQfAWgfAGVkZAIBD2QWAgIBD2QWBgIBDxBkEBWYAQnoq4vpgbjmk4cG5YmNIDQyBuWJjSA0MQbliY0gNDAG5YmNIDM5BuWJjSAzOAbliY0gMzcG5YmNIDM2BuWJjSAzNQbliY0gMzQG5YmNIDMzBuWJjSAzMgbliY0gMzEG5YmNIDMwBuWJjSAyOQbliY0gMjgG5YmNIDI3BuWJjSAyNgbliY0gMjUG5YmNIDI0BuWJjSAyMwbliY0gMjIG5YmNIDIxBuWJjSAyMAbliY0gMTkG5YmNIDE4BuWJjSAxNwbliY0gMTYG5YmNIDE1BuWJjSAxNAbliY0gMTMG5YmNIDEyBuWJjSAxMQbliY0gMTAF5YmNIDkF5YmNIDgF5YmNIDcF5YmNIDYF5YmNIDUF5YmNIDQF5YmNIDMF5YmNIDIF5YmNIDEBMQEyATMBNAE1ATYBNwE4ATkCMTACMTECMTICMTMCMTQCMTUCMTYCMTcCMTgCMTkCMjACMjECMjICMjMCMjQCMjUCMjYCMjcCMjgCMjkCMzACMzECMzICMzMCMzQCMzUCMzYCMzcCMzgCMzkCNDACNDECNDICNDMCNDQCNDUCNDYCNDcCNDgCNDkCNTACNTECNTICNTMCNTQCNTUCNTYCNTcCNTgCNTkCNjACNjECNjICNjMCNjQCNjUCNjYCNjcCNjgCNjkCNzACNzECNzICNzMCNzQCNzUCNzYCNzcCNzgCNzkCODACODECODICODMCODQCODUCODYCODcCODgCODkCOTACOTECOTICOTMCOTQCOTUCOTYCOTcCOTgCOTkDMTAwAzEwMQMxMDIDMTAzAzEwNAMxMDUDMTA2AzEwNwMxMDgDMTA5FZgBAAQxODcwBDE4NzEEMTg3MgQxODczBDE4NzQEMTg3NQQxODc2BDE4NzcEMTg3OAQxODc5BDE4ODAEMTg4MQQxODgyBDE4ODMEMTg4NAQxODg1BDE4ODYEMTg4NwQxODg4BDE4ODkEMTg5MAQxODkxBDE4OTIEMTg5MwQxODk0BDE4OTUEMTg5NgQxODk3BDE4OTgEMTg5OQQxOTAwBDE5MDEEMTkwMgQxOTAzBDE5MDQEMTkwNQQxOTA2BDE5MDcEMTkwOAQxOTA5BDE5MTAEMTkxMQQxOTEyBDE5MTMEMTkxNAQxOTE1BDE5MTYEMTkxNwQxOTE4BDE5MTkEMTkyMAQxOTIxBDE5MjIEMTkyMwQxOTI0BDE5MjUEMTkyNgQxOTI3BDE5MjgEMTkyOQQxOTMwBDE5MzEEMTkzMgQxOTMzBDE5MzQEMTkzNQQxOTM2BDE5MzcEMTkzOAQxOTM5BDE5NDAEMTk0MQQxOTQyBDE5NDMEMTk0NAQxOTQ1BDE5NDYEMTk0NwQxOTQ4BDE5NDkEMTk1MAQxOTUxBDE5NTIEMTk1MwQxOTU0BDE5NTUEMTk1NgQxOTU3BDE5NTgEMTk1OQQxOTYwBDE5NjEEMTk2MgQxOTYzBDE5NjQEMTk2NQQxOTY2BDE5NjcEMTk2OAQxOTY5BDE5NzAEMTk3MQQxOTcyBDE5NzMEMTk3NAQxOTc1BDE5NzYEMTk3NwQxOTc4BDE5NzkEMTk4MAQxOTgxBDE5ODIEMTk4MwQxOTg0BDE5ODUEMTk4NgQxOTg3BDE5ODgEMTk4OQQxOTkwBDE5OTEEMTk5MgQxOTkzBDE5OTQEMTk5NQQxOTk2BDE5OTcEMTk5OAQxOTk5BDIwMDAEMjAwMQQyMDAyBDIwMDMEMjAwNAQyMDA1BDIwMDYEMjAwNwQyMDA4BDIwMDkEMjAxMAQyMDExBDIwMTIEMjAxMwQyMDE0BDIwMTUEMjAxNgQyMDE3BDIwMTgEMjAxOQQyMDIwFCsDmAFnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZxYBAn5kAgMPEGQQFQ0J6KuL6YG45pOHAjAxAjAyAjAzAjA0AjA1AjA2AjA3AjA4AjA5AjEwAjExAjEyFQ0AAjAxAjAyAjAzAjA0AjA1AjA2AjA3AjA4AjA5AjEwAjExAjEyFCsDDWdnZ2dnZ2dnZ2dnZ2cWAQIMZAIFDxBkEBUgCeiri+mBuOaThwIwMQIwMgIwMwIwNAIwNQIwNgIwNwIwOAIwOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNQIyNgIyNwIyOAIyOQIzMAIzMRUgAAIwMQIwMgIwMwIwNAIwNQIwNgIwNwIwOAIwOQIxMAIxMQIxMgIxMwIxNAIxNQIxNgIxNwIxOAIxOQIyMAIyMQIyMgIyMwIyNAIyNQIyNgIyNwIyOAIyOQIzMAIzMRQrAyBnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgIPZBYEZg9kFgYCAw8PFgIeCEltYWdlVXJsBVxWYWxpZE51bWJlci5hc3B4P2NoZWNrQ29kZT1OQUI2QUVvQVl3QmpBRXNBY2dBMUFHWUFiQUJNQUdZQUx3QXlBRk1BZFFCWEFEWUFhZ0JCQURVQVp3QTlBRDBBMGRkAgcPDxYCHwAFBkI0ODhMWmRkAgkPDxYCHwAFAVlkZAIBD2QWAgIBDw9kFgIeCW9ua2V5ZG93bgUXZm5UcmFwS0QoYnRuT0ssIGV2ZW50KTtkAgMPZBYCZg9kFgICAw8PFgQeBF8hU0ICCB4JQmFja0NvbG9yCp4BZGQCBA9kFgJmD2QWAgIBD2QWAgIHDxBkZBYBZmQCCw8PFgIfAWhkFgICAQ9kFgQCAg9kFgICAw9kFgICAQ8QZGQWAWZkAgQPZBYCAgEPZBYYAgEPEGRkFgBkAgMPEGRkFgBkAgUPZBYCAgEPZBYGAgMPEGRkFgFmZAIFDxBkZBYBZmQCCw8PFgIfAGVkZAIJD2QWAgIBD2QWBgIDDxBkZBYBZmQCBQ8QZGQWAWZkAgsPDxYCHwBlZGQCEQ8QZGQWAGQCEw8QZGQWAGQCGw8QZGQWAGQCIw9kFgICAQ9kFgYCAw8QZGQWAWZkAgUPEGRkFgFmZAILDw8WAh8AZWRkAiUPZBYMZg9kFgICAQ9kFgICAQ8QZGQWAGQCAQ9kFgICAQ9kFgICAQ8QZGQWAGQCAg9kFgICAQ9kFgICAQ8QZGQWAGQCAw9kFgICAQ9kFgICAQ8QZGQWAGQCBA9kFgICAQ9kFgICAQ8QZGQWAGQCBQ9kFgICAQ9kFgICAQ8QZGQWAGQCJw9kFgICBA9kFgICAQ9kFgICAQ8QZGQWAGQCKQ9kFgQCBQ9kFgICAQ9kFgICAQ8QZGQWAGQCBg9kFgICAQ9kFgICAQ8QZGQWAGQCNQ8PFgIfAAUdMTA55bm0OeaciDLml6XkuIrljYgg56ysMDnoqLpkZAINDw8WAh8BaGRkAg8PDxYCHwFoZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFC2J0blJlTmV3TnVtdOanodcpJKkJllwnnl4MA4GEW+I=" />

                        <script type="text/javascript">
                            <!--
var theForm = document.forms['Form1'];
if (!theForm) {
                                theForm = document.Form1;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
                                theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
// -->
</script>


                        <script language="javascript">
                            <!--
function OnLoadFun()
										{
                                SmartScroller_Scroll();
										}function SmartScroller_GetCoords() {
var scrollX, scrollY;
if (document.all) {
if (!document.documentElement.scrollLeft)
scrollX = document.body.scrollLeft;
else
scrollX = document.documentElement.scrollLeft;
if (!document.documentElement.scrollTop)
scrollY = document.body.scrollTop;
else
scrollY = document.documentElement.scrollTop; }
else {
                                scrollX = window.pageXOffset; scrollY = window.pageYOffset; }

document.getElementById('scrollLeft').value = scrollX;
document.getElementById('scrollTop').value = scrollY;
}

function SmartScroller_Scroll() {
var x = document.getElementById('scrollLeft').value;
var y = document.getElementById('scrollTop').value;
window.scrollTo(x, y); }

window.onload = OnLoadFun;
window.onscroll = SmartScroller_GetCoords;
window.onclick = SmartScroller_GetCoords; window.onkeypress = SmartScroller_GetCoords;document.body.style.marginLeft = 0;
// -->
</script>
                        <input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="A291BFFA" />
                        <script type="text/javascript">

                            function myDisableButton(obj) {
                                obj.className = "DisableButton";
                    obj.value = "處理中..";
                    obj.onclick = Function("return false;");
                    return true;
                }
            </script>
                        <a href="http://www.ntuh.gov.tw/無障礙網頁_rg.htm" accesskey="C" title="資料內容區" style="text-decoration: none" target="_blank">:::</a>
                        <table cellspacing="0" cellpadding="0" width="72%" align="center">
                            <tr>
                                <td align="center">
                                    <img id="Image1" alt="網路預約掛號" src=".\Images\Regist9.gif" border="0" />
                                    <br />
                                </td>
                            </tr>
                            <tr>
                                <td>

                                </td>
                            </tr>
                            <tr>
                                <td>

                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <div id="Panel1">

                                        <table width="100%" align="center">
                                            <tr>
                                                <td>
                                                    <img id="Image2" alt="預約掛號資料" src=".\Images\reg_info_book.gif" border="0" /></td>
                                            </tr>
                                            <tr>
                                                <td>
                                                    <table id="Table1" style="border-color: #dcc38a;" cellspacing="0" cellpadding="0" width="80%" border="1">
                                                        <tr>
                                                            <td style="background-color: #f8f0e0;" class="style2"><font color="#800000">時 間:</font>
                                                            </td>
                                                            <td>
                                                                <span id="ShowTime" style="font-size:16pt;">109.9.2 星期三 上午</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="background-color: #f8f0e0;" class="style2"><font color="#800000">科 別:</font></td>
                                                            <td>
                                                                <span id="ShowDept">外科部</span></td>
                                                        </tr>
                                                        <tr>
                                                            <td style="background-color: #f8f0e0;" class="style2"><font color="#800000">診 別:</font></td>
                                                            <td>
                                                                <span id="ShowClinic">普通門診 第09診 (代碼： 103209 )</span></td>
                                                        </tr>
                                                        <tr>
                                                            <td style="background-color: #f8f0e0;" class="style2"><font color="#800000">醫事人員:</font></td>
                                                            <td>
                                                                <span id="ShowDt">陳石池  醫師</span></td>
                                                        </tr>
                                                        <tr>
                                                            <td style="background-color: #f8f0e0;" class="style2"><font color="#800000">看診地點:</font></td>
                                                            <td>
                                                                <span id="ShowLoc">總院區-西址-1樓</span></td>
                                                        </tr>
                                                    </table>

                                                </td>
                                            </tr>
                                        </table>

                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <div id="pa1PatType">

                                        <table width="100%" align="center">
                                            <table width="100%" columnspan="2">
                                                <tr>
                                                    <td class="style1">
                                                        <img id="Image3" alt="病友身分認證" src=".\Images\pat_certify.gif" border="0" />
                                                    </td>
                                                    <td>
                                                        <span id="ShowMsg" style="color:#CC0000;"></span>
                                                    </td>
                                                </tr>
                                            </table>

                                            <tr>
                                                <td>
                                                    <table id="Table2" style="border-color: #dcc38a;" cellspacing="0" cellpadding="0" bgcolor="#fcf9f3" border="1">
                                                        <tr>
                                                            <td style="background-color: #f8f0e0;" class="style3">
                                                                <span id="lblIdno" style="font-size: small">
                                                                    <font color="#800000">請輸入您的:(請點選其一)</font></span>
                                                                <table id="radInputNum" border="0">
                                                                    <tr>
                                                                        <td><input id="radInputNum_0" type="radio" name="radInputNum" value="0" onclick="javascript:setTimeout('__doPostBack(\'radInputNum$0\',\'\')', 0)" language="javascript" /><label for="radInputNum_0">病歷號碼 (七位文數字) </label></td>
                                                                    </tr><tr>
                                                                        <td><input id="radInputNum_1" type="radio" name="radInputNum" value="1" checked="checked" /><label for="radInputNum_1">身分證號碼(十位文數字)</label></td>
                                                                    </tr><tr>
                                                                        <td><input id="radInputNum_2" type="radio" name="radInputNum" value="2" onclick="javascript:setTimeout('__doPostBack(\'radInputNum$2\',\'\')', 0)" language="javascript" /><label for="radInputNum_2">其它 (居留證號等)</label></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                            <td>
                                                                <br />
                                                                <br />
                                                                <input name="txtIdno" type="text" maxlength="10" id="txtIdno" style="ime-mode: disabled;" /><br />
                                                                <br />

                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="background-color: #f8f0e0;" class="style3">
                                                                <span id="lbl2">
                                                                    <font color="#800000">請輸入您的出生日期 :</font></span>
                                                            </td>
                                                            <td>民國
										            <select name="ddlBirthYear" onchange="javascript:setTimeout('__doPostBack(\'ddlBirthYear\',\'\')', 0)" language="javascript" id="ddlBirthYear" style="width:60px;">
                                                                    <option value="">請選擇</option>
                                                                    <option value="1870">前 42</option>
                                                                    <option value="1871">前 41</option>
                                                                    <option value="1872">前 40</option>
                                                                    <option value="1873">前 39</option>
                                                                    <option value="1874">前 38</option>
                                                                    <option value="1875">前 37</option>
                                                                    <option value="1876">前 36</option>
                                                                    <option value="1877">前 35</option>
                                                                    <option value="1878">前 34</option>
                                                                    <option value="1879">前 33</option>
                                                                    <option value="1880">前 32</option>
                                                                    <option value="1881">前 31</option>
                                                                    <option value="1882">前 30</option>
                                                                    <option value="1883">前 29</option>
                                                                    <option value="1884">前 28</option>
                                                                    <option value="1885">前 27</option>
                                                                    <option value="1886">前 26</option>
                                                                    <option value="1887">前 25</option>
                                                                    <option value="1888">前 24</option>
                                                                    <option value="1889">前 23</option>
                                                                    <option value="1890">前 22</option>
                                                                    <option value="1891">前 21</option>
                                                                    <option value="1892">前 20</option>
                                                                    <option value="1893">前 19</option>
                                                                    <option value="1894">前 18</option>
                                                                    <option value="1895">前 17</option>
                                                                    <option value="1896">前 16</option>
                                                                    <option value="1897">前 15</option>
                                                                    <option value="1898">前 14</option>
                                                                    <option value="1899">前 13</option>
                                                                    <option value="1900">前 12</option>
                                                                    <option value="1901">前 11</option>
                                                                    <option value="1902">前 10</option>
                                                                    <option value="1903">前 9</option>
                                                                    <option value="1904">前 8</option>
                                                                    <option value="1905">前 7</option>
                                                                    <option value="1906">前 6</option>
                                                                    <option value="1907">前 5</option>
                                                                    <option value="1908">前 4</option>
                                                                    <option value="1909">前 3</option>
                                                                    <option value="1910">前 2</option>
                                                                    <option value="1911">前 1</option>
                                                                    <option value="1912">1</option>
                                                                    <option value="1913">2</option>
                                                                    <option value="1914">3</option>
                                                                    <option value="1915">4</option>
                                                                    <option value="1916">5</option>
                                                                    <option value="1917">6</option>
                                                                    <option value="1918">7</option>
                                                                    <option value="1919">8</option>
                                                                    <option value="1920">9</option>
                                                                    <option value="1921">10</option>
                                                                    <option value="1922">11</option>
                                                                    <option value="1923">12</option>
                                                                    <option value="1924">13</option>
                                                                    <option value="1925">14</option>
                                                                    <option value="1926">15</option>
                                                                    <option value="1927">16</option>
                                                                    <option value="1928">17</option>
                                                                    <option value="1929">18</option>
                                                                    <option value="1930">19</option>
                                                                    <option value="1931">20</option>
                                                                    <option value="1932">21</option>
                                                                    <option value="1933">22</option>
                                                                    <option value="1934">23</option>
                                                                    <option value="1935">24</option>
                                                                    <option value="1936">25</option>
                                                                    <option value="1937">26</option>
                                                                    <option value="1938">27</option>
                                                                    <option value="1939">28</option>
                                                                    <option value="1940">29</option>
                                                                    <option value="1941">30</option>
                                                                    <option value="1942">31</option>
                                                                    <option value="1943">32</option>
                                                                    <option value="1944">33</option>
                                                                    <option value="1945">34</option>
                                                                    <option value="1946">35</option>
                                                                    <option value="1947">36</option>
                                                                    <option value="1948">37</option>
                                                                    <option value="1949">38</option>
                                                                    <option value="1950">39</option>
                                                                    <option value="1951">40</option>
                                                                    <option value="1952">41</option>
                                                                    <option value="1953">42</option>
                                                                    <option value="1954">43</option>
                                                                    <option value="1955">44</option>
                                                                    <option value="1956">45</option>
                                                                    <option value="1957">46</option>
                                                                    <option value="1958">47</option>
                                                                    <option value="1959">48</option>
                                                                    <option value="1960">49</option>
                                                                    <option value="1961">50</option>
                                                                    <option value="1962">51</option>
                                                                    <option value="1963">52</option>
                                                                    <option value="1964">53</option>
                                                                    <option value="1965">54</option>
                                                                    <option value="1966">55</option>
                                                                    <option value="1967">56</option>
                                                                    <option value="1968">57</option>
                                                                    <option value="1969">58</option>
                                                                    <option value="1970">59</option>
                                                                    <option value="1971">60</option>
                                                                    <option value="1972">61</option>
                                                                    <option value="1973">62</option>
                                                                    <option value="1974">63</option>
                                                                    <option value="1975">64</option>
                                                                    <option value="1976">65</option>
                                                                    <option value="1977">66</option>
                                                                    <option value="1978">67</option>
                                                                    <option value="1979">68</option>
                                                                    <option value="1980">69</option>
                                                                    <option value="1981">70</option>
                                                                    <option value="1982">71</option>
                                                                    <option value="1983">72</option>
                                                                    <option value="1984">73</option>
                                                                    <option value="1985">74</option>
                                                                    <option value="1986">75</option>
                                                                    <option value="1987">76</option>
                                                                    <option value="1988">77</option>
                                                                    <option value="1989">78</option>
                                                                    <option value="1990">79</option>
                                                                    <option value="1991">80</option>
                                                                    <option value="1992">81</option>
                                                                    <option value="1993">82</option>
                                                                    <option value="1994">83</option>
                                                                    <option selected="selected" value="1995">84</option>
                                                                    <option value="1996">85</option>
                                                                    <option value="1997">86</option>
                                                                    <option value="1998">87</option>
                                                                    <option value="1999">88</option>
                                                                    <option value="2000">89</option>
                                                                    <option value="2001">90</option>
                                                                    <option value="2002">91</option>
                                                                    <option value="2003">92</option>
                                                                    <option value="2004">93</option>
                                                                    <option value="2005">94</option>
                                                                    <option value="2006">95</option>
                                                                    <option value="2007">96</option>
                                                                    <option value="2008">97</option>
                                                                    <option value="2009">98</option>
                                                                    <option value="2010">99</option>
                                                                    <option value="2011">100</option>
                                                                    <option value="2012">101</option>
                                                                    <option value="2013">102</option>
                                                                    <option value="2014">103</option>
                                                                    <option value="2015">104</option>
                                                                    <option value="2016">105</option>
                                                                    <option value="2017">106</option>
                                                                    <option value="2018">107</option>
                                                                    <option value="2019">108</option>
                                                                    <option value="2020">109</option>

                                                                </select>年
										            <select name="ddlBirthMonth" onchange="javascript:setTimeout('__doPostBack(\'ddlBirthMonth\',\'\')', 0)" language="javascript" id="ddlBirthMonth" style="width:60px;">
                                                                    <option value="">請選擇</option>
                                                                    <option value="01">01</option>
                                                                    <option value="02">02</option>
                                                                    <option value="03">03</option>
                                                                    <option value="04">04</option>
                                                                    <option value="05">05</option>
                                                                    <option value="06">06</option>
                                                                    <option value="07">07</option>
                                                                    <option value="08">08</option>
                                                                    <option value="09">09</option>
                                                                    <option value="10">10</option>
                                                                    <option value="11">11</option>
                                                                    <option selected="selected" value="12">12</option>

                                                                </select>月
										            <select name="ddlBirthDay" id="ddlBirthDay" style="width:60px;">
                                                                    <option value="">請選擇</option>
                                                                    <option value="01">01</option>
                                                                    <option value="02">02</option>
                                                                    <option value="03">03</option>
                                                                    <option value="04">04</option>
                                                                    <option value="05">05</option>
                                                                    <option value="06">06</option>
                                                                    <option value="07">07</option>
                                                                    <option value="08">08</option>
                                                                    <option value="09">09</option>
                                                                    <option value="10">10</option>
                                                                    <option value="11">11</option>
                                                                    <option value="12">12</option>
                                                                    <option value="13">13</option>
                                                                    <option value="14">14</option>
                                                                    <option value="15">15</option>
                                                                    <option value="16">16</option>
                                                                    <option value="17">17</option>
                                                                    <option value="18">18</option>
                                                                    <option value="19">19</option>
                                                                    <option value="20">20</option>
                                                                    <option value="21">21</option>
                                                                    <option value="22">22</option>
                                                                    <option value="23">23</option>
                                                                    <option value="24">24</option>
                                                                    <option value="25">25</option>
                                                                    <option value="26">26</option>
                                                                    <option value="27">27</option>
                                                                    <option value="28">28</option>
                                                                    <option value="29">29</option>
                                                                    <option value="30">30</option>
                                                                    <option value="31">31</option>

                                                                </select>日
                                                </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="background-color: #f8f0e0; height: 50px;" class="style1">
                                                                <span id="Label1" style="color:Maroon;font-size:11pt;">請按照圖形所顯示的文數字輸入驗證碼:
					    <br /><font color="blue" size="2">(英文字母不用區分大小寫）</font></span>
                                                                <br />
                                                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
						<img id="imgVlid" src="ValidNumber.aspx?checkCode=NAB6AEoAYwBjAEsAcgA1AGYAbABMAGYALwAyAFMAdQBXADYAagBBADUAZwA9AD0A0" alt="圖形驗證碼" border="0" />
                                                                <input type="image" name="btnReNewNum" id="btnReNewNum" title="重新產生驗證碼" onkeypress="btnReNewNum_Click" src="Images/today.gif" alt="重新產生驗證碼" border="0" />

                                                                <font face="新細明體">

                                                                </font>
                                                            </td>
                                                            <td>&nbsp;
					    <input name="txtVerifyCode" type="text" maxlength="6" id="txtVerifyCode" onkeydown="fnTrapKD(btnOK, event);" style="width:100px;" />
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td style="background-color: #fcf9f3;" align="center" colspan="2">
                                                                <span id="ErrorMessageText" style="color:Red;"></span>
                                                                <input type="submit" name="btnOK" value="確定" onclick="myDisableButton(this);" language="javascript" id="btnOK" tabindex="1" style="color:Yellow;background-color:Teal;font-size:10pt;font-weight:bold;height:35px;width:65px;margin-top: 0px" />
                                                                <input type="submit" name="btnClear" value="清空" id="btnClear" onkeypress="btnClear_Click" style="color:Yellow;background-color:Teal;font-size:10pt;font-weight:bold;height:35px;width:65px;" /></td>
                                                        </tr>
                                                        <tr>
                                                            <td colspan="2">

                                                            </td>
                                                        </tr>
                                                    </table>

                                                </td>
                                            </tr>
                                        </table>

                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td>

                                </td>
                            </tr>
                            <tr>
                                <td align="center">

                                </td>
                            </tr>
                            <tr>
                                <td align="center">

                                </td>
                            </tr>
                        </table>

                        <script type="text/javascript">
                            function fnTrapKD(btn, event){
    var keynum;
    if(window.event) // IE
    {
                                keynum = event.keyCode
                            }
    else if(e.which) // Netscape/Firefox/Opera
    {
                                keynum = event.which
                            }
    if(keynum==13)
    {
                                event.returnValue = false;
        event.cancel = true;
        if(event.preventDefault)
        {
                                event.preventDefault();
        }
        btn.click();
        btn.focus();
    }
}
</script></form>
                </div>
            </body>
        </html>
