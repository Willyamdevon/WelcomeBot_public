from dataclasses import dataclass


@dataclass
class Config:
    TOKEN: str = "TOKEN"
    CHANNEL_ID: int = 'id_where_wil_be_massege'
    GUILD_ID: int = 'your guild_id'
