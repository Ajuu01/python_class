from django.db import models 

class calculator_history(models.Model):
    number_a=models.FloatField()
    number_b=models.FloatField()
    operation=models.CharField( max_length=10)
    operation_status=models.CharField(max_length=10)
    result=models.TextField()

    created_at=models.DateTimeField( 
        # auto_now=True,# update timestamp capture
        auto_now_add=True#creation timestamp capture
        )
    updated_at=models.DateTimeField( 
        auto_now=True,# update timestamp capture
        # auto_now_add=True,#creation timestamp capture
        )
    
    class Meta:
        db_table="calculator_history"
    
    def __str__(self):
        return self.result