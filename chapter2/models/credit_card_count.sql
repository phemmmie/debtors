-- credit_card_count: Breakdown of the count of fares paid by credit card.

{{ config(materialized='table') }}

select payment, count(*) as count
from {{ ref('taxi_trips') }}
where payment = 'credit card'
group by payment
