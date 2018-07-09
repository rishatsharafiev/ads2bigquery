[
    {
        "name": "id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "account_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "budget_rebalance_flag",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "buying_type",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "can_create_brand_lift_study",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "can_use_spend_cap",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
    },
    {
        "name": "configured_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "created_time",
        "type": "DATETIME",
        "mode": "NULLABLE"
    },
    {
        "name": "effective_status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "objective",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "source_campaign",
        "type": "RECORD",
        "fields": [
            {
                "name": "id",
                "type": "INTEGER"
            }
        ]
    },
    {
        "name": "source_campaign_id",
        "type": "INTEGER",
        "mode": "NULLABLE"
    },
    {
        "name": "start_time",
        "type": "DATETIME",
        "mode": "NULLABLE"
    },
    {
        "name": "status",
        "type": "STRING",
        "mode": "NULLABLE"
    },
    {
        "name": "updated_time",
        "type": "DATETIME",
        "mode": "NULLABLE"
    }
]
