from PyQt5.QtGui import *

def createlabel():
    textdata = "*500098254884*"

    fid = QFontDatabase.addApplicationFont('../static/fonts/3of9/3OF9_NEW.TTF')
    family = QFontDatabase.applicationFontFamilies(fid)
    print(family)
    fnt = QFont(family[0], pointSize=36)
    fnt1 = QFont('Times', pointSize=20)

    tdoc = QTextDocument(textdata+"\n"+textdata)
    tblk = tdoc.begin()
    print(tblk.text())
    tf = tblk.iterator.fragment()
    tf.charFormat().setFont(fnt)

    tf2 = tblk.next().iterator.fragment()
    tf2.charFormat().setFont(fnt1)
    return tdoc