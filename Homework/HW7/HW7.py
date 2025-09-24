
import requests


base_url = 'http://5.101.50.27:8000'

"""
Разработать автоматические тесты,
которые проверяют корректность работы API для управления сотрудниками.
Создайте класс EmployeeApi для создания вспомогательных методов.
API Методы
"""

# 1. Создание нового работника
# ● Метод: POST
# ● URL http://5.101.50.27:8000/employee/create
# ● Описание: Создаёт нового сотрудника, принимает данные в JSON.


def test_create_employee():
    """Проверка: создание нового сотрудника"""

    employee = {
        "first_name": "John",
        "last_name": "Doe",
        "middle_name": "Edward",
        "company_id": 1,
        "email": "johndoe@example.com",
        "phone": "+1234567890",
        "birthdate": "1990-01-15",
        "is_active": True
    }

    resp = requests.post(base_url + '/employee/create', json=employee)

    # Проверка кода ответа (API возвращает 200, а не 201)
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"

    data = resp.json()

    # Проверяем, что поля совпадают с тем, что отправили
    for key in employee:
        assert data[key] == employee[key], f"Mismatch in field '{key}'"



# 2. Получение информации о работнике
# ● Метод: GET
# ● URL http://5.101.50.27:8000/employee/info
# ● Описание: Получает данные о сотруднике по его ID.

def test_get_employee_info():
    """Проверка: получение списка сотрудников по ID компании"""

    company_id = 1  # ID компании, а не сотрудника!

    resp = requests.get(f"{base_url}/employee/list/{company_id}")

    # Проверка кода ответа
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"

    data = resp.json()
    assert isinstance(data, list), "Response should be a list"
    assert len(data) > 0, "Employee list should not be empty"

    # Проверяем наличие ключей у первого сотрудника
    expected_keys = {
        "first_name", "last_name", "middle_name",
        "company_id", "email", "phone",
        "birthdate", "is_active"
    }

    assert expected_keys.issubset(data[0].keys()), (
        f"Missing keys in employee: {set(expected_keys) - set(data[0].keys())}"
    )

# 3. Изменение данных о работнике
# ● Метод: PATCH
# ● URL http://5.101.50.27:8000/employee/change
# ● Описание: Позволяет изменить информацию о сотруднике по его ID


def test_update_employee():
    """Проверка: изменение данных сотрудника по ID"""

    employee_id = 1        # должен существовать в базе  (не знаю что сюда ставить )
    client_token = "test"  # нужно подставить реальный токен, если API требует авторизации

    update_data = {
        "last_name": "UpdatedLastName",
        "email": "updated@example.com",
        "phone": "+79998887766",
        "is_active": False
    }

    resp = requests.patch(
        f"{base_url}/employee/change/{employee_id}?client_token={client_token}",
        json=update_data
    )

    # Проверка кода ответа
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"

    data = resp.json()

    # Проверяем, что обновлённые поля применились
    assert data["last_name"] == update_data["last_name"]
    assert data["email"] == update_data["email"]
    assert data["phone"] == update_data["phone"]
    assert data["is_active"] == update_data["is_active"]