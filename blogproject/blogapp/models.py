from django.db import models

class BlogPost(models.Model):
    #モデルクラス
    #カテゴリに関する項目を入れ子のタプルとして定義
    #タプルの第一要素はモデルが使用する値
    #第二要素は管理サイトの選択メニューに表示する文字列
    CATEGORY = (('fashion', 'fashion')),(('dailylife','dailylife')),(('sports','sports'))

    #タイトル用のフィールド
    title = models.CharField(verbose_name='title',max_length=200)

    #本文用のフィールド
    content = models.TextField(verbose_name='contnet')

    #投稿日時のフィールド
    posted_at = models.DateTimeField(verbose_name='datetime',auto_now_add=True)

    #カテゴリのフィールド
    category = models.CharField(verbose_name='category',max_length=50,choices=CATEGORY)

    def __str__(self):
        return self.title
