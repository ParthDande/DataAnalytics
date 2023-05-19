public class Employee {
	String name;
	private double salary;
	Employee(String name1 ){
		name = name1;
	}
	void emp_name(String empName) 
	{
		empName = name;
	}
	void set_salary(double emp_salary) {
		salary = emp_salary;
	}
	void print() {
		System.out.println(name);
		System.out.println(salary);
	}
public static void main(String[] args) {
	Employee emp1 = new Employee("parth");
	emp1.set_salary(10000);
	emp1.print();
    Employee emp2 = new Employee("Raj");
    emp2.set_salary(20000);
    emp2.print();
}
}
