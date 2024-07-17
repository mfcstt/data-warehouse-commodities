with source as (
    select
        *
    from
        {{ source('postgres', 'commodities') }}
),

rename_columns as (
    select
        cast("Date" as date) as trade_date, 
        "Close" as closing_value,
        symbol as symbol_commodity     
    from
        source
)

select * from rename_columns