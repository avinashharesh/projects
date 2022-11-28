package com.javaguides.ems.service;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.javaguides.ems.exception.ResourceNotFoundException;
import com.javaguides.ems.model.Employee;
import com.javaguides.ems.repository.EmployeeRepository;

@Service
public class EmployeeService {
	
	@Autowired
	private EmployeeRepository employeerepository;
	
	public List<Employee> getEmployees()
	{
		return employeerepository.findAll();
	}
	
	public Employee getEmployeeByID(Long id)
	{
		return employeerepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("Emloyee "+id+" does not exits"));
		
	}
	
	public Employee createEmployee(Employee employee)
	{
		return employeerepository.save(employee);
	}
	
	public Employee updateEmployee(Long id,Employee new_employee)
	{
		if(!employeerepository.existsById(id))
		{
			throw new ResourceNotFoundException("Emloyee "+id+" does not exist");
		}
		
		Employee old_employee=employeerepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("Emloyee "+id+" does not exits"));
		old_employee.setFirstName(new_employee.getFirstName());
		old_employee.setLastName(new_employee.getLastName());
		old_employee.setEmailId(new_employee.getEmailId());
		return employeerepository.save(old_employee);
	}
	
	public String deleteEmployee(Long id)
	{
		if(!employeerepository.existsById(id))
		{
			throw new ResourceNotFoundException("Emloyee "+id+" does not exist");
		}
		
		employeerepository.deleteById(id);
		return "Employee "+id+"  deleted";
	}

}
