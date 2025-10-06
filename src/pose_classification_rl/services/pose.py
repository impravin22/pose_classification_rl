from __future__ import annotations

import logging
from typing import Any, Dict

logger = logging.getLogger(__name__)


class PoseService:
    """Domain service for Pose classification with RL."""

    def __init__(self, model_name: str = "dummy") -> None:
        self.model_name = model_name

    async def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        logger.info("running pose service", extra={"keys": list(payload.keys())})
        return {"ok": True, "model": self.model_name, "received": list(payload.keys())}
