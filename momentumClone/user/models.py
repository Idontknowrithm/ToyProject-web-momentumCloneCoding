from django.db import models

class User(models.Model):
    objects = models.Manager()
    userid = models.CharField(max_length = 64,
                              verbose_name = '아이디')
    username = models.CharField(max_length = 64, 
                                verbose_name = '이름')
    useremail = models.EmailField(max_length = 128, 
                                  verbose_name = '이메일')
    password = models.CharField(max_length = 64, 
                                verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add = True, verbose_name = '등록 시간')


    class Meta:
        db_table = 'users'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

def __str__(self):
    return self.username