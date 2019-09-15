# ui 国际化步骤
1. x.ui → x.py (用pyuic)
2. x.py → x.ts (用pylupdate) `pylupdate5 file1.py file2.py -ts English.ts`
3. x.ts → x.qm (用Qt Linguist) `lrelease`
4. 将.qm文件以及其他资源(如图标)嵌入到Python模块中(用Qt pyrcc5) `pyrcc5`

> 因为pyqt5国际化对继承的类支持不是很好，所以需要把生成的ts文件中的MainWinBase改为MainWin
