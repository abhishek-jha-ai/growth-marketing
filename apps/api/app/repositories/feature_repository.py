from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from apps.api.app.schemas.app_schema import FeatureCreate, FeatureUpdate
from apps.api.app.models.feature_model import Feature

class FeatureRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get(self, feature_id: int) -> Optional[Feature]:
        result = await self.session.execute(select(Feature).where(Feature.id == feature_id))
        return result.scalars().first()

    async def list(self) -> List[Feature]:
        result = await self.session.execute(select(Feature))
        return result.scalars().all()

    async def create(self, feature_create: FeatureCreate) -> Feature:
        feature = Feature(**feature_create.dict())
        self.session.add(feature)
        await self.session.commit()
        await self.session.refresh(feature)
        return feature

    async def update(self, feature_id: int, feature_update: FeatureUpdate) -> Optional[Feature]:
        feature = await self.get(feature_id)
        if not feature:
            return None
        for key, value in feature_update.dict(exclude_unset=True).items():
            setattr(feature, key, value)
        self.session.add(feature)
        await self.session.commit()
        await self.session.refresh(feature)
        return feature

    async def delete(self, feature_id: int) -> bool:
        feature = await self.get(feature_id)
        if not feature:
            return False
        await self.session.delete(feature)
        await self.session.commit()
        return True
