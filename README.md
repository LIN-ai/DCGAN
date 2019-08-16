# DCGAN
參考影片：https://www.youtube.com/watch?v=thr7KldvpPw

參考github：https://github.com/DLangerr/dcgan-mnist-tensorflow 

錯誤

1. No module named 'matplotlib'

解決方法(測試)：安裝matplotlib

參考：(Anaconda中ImportError: No module named 'matplotlib' 问题的解决) https://blog.csdn.net/yangzijiang666/article/details/79695938

解決步驟：

1.	開啟Anaconda Navigator
2.	選擇所在環境
3.	在installed中查找是否安装了matplotlib，如果没有找到，就切换到Not installed，將其安装上，確定安裝成功。

展示：
![img](https://github.com/LIN-ai/DCGAN/blob/master/dcgan00.png?raw=true)

![img](https://github.com/LIN-ai/DCGAN/blob/master/dcgan01.png?raw=true)

![img](https://github.com/LIN-ai/DCGAN/blob/master/dcgan02.png?raw=true)

結論：由於最後訓練出來的檔案，除了第一張圖片略有雛形，從第二章開始基本上便成了純色塊，在訓練了十五張後，一直沒有改善，暫時認定為參數設定有問題，本次訓練失敗。

DCGAN修正測試：

修改epochs的數值，由原本參考程式碼的5000更改為1000，發現這次圖片有出來，可是，訓練出來的圖片合成差不多2~3張就會跳出來。

展示：
![img](https://github.com/LIN-ai/DCGAN/blob/master/dcgan03.png?raw=true)

