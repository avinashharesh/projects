package net.javaguides.ems.service;

import java.util.List;
import java.util.Random;

import org.springframework.beans.factory.annotation.Autowired;

import net.javaguides.ems.model.Employee;
import net.javaguides.ems.repository.EmployeeRepository;

public class EmployeeService {
	
	@Autowired
	private EmployeeRepository employeerepository;
	
	public List<Employee> getEmployees()
	{
		return employeerepository.findAll();
	}
	
	public Employee getEmployeeByID(Long id)
	{
		return employeerepository.findById(id).get();
	}
	
	public Employee createEmployee(Employee employee)
	{
		long generatedLong = new Random().nextLong();
		employee.setId(generatedLong);
		return employeerepository.save(employee);
	}
	
	public Employee updateEmployee(Employee y)
	{
		Employee x=employeerepository.findById(y.getId()).get();
		x.setEmailId(y.getEmailId());
		x.setFirstName(y.getFirstName());
		x.setLastName(y.getLastName());
		return employeerepository.save(x);
	}
	
	public String deleteEmployee(Long id)
	{
		employeerepository.deleteById(id);
		return id+" Employee is deleted";
	}

}
