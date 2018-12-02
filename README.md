# baha_pic_crawler
### This is a python function of crawler for Baha picture
>Baha(巴哈姆特)：<https://www.gamer.com.tw/>

You can get a table like this：

| 樓層  | 推  | 噓 | 差 |
|-------|-----|-----|----|
| 樓主  | 739 | 10 | 729 |
| 6 樓  | 242 |  9 | 233 |
| 16 樓 | 441 |  0 | 441 |
| 23 樓 | 593 |  0 | 593 |

* 推 = GP(Good Point) : means how many people click like for this floor
* 噓 = BP(Bad  point) : means how many people click unlike for this floor

You can also get the hyperlink of the picture : 
>樓主
>>https://truth.bahamut.com.tw/s01/201601/f24e834da66aa649fb2b236c7b2377d1.JPG

>6 樓
>>https://truth.bahamut.com.tw/s01/201402/0d5c2e423861fb9c9de1fec8a054c3a2.JPG

>.
>.
>.

>64 樓
>>https://truth.bahamut.com.tw/s01/201601/0a869b76d7ac29416e57ca6af42e74de.JPG
>>https://truth.bahamut.com.tw/s01/201601/d49409893c4edd8b6c7de6d3d927c9d2.JPG
>>https://truth.bahamut.com.tw/s01/201601/3fabcf9445b2f044888c7f893225de8e.JPG
>>https://truth.bahamut.com.tw/s01/201601/157ce525d9687cfb1548804f28e8894c.JPG


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
