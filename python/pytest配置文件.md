
pytest.ini 文件是配置和自定义 pytest 的一种方式。pytest 是一个用于 Python 的测试框架，pytest.ini 文件允许你为测试运行配置各种选项和参数。

# 配置选项：
你可以在 pytest.ini 文件中设置各种配置选项，如默认测试目录、忽略的测试文件、输出格式等。例如：
[pytest]
addopts = -v --maxfail=3
testpaths = tests

# 标记管理：
你可以在 pytest.ini 文件中定义和管理自定义标记，以便在测试中使用。例如：
[pytest]
markers =
    smoke: marks tests as smoke tests
    regression: marks tests as regression tests
    api: marks tests as API tests
    
    
# 使用标记
import pytest

@pytest.mark.smoke
def test_smoke():
    assert 1 + 1 == 2

@pytest.mark.regression
def test_regression():
    assert 2 * 2 == 4

@pytest.mark.api
def test_api():
    assert "hello".upper() == "HELLO"

失败重新运行
安装 pytest-rerunfailures 插件
1。pip install pytest-rerunfailures

配置 pytest.ini 文件：
[pytest]
addopts = --reruns 3 --reruns-delay 2

import pytest


在测试中使用：你可以在测试函数中直接应用重运行装饰器，如果你希望某些特定的测试有不同的重运行次数：
@pytest.mark.flaky(reruns=5, reruns_delay=1)
def test_example():
    assert 1 == 2
