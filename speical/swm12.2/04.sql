/* 맴버쉽 서비스
1등급 고객 선물,

누적 구매액 선물

고객 테이블 - 고객 아이디, 고객 이름, 맴버쉽 등급, 고객 전화번호
책관리 테이블 - 아이디, 이름, 출판사, 가격
주문 테이블 - 아이디, 고객아이디, 책 아이디, 책 판매일

전체 기간에 대한 누적 구매액

*/

select A.user_name as "고객 아이디" ,sum(C.price) as "누적 구매액"
from  customer as A inner join orderInfo as B on A.user_id = B.buyer_id  inner join library as C on B.book_id = C.book_id
where A.membership = 1



-- group by 안하냐 ?