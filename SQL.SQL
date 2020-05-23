-- 코드를 입력하세요
SELECT A.ID USER_ID,COUNT(*) PURCHASE_COUNT, SUM(C.PRICE) TOTAL_PRICE
FROM (GAME_USERS A INNER JOIN PURCHASES B ON A.ID = B.USER_ID) INNER JOIN CHARACTERS C ON B.ITEM = C.NAME
GROUP BY A.ID
ORDER BY A.ID



-- 코드를 입력하세요
SELECT A.ID USER_ID,COUNT(*) PURCHASE_COUNT, IFNULL(SUM(C.PRICE),0) TOTAL_PRICE
FROM GAME_USERS A LEFT JOIN (PURCHASES P LEFT JOIN CHARACTERS C ON P.ITEM = C.NAME  ) ON A.ID = P.USER_ID
GROUP BY A.ID
ORDER BY A.ID

```
USER_ID	PURCHASE_COUNT	TOTAL_PRICE
aboriginalvader565	1	10000
adorableblue1813	1	1000
ayrmogul500	1	0
baffledchoose600	1	0
barracudafried1489	2	11000
bipedalcapillary1194	1	1000
bizarrehaltwhistle943	1	0
boiledemral1149	1	0
capstanzesty1464	1	2000
chamaeleonbullhorn1467	1	0
chongqingricochet889	1	2000
clippergaiters399	1	0
closehelm996	1	0
cloutedneuroma1915	1	1000
clwydiankorean1876	1	0
consideredrubidium1202	1	2000
crestrumble1879	1	10000
cronzbloviate1050	1	10000
curryartle678	1	0
daysglossy1776	1	10000
dineronoodle1236	1	0
discoveredcur1700	1	1000
dreamscustom1880	1	10000
evilrasp332	1	0
fadewaterloo552	1	0
formflat1915	1	0
fraysplink94	1	10000
frenchchampagne1501	1	1000
fundagesugarcane817	2	11000
galettemarine1254	1	2000
globulargranted1285	1	10000
greekfiona1630	1	1000
guccifounder457	1	1000
hairtennis1628	1	1000
hastinesshaggis1056	1	10000
henryrickety929	1	0
hideousheadphones1123	1	1000
hindwellphineas489	1	0
idahojealous1863	1	0
injectidiopathic1475	1	0
intestinetrigger1644	1	0
inventorymeta1544	1	0
langworthychance1887	1	1000
lomojubilee1357	1	0
mahjongsooty678	1	10000
malvernroasting1960	1	10000
mastmilo1852	1	0
micatingley1806	1	1000
naneekgunpowder1886	1	1000
noisytransfer1742	1	0
nonstopwindlass1768	2	12000
northumberlandcord1903	1	1000
paltryquintic295	1	0
popbanker158	1	0
processornoe1303	1	1000
providencechant1561	1	0
rapadashpallas1529	1	1000
removeimpolite422	1	1000
rhapsodydusky1531	1	0
roscoebridled453	1	10000
savesnarl1250	1	10000
savoryjoomla915	1	10000
shademanhole1508	1	0
siemensplayoffs768	1	10000
skimmedfastidious248	1	1000
slalomrabai1391	1	2000
slingingviolin1916	1	1000
solidwillow917	1	0
solubleusd1278	2	3000
sometimeschoc231	1	10000
speakingcrunchy1324	1	1000
stopperwallabyies1535	1	0
stovemoth586	1	0
sturcombethus152	1	0
toucanmoaning1646	1	0
triumphfox488	1	1000
tumbleglenmore1028	1	10000
untrueshira1333	1	0
vegetableshannon1838	1	2000
widespreadkeyboard1906	1	10000
```

-- 코드를 입력하세요
SELECT *
FROM GAME_USERS A LEFT JOIN (PURCHASES P LEFT JOIN CHARACTERS C ON P.ITEM = C.NAME  ) ON A.ID = P.USER_ID
ORDER BY A.ID

-- 코드를 입력하세요
SELECT *
FROM (PURCHASES P LEFT JOIN CHARACTERS C ON P.ITEM = C.NAME  )

