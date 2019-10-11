"""
Coursework Assignment 1
CSC061
2019/20.
"""

                             #~User input~#

# Prompts user to input gross salary and tax code
employeeGross = input("Enter Employee's Gross Salary: ")
employeeTaxCode = input("Enter Employee's 4-digit Tax Code: ").upper()

                            #~Calculations~#
class Employee():
    """This class takes the user input and performs all the necessary
    calculations upon initialisation. The results of these
    calculations are then stored as <self.properties> in the object after
    initialisation. They can then easily be used in further calculations
    or outputs"""
    def __init__(self, gross, taxCode):
        self.gross = float(gross)
        self.taxCode = taxCode
        
        # Employee pension contribution of 5%:
        self.pensionEmployee = self.gross * 0.05
        
        # Employer pension contribution of 7.5%:
        self.pensionEmployer = self.gross * 0.075
        
        # Total pension contribution:
        self.pensionTotal = self.pensionEmployee + self.pensionEmployer
        
        # Employee's gross salary after pension contribution:
        self.grossMinusPension = self.gross - self.pensionEmployee
        
        # Employee's personal tax allowance:
        self.allowance = self.calcAllowance()
        
        # Taxable income
        self.taxableIncome = self.calcTaxableIncome()
        
        # Tax deducted
        self.taxArray = self.calcTax()
        self.lowerTax = self.taxArray[0]
        self.upperTax = self.taxArray[1]
        self.totalTax = self.lowerTax + self.upperTax
        
        # Net salary
        self.netSalary = self.grossMinusPension - self.totalTax

    def calcAllowance(self):
        # Takes the tax code and calculates personal allowance
        string = self.taxCode
        number = int(string[:3]) * 10
        letter = string[-1:]
        if letter == "Z":
            number = number + 1000
        return number

    def calcTaxableIncome(self):
        # First establishes whether or not there is any taxable income,
        # and then returns the calculated value
        if self.allowance >= self.grossMinusPension:
            return 0
        else:
            return (self.grossMinusPension - self.allowance)

    def calcTax(self):
        # Returns array: [0] = lower tax paid, [1] = higher tax paid
        lowerBand = 40000
        if self.taxableIncome == 0: # Returns 0 upper and lower tax if no taxable income 
            return [0, 0]   
        elif self.taxableIncome <= lowerBand:
            return [(self.taxableIncome * 0.09), 0]
        else:
            upperBand = (self.taxableIncome - lowerBand) * 0.49
            return [(lowerBand * 0.09), upperBand]

# Initialisation of Employee class to calculations user inputs
employee = Employee(employeeGross, employeeTaxCode)


                                #~Output~#

# Variable used in the print statements to format the table
border = "-" * 79                                    # Solid border
breakLine = "- " * int((78/2)) + "-"                 # Dashed border
allignmentF = "| {0:<55s}|{1:>18.2f}{2:>3s}\n{3}"    # Alignment for floats
allignmentS= "| {0:<55s}|{1:>18s}{2:>3s}\n{3}"       # Alignment for strings

# Print statements
print(border + "\n" + allignmentF
      .format("Gross Salary:",
              employee.gross, "|",
              breakLine))

print(allignmentS
      .format("Tax Code:",
              employeeTaxCode, "|",
              border))

print(allignmentF
      .format("Employee Pension Contribution:",
              employee.pensionEmployee, "|",
              breakLine))

print(allignmentF
      .format("Employer Pension Contribution:",
              employee.pensionEmployer, "|",
              breakLine))

print(allignmentF
      .format("Total Pension Contribution:",
              employee.pensionTotal, "|",
              breakLine))

print(allignmentF
      .format("Gross Salary after pension contribution:",
              employee.grossMinusPension, "|",
              border))

print(allignmentF
      .format("Personal Tax Allowance:",
              employee.allowance, "|",
              border))

print(allignmentF
      .format("Taxable Income:",
              employee.taxableIncome, "|",
              breakLine))

print(allignmentF
      .format("Lower Tax Paid:",
              employee.lowerTax, "|",
              breakLine))

print(allignmentF
      .format("Upper Tax Paid:",
              employee.upperTax, "|",
              breakLine))

print(allignmentF
      .format("Total Tax Paid:",
              employee.totalTax, "|",
              border))

print(allignmentF
      .format("Net Income:",
              employee.netSalary, "|",
              border))

