-- 판매중이지 않은데, 판매된 기록
-- 서점이 닫혔는데, 고객이 도서를 구매한 기록
-- library
-- orderInfo
select B.buyer_id,
    B.buy_date,
    A.book_name,
    A.price
from library as A
    inner join orderInfo as B on A.book_id = B.book_id
where (A.book_name like "Looking with Elice")
    or (
        B.buy_date >= "2020-07-27"
        and B.buy_date <= "2020-07-31"
    )
order by B.buy_date