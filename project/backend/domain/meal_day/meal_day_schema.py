from datetime import datetime,date
from typing import Optional, List

from pydantic import BaseModel

class MealDay_schema(BaseModel):
    id: int
    user_id: int
    water: float
    coffee: float
    alcohol: float
    carb: float
    protein: float
    fat: float
    cheating: int
    goalcalorie: float
    nowcalorie: float
    gb_carb: Optional[str] = None
    gb_protein: Optional[str] = None
    gb_fat: Optional[str] = None
    date: date
    track_id: Optional[int]

class MealDay_cheating_get_schema(BaseModel):
    cheating: int

class MealDay_wca_get_schema(BaseModel):
    water:float
    coffee: float
    alcohol: float

class Mealday_wca_update_schema(BaseModel): ##물, 커피, 알코올
    water: float
    coffee: float
    alcohol: float

class MealDay_calorie_get_schema(BaseModel): ## 목표, 현재 칼로리
    goalcalorie: float
    nowcalorie: float


class MealDay_track_hour_schema(BaseModel):
    name: Optional[str] = None
    calorie: Optional[float] = None
    date: Optional[datetime] =None
    heart: Optional[float] = None
    picture: Optional[str] = None
    track_goal: Optional[bool] =None

class MealDay_track_today_schema(BaseModel):
    mealday: List[MealDay_track_hour_schema]

class MealDay_track_dday_goal_real_schema(BaseModel):
    dday: int
    goal: List[str]
    real: List[str]