from datetime import date
from domain.track_routine import track_routine_schema
from domain.group import group_crud
from models import TrackRoutine
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from fastapi import HTTPException

def get_TrackRoutine_by_track_id(db: Session, track_id:int):
    trackroutines = db.query(TrackRoutine).filter(
        TrackRoutine.track_id==track_id
    ).first()
    return trackroutines

#def get_Suggestion_title_all(db: Session, user_id: int):
 #   suggestions = db.query(suggestion.id,suggestion.title).filter(
 #       suggestion.user_id == user_id
 #  ).all()
 #   return [Suggestion_title_schema(id=suggest.id, title=suggest.title) for suggest in suggestions]


def create(db: Session, track_id: int,
           routine_create: track_routine_schema.TrackRoutineCreate):
    db_routine = TrackRoutine(
        track_id=track_id,
        time=routine_create.time,
        title=routine_create.title,
        calorie=routine_create.calorie,
        food=routine_create.food,
        week=routine_create.week,
        repeat=routine_create.repeat,
    )
    db.add(db_routine)
    db.commit()
    db.refresh(db_routine)
    return db_routine


def delete_all(db, track_id):
    routines = db.query(TrackRoutine).filter(TrackRoutine.track_id==track_id).all()
    for routine in routines:
        db.delete(routine)
        db.commit()
        db.refresh(routine)

#############################################

def get_TrackRoutine_bytrack_id(db: Session, track_id:int):
    trackroutines = db.query(TrackRoutine).filter(
        TrackRoutine.track_id==track_id
    ).all()
    return trackroutines

def get_goal_caloire_bydate_using_trackroutine(db: Session, days: int ,track_id: int, date: date)->float:
    ## 당일 칼로리 계산
    # 요일을 정수로 얻기 (월요일=0, 일요일=6)
    weekday_number = date.weekday()
    # 요일을 한글로 얻기 (월요일=0, 일요일=6)
    weekday_str = ["월", "화", "수", "목", "금", "토", "일"][weekday_number]
    day = str(days)
    results = db.query(TrackRoutine.time, TrackRoutine.calorie).filter(
        and_(
            TrackRoutine.track_id == track_id,
            or_(
                TrackRoutine.week.like(f"%{weekday_str}%"),
                TrackRoutine.date.like(f"%{day}%"),
            )
        )
    ).all()
    calorie = 0.0
    for result in results:
        count=result.count(',')
        calorie += (count * result.calorie)
    return calorie

def get_calorie_average(track_id: int, db: Session):
    routines = db.query(TrackRoutine).filter(TrackRoutine.track_id==track_id).all()

    sum = 0
    for routine in routines:
        sum += routine.calorie

    return sum / len(routines)