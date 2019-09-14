# ui 国际化步骤
1. x.ui → x.py (用pyuic)
2. x.py → x.ts (用pylupdate) `pylupdate5 file1.py file2.py -ts English.ts`
3. x.ts → x.qm (用Qt Linguist) ``