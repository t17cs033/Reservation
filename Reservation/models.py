from django.db import models
import datetime as dt
from django.core.validators import MaxValueValidator,MinValueValidator
from django.template.defaultfilters import default
# Create your models here.

def get_next():
    try:
        return Member.objects.latest('cmpId').cmpId + 1
    except Member.DoesNotExist:
        return 1

class Billing(models.Model):
    cmpId = models.IntegerField(default = get_next)               #ID
    bill = models.CharField(max_length = 50, default = '0')     #支払金額
    def __str__(self):
        return str(self.cmpId)


class Member(models.Model):
    cmpId = models.IntegerField(default = get_next)               #ID
    cmpName = models.CharField(max_length = 50) #企業名
    address = models.CharField(max_length = 50) #住所
    tel = models.CharField(max_length = 50)     #電話番号
    section = models.CharField(max_length = 50) #担当部署
    name = models.CharField(max_length = 50)    #担当者名
    mail = models.CharField(max_length = 50)    #メールアドレス
    pay = models.ForeignKey(Billing,on_delete=models.CASCADE)     #支払金額

    def __str__(self):
        return self.cmpName

class Reserve(models.Model):
    cmpId = models.IntegerField('企業')                   #ID
    date = models.DateField('日付', blank=False,null=False) #日付
    start_time = models.TimeField('開始時間',
                                  default=dt.time(9,0))                 #利用開始時間
    end_time = models.TimeField('終了時間',
                                default=dt.time(10,0))                   #利用終了時間
    mrName = models.CharField('会議室名', max_length = 50)      #会議室名
    whiteboard = models.IntegerField('ホワイトボード', default = 0,
                validators=[MinValueValidator(0),
                            MaxValueValidator(10)]) #ホワイトボード
    projector = models.IntegerField('プロジェクター', default = 0,
                validators=[MinValueValidator(0),
                            MaxValueValidator(5)])  #プロジェクター
    charge = models.IntegerField()      #料金
    def __str__(self):
        return str(self.cmpId)

class MeetingRoom(models.Model):
    mrName= models.CharField(max_length = 50)       #会議室名
    #avail = models.IntegerField()                   #空き数
    timeCharge = models.CharField(max_length = 50)  #時間貸し料金
    halfCharge = models.CharField(max_length = 50)  #半日貸し料金
    dayCharge = models.CharField(max_length = 50)   #一日貸し料金
    def __str__(self):
        return self.mrName

class Facility(models.Model):
    fclName = models.CharField(max_length = 50) #付属設備名
    stock = models.CharField(max_length = 50)   #在庫数
    charge = models.CharField(max_length = 50)  #料金

    def __str__(self):
        return self.fclName


