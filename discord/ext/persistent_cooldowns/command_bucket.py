from dataclasses import dataclass, field


@dataclass(frozen=True)
class CommandBucket:
    command_name: str
    cache: dict = field(default_factory=dict)
    cooldown_rate: int = None
    cooldown_per: int = None
    window
