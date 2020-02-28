from django.db import models

class Recurt(models.Model):
    name = models.CharField('Имя', max_length=30)
    planet = models.CharField('Планета',null=True, max_length=40)
    age = models.IntegerField('Возраст' ,null=True)
    email = models.EmailField('Почта',null=True)
    question1 = models.IntegerField("Ответ на первый вопрос 1 или 2 или 3", null=True)
    question2 = models.IntegerField("Ответ на второй вопрос 1 или 2 или 3", null=True)
    question3 = models.IntegerField("Ответ на третий вопрос 1 или 2 или 3", null=True)

class Sith(models.Model):
    sith_name = models.CharField("Имя Ситха" ,null=True, max_length=30)
    planet_learn = models.CharField("Планета на которой обучает", null=True, max_length=30)

class Task(models.Model):
    title = models.TextField('Вопрос', max_length=256)
    answer = models.CharField('Ответ #1',max_length=128, blank=True)
    answer1 = models.CharField('Ответ #2', max_length=128, blank=True)
    answer2 = models.CharField('Ответ #3', max_length=128, blank=True)

class Form (models.Model):
    recurt = models.ForeignKey(Recurt, on_delete=models.CASCADE, related_name='recurt')
    def __str__(self):
        return self.recurt

    def publish(self):
        self.save()

class Form_Sith (models.Model):
    sith = models.ForeignKey(Sith, on_delete=models.CASCADE, related_name='sith')
    def __str__(self):
        return self.sith

    def publish(self):
        self.save()

class Task_Form(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task')

    def __str__(self):
        return self.task

    def publish(self):
        self.save()

class ShadowHand(models.Model):
    name = models.CharField('Имя рекуртера', max_length=30)
    email = models.EmailField('Почта рекуртера', null=True)

class ShadowHand_Form(models.Model):
    hand = models.ForeignKey(ShadowHand, on_delete=models.CASCADE, related_name='hand')

    def __str__(self):
        return self.hand

    def publish(self):
        self.save()