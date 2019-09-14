# ui 国际化步骤
1. x.ui → x.py (用pyuic)
2. x.py → x.ts (用pylupdate) `pylupdate5 file1.py file2.py -ts English.ts`
3. x.ts → x.qm (用Qt Linguist) `lrelease`

> 发布管理可以选择使用pyrcc5将.qm 文件以及其他应用程序资源（如图标）嵌入到Python模块中。