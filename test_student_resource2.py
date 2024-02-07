import pytest
import json
from unittest.mock import patch
from final import Student

@pytest.fixture
def test_student(tmpdir):  # Use a temporary directory for data file
    data_file_path = tmpdir.join("test_data_file.json")
    student = Student("test_user", "test_password", str(data_file_path))
    return student

def test_update_academic_calendar(test_student):
    # Mock user input in update_academic_calendar
    with patch("builtins.input", side_effect=["2", "Math 101", "01-15-23"]):
        test_student.update_academic_calendar()

    # Assert that academic calendar has been updated correctly
    assert test_student.academic_calendar == [{"course": "Math 101", "deadline": "01-15-23"}]

def test_update_grade_tracker(test_student):
    # Mock user input in update_grade_tracker process
    with patch("builtins.input", side_effect=["3.5", "Study hard"]):
        test_student.update_grade_tracker()

    # Assert that grade tracker has been updated correctly
    assert test_student.grade_tracker == {"gpa": 3.5, "academic_goals": "Study hard"}

def test_update_task_manager(test_student):
    # Mock user input in update_task_manager process
    with patch("builtins.input", side_effect=["Study for exam", "Grocery shopping"]):
        test_student.update_task_manager()

    # Assert that task manager has been updated correctly
    assert test_student.task_manager == {
        "tasks": [{"task": "Study for exam", "completed": False}],
        "errands": [{"errand": "Grocery shopping", "completed": False}],
    }

def test_update_event_calendar(test_student):
    # Mock user input in update_event_calendar process
    with patch("builtins.input", side_effect=["Leg day", "Code club meeting", "Birthday party"]):
        test_student.update_event_calendar()

    # Assert that event calendar has been updated correctly
    assert test_student.event_calendar == {
        "gym_efforts": ["Leg day"],
        "meeting": ["Code club meeting"],
        "other": ["Birthday party"],
    }

def test_update_financial_management(test_student):
    # Mock user input during update_financial_management process
    with patch("builtins.input", side_effect=["100", "200", "Books", "50"]):
        test_student.update_financial_management()

    # Assert that financial management has been updated correctly
    assert test_student.financial_management == {
        "budgets": {"weekly": 100.0, "monthly": 200.0},
        "expenses": [{"item": "Books", "price": 50.0}],
    }
