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


Teacher(1,"大原老师",300,"神一般的老师，啥都好","高数","男","硕士",3,"3447372030@qq.com",1254646845624,13345465455,"曾获得奥林匹克数学竞赛金牌，教育出众多优秀才子").save()
Teacher(2,"大段老师",400,"神一般的老师，啥都好","物理","男","博士",4,"4543644@qq.com",454564454545,245454545,"曾获得国家物理竞赛一等奖").save()
```

