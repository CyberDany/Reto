from django.db import models
from django.core.validators import MinValueValidator
from .sources.matrix_helper import MatrixHelper
from django.db import IntegrityError

# Create your models here.
class Asteroid(models.Model):
    width = models.IntegerField(validators=[MinValueValidator(1)])
    height = models.IntegerField(validators=[MinValueValidator(1)])
    matrix = models.CharField(max_length=2048)

    def check_exists(self):
        '''
            Checks if the Asteroid exists in the Database
        '''
        try:
            return Asteroid.objects.get(width=self.width,
                                        height=self.height,
                                        matrix=self.matrix)
        except Asteroid.DoesNotExist:
            return None


    def get_list_representation(self):
        '''
            Gets the matrix of the Asteroid in list format
        '''
        list = []
        for idx_row in range(self.height):
            row = []
            for idx_col in range(self.width):
                row.append(self.matrix[idx_row*self.width+idx_col])
            list.append(row)
        return list


class Observation(models.Model):
    date = models.DateField()
    time = models.TimeField()
    observatory_code = models.CharField(max_length=64)
    device_code = models.CharField(max_length=64)
    width = models.IntegerField(validators=[MinValueValidator(1)])
    height = models.IntegerField(validators=[MinValueValidator(1)])
    device_matrix = models.CharField(max_length=2048)
    asteroid = models.ForeignKey(Asteroid, on_delete=models.CASCADE)
    class Meta:
        unique_together = ["date", "time", "observatory_code", "device_code"]
    
    def process_and_save(self):
        '''
            This function creates the observed Asteroid in it, 
            checks its existance, if it does not exist, 
            the new Asteroid is saved in the database,
            finally it also saves the Observation in the database
        '''
        matrix = MatrixHelper.get_observed_object(self.width, self.height, self.device_matrix)
        
        new_asteroid = Asteroid(width=int(matrix['width']),
                                height=int(matrix['height']), 
                                matrix=matrix['string'])

        found_asteroid = new_asteroid.check_exists()

        if (found_asteroid is None):
            new_asteroid.save()
            self.asteroid = new_asteroid
        else:
            self.asteroid = found_asteroid

        try:
            self.save()
        except IntegrityError:
            pass