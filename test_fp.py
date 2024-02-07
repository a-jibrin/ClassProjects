import pytest
import json
from unittest.mock import patch
from final import Student

@pytest.fixture
def test_student(tmpdir):  # temporary directory for user's Canvas login 
    data_file_path = tmpdir.join("test_data_file.json")
    student = Student("test_user", "test_password", str(data_file_path))
    return student

def test_log_in(test_student):
    sample_user_data = {
        "test_user": {
            "password": "test_password",
            "profile": {"name": "Test User", "dob": "01/015", "preferences": "Test Preferences"},
            "academic_calendar": [],
            "grade_tracker": {"gpa": 0.0, "academic_goals": ""},
            "task_manager": {"tasks": [], "errands": []},
            "event_calendar": {"gym_efforts": [], "meeting": [], "other": []},
            "financial_management": {"budgets": {"weekly": 0.0, "monthly": 0.0}, "expenses": []},
        }
    }

    # Save sample user data to temporary file
    with open(test_student.data_file, "w") as file:
        json.dump(sample_user_data, file)

    # Mock user input for the log_in process
    with patch("builtins.input", side_effect=["test_user", "test_password"]):
        test_student.log_in()

    # Assert that user's data has been logged correctly
    assert test_student.username == "test_user"
    assert test_student.password == "test_password"
    assert test_student.profile == {"name": "Test User", "dob": "01/15", "preferences": "Test Preferences"}
    assert test_student.academic_calendar == []
    assert test_student.grade_tracker == {"gpa": 0.0, "academic_goals": ""}
    assert test_student.task_manager == {"tasks": [], "errands": []}
    assert test_student.event_calendar == {"gym_efforts": [], "meeting": [], "other": []}
    assert test_student.financial_management == {"budgets": {"weekly": 0.0, "monthly": 0.0}, "expenses": []}



