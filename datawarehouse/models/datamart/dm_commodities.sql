with commodities as (
    select * from {{ ref('stg_commodities') }}
),

commodity_movements as (
    select * from {{ ref('stg_commodities_movements') }}
),

joined as (
    select
        c.trade_date,  
        c.symbol_commodity,
        c.closing_value,
        m.action_type,
        m.quantity_traded,
        (m.quantity_traded * c.closing_value) as value,
        case
            when m.action_type = 'sell' then (m.quantity_traded * c.closing_value)
            else -(m.quantity_traded * c.closing_value)
        end as gain
    from commodities c
    join commodity_movements m on c.symbol_commodity = m.symbol_commodity
)
select * from joined