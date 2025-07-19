# fsm_states/survey_states.py

from aiogram.fsm.state import State, StatesGroup

class UserSurvey(StatesGroup):
    """
    Класс состояний для проведения опроса пользователя.
    Хранит состояния для каждого шага опроса.
    """
    # Шаг 1: Ожидание имени пользователя
    waiting_for_name = State()
    
    # Шаг 2: Ожидание возраста пользователя
    waiting_for_age = State()
    
    # Шаг 3: Ожидание подтверждения
    waiting_for_confirmation = State()
