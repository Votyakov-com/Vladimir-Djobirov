import datetime
from task_1 import Task, TaskList
import pytest


@pytest.fixture
def sample_task():
    return Task("[Описание]")


@pytest.fixture
def task_list():
    return TaskList()


@pytest.fixture
def sample_task_1():
    return Task("[Описание]", 1)


@pytest.fixture
def sample_task_2():
    return Task("[Описание]", 2)


def test_task_initialization(sample_task):
    assert sample_task.priority == 1
    assert sample_task.deadline is None
    assert not sample_task.is_completed


def test_mark_completed(sample_task):
    sample_task.mark_completed()
    assert sample_task.is_completed


def test_set_deadline(sample_task):
    deadline = datetime.datetime(2023, 11, 25)
    sample_task.set_deadline(deadline)
    assert sample_task.deadline == deadline


def test_task_string_representation(sample_task):
    assert str(sample_task) == 'Description: [Описание]\nPriority: 1\nStatus: Not Completed\nNo Deadline\n'


def test_tasklist_initialization(task_list):
    assert len(task_list.tasks) == 0


def test_add_task(task_list, sample_task):
    task_list.add_task(sample_task)
    assert len(task_list.tasks) == 1
    assert sample_task in task_list.tasks


def test_remove_task(task_list, sample_task):
    task_list.add_task(sample_task)
    initial_task_count = len(task_list.tasks)
    task_list.remove_task(sample_task)
    final_task_count = len(task_list.tasks)
    assert final_task_count == initial_task_count - 1
    assert sample_task not in task_list.tasks


def test_sort_by_priority(task_list, sample_task_1, sample_task_2):
    task_list.add_task(sample_task_1)
    task_list.add_task(sample_task_2)
    task_list.sort_by_priority()
    assert task_list.tasks[0].priority > task_list.tasks[1].priority


def test_filter_by_status(task_list, sample_task_1, sample_task_2):
    sample_task_2.mark_completed()
    task_list.add_task(sample_task_1)
    task_list.add_task(sample_task_2)
    result_list = task_list.filter_by_status(True)
    assert len(result_list) == 1
    assert result_list[0].is_completed
