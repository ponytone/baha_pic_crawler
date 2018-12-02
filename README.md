# baha_pic_crawler
#### This is a python function of crawler for Baha picture
>Baha(巴哈姆特)：<https://www.gamer.com.tw/>

You can get a table like this：
| 樓層  | 推  | 噓 | 差 |
| :---  |:-- :|:--:| ---:|
| 樓主  | 739 | 10 | 729 |
| 6 樓  | 242 |  9 | 233 |
| 16 樓 | 441 |  0 | 441 |
| 23 樓 | 593 |  0 | 593 |

| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ |:---------------:| -----:|
| col 3 is      | some wordy text | $1600 |
| col 2 is      | centered        |   $12 |
| zebra stripes | are neat        |    $1 |
| test | 測試        |    $3333 |

## First : Check out for the packages
* requests 
* re  
* BeautifulSoup 
* pandas 
* numpy 
## Second : select a class
* For example ： [場外休憩區](https://forum.gamer.com.tw/A.php?bsn=60076)
## Third : select a topic
* For example : <https://forum.gamer.com.tw/C.php?page=1&bsn=60076&snA=3144471&locked=F&gothis=54827297#54827297>
## Function *baha_picture(url,page_number,gp_number)*
* page_number = How many pages you want to get
* gp_number = the filter of (Gp - Bp)
## Demo
* You can try Demo for more details
