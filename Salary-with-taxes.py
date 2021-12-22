salarybyhour = float(input("How much you earn by hour?: "))
workhours = int(input("How much hours have you worked this month?: "))

grosssalary = salarybyhour*workhours
inss = grosssalary*0.08
sindicate = grosssalary*0.05
anualtax = grosssalary*0.11
liquidsalary =  grosssalary-(inss+sindicate+anualtax)



print('+ Salário Bruto : R${}'.format(grosssalary))
print('- IR (11%) : R${}'.format(anualtax))
print('- INSS (8%) : R${}'.format(inss))
print('- Sindicato ( 5%) : R${}'.format(sindicate))
print('= Salário Liquido : R${}'.format(liquidsalary))