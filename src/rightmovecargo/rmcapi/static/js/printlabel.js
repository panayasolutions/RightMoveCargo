function printlabel()
{
    var fontname = "Libre Barcode 39";
    var prtcnt = "<html>";
    prtcnt += "<head> <meta charset='UTF-8'>";
    prtcnt += "<link href='https://fonts.googleapis.com/css?family=Libre+Barcode+39' rel='stylesheet'> </head>";
    prtcnt += "<body onload=&#34window.print()&#34><p> 54132122</p><p style=font-family:&#34Libre&#32Barcode&#32&#51&#57&#34;>*54132122*</p></body></html>";
    /*var WinPrint = window.open(",",left=50,top=50,width=400,height=300);
    WinPrint.document.write(prtcnt);
    WinPrint.document.close();
    WinPrint.focus();
    window.stop();
    WinPrint.print();
    WinPrint.close();*/
}