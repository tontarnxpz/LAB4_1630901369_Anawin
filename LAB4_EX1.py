class cylinder():
    radius = 5
    height = 10
    def calculate(self):
        self.result = 3.14 * (self.radius*self.radius) * self.height
        return self.result

result_cylinder = cylinder()
print("First cylinders =",str(result_cylinder.calculate()))

result_cylinder.radius = 7
result_cylinder.height = 13
print("First cylinders =",str(result_cylinder.calculate()))