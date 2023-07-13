# 输入以下代码创建一些基础的学生信息

```bash
python manage.py migrate
python manage.py shell
```

然后在python shell中输入

```python
from menu.models import *
Student(1,"Tom",100,"活泼的小男孩，成绩差了点","物理","男","18","初中生",1,"Tom@hotmail.com",'Chicaco','初中').save()
Student(2,"Yuan",250,"神一般的男生，啥都好","高数","男","19","大学生",2,"3447372030@qq.com",'苏州大学','大学').save()
```