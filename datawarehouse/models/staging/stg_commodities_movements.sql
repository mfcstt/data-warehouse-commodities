with source as (
    select
        *
    from
        {{ source('postgres', 'commodity_movements') }}
),

rename_columns as (
    select
        cast(date as date) as date_mov,
        symbol as symbol_commodity,
        action as action_type,
        quantity as quantity_traded
    from
        source
)

select * from rename_columns