from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    # 新增圖片欄位，圖片會上傳到 media/products/ 資料夾
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name