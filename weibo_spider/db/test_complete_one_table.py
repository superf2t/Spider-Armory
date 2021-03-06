from peewee import *
from datetime import datetime
"""
获取转发的原始html,没有经过任何处理
"""
# db = SqliteDatabase('complete_parse_res.sqlite')
mysql_db = MySQLDatabase('wuhan',
                          user='root',
                          password='',
                          host='localhost',
                          charset='utf8mb4')
mysql_db.connect()


class BaseModel(Model):
    class Meta:
        database = mysql_db
        # database = db


class Test_Complete_Weibo(BaseModel):
    id = BigIntegerField(null=False, primary_key=True, verbose_name='如果是原微博直接用mid做主键，如果不是，则用生成路径hash过后做主键')
    current_page = IntegerField(null=True, verbose_name='当前页数')
    mid_id = BigIntegerField(null=True, verbose_name='评论mid')
    repost_html = TextField(null=True, verbose_name='单条评论的raw_html')
    repost_user_id = BigIntegerField(null=True, verbose_name='评论的用户id')
    repost_user = CharField(null=True, verbose_name='评论用户名')
    repost_content = TextField(null=True, verbose_name='单条评论内容')
    repost_time = CharField(null=True, verbose_name='评论时间')
    repost_num = IntegerField(null=True, verbose_name='转发数')
    upvote_num = IntegerField(null=True, verbose_name='点赞数')

    repost_path = TextField(null=True, verbose_name='转发消息的层次关系:mid->mid->mid')
    is_crawl = BooleanField(null=False, verbose_name='页面是否已经爬过了')
    is_origin = BooleanField(null=False, verbose_name='是否是原微博')

    matrix = BigIntegerField(null=True, verbose_name='经过转发的微博的宿主微博')
    depth = IntegerField(null=True, verbose_name='转发深度')

    created_time = DateTimeField(default=datetime.now, verbose_name='创建时间')


if __name__ == '__main__':
    Test_Complete_Weibo.create_table()

