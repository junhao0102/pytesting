# 測試斷言方法

在進行單元測試時，你可以使用以下幾種斷言方法來確保你的代碼按預期工作：

- **assertEqual**
  - 描述：檢查兩個值是否相等。如果不相等，則測試失敗。
  - 例子：`assertEqual(result, 42)`

- **assertNotEqual**
  - 描述：檢查兩個值是否不相等。如果相等，則測試失敗。
  - 例子：`assertNotEqual(result, 42)`

- **assertTrue**
  - 描述：檢查一個值是否為 True。如果不是，則測試失敗。
  - 例子：`assertTrue(is_valid)`

- **assertFalse**
  - 描述：檢查一個值是否為 False。如果不是，則測試失敗。
  - 例子：`assertFalse(is_valid)`

- **assertIs**
  - 描述：檢查兩個值是否是同一個對象。如果不是，則測試失敗。
  - 例子：`assertIs(var1, var2)`

- **assertIsNot**
  - 描述：檢查兩個值是否不是同一個對象。如果是，則測試失敗。
  - 例子：`assertIsNot(var1, var2)`

- **assertIn**
  - 描述：檢查一個值是否包含在另一個值中。如果不是，則測試失敗。
  - 例子：`assertIn(item, list)`

- **assertNotIn**
  - 描述：檢查一個值是否不包含在另一個值中。如果是，則測試失敗。
  - 例子：`assertNotIn(item, list)`

- **assertRaises**
  - 描述：檢查一個函數是否會引發異常。如果不會，則測試失敗。
  - 例子： 
  ```python
    with self.assertRaises(ValueError):
        raise ValueError("Invalid value")
    ```




## allure
```bash
allure serve report
