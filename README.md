# simple Cournot model

這個專案模擬了一個簡單的 Cournot 模型，這是一個用於分析公司競爭的經濟模型。

## 概述

該專案包含了Firm 以及 Cournot 兩個class。它模擬了在 Cournot 競爭假設下公司在市場上的行為。

## 安裝

   ```bash
   git clone https://github.com/aryhsg/cournot-model.git@v1.0.12
```
## 使用說明

首先必須先引入模組：
```bash
   from simple_Cournot_model.firm import Firm
   from simple_Cournot_model.cournot import Cournot
```

接著介紹 `Firm <class>` 和 `Cournot <class>`的使用方式。

在 `Firm <class>`，有兩個欄位需要輸入，分別為**q**以及**cost_func**。
```bash
   apple = Firm(q= "x", cost_func = "200+10*x")
```
其中，**q** 表示該企業成本函數方程式所欲使用的代數符號，**cost_func** 則須輸入該企業之成本函數。

而`Cournot <class>` 則須輸入兩家競爭的企業，以list方式輸入；**mkt_demand_func** 則須輸入兩企業共同面對的市場需求函數，以字串形式輸入。    

```bash
   cournot = Cournot(firm: list, mkt_demand_func: str)
```

在`Cournot <class>` 中，設置了幾個`method`，分別為`.profit()`，`.reaction_func()`，`.equilibrium()`以及`.figure()`。

在使用上必須依照此順序進行操作，先以`.profit()`求得雙方的利潤函數，再用`.reaction_func()`透過一階微分得出反應函數，最後透過`.equilibrium()`將反應函數聯立求出均衡解，並以`.figure()`呈現出交點。


