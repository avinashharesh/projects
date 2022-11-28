package com.javaguides.ems.controller;

import java.util.List;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.javaguides.ems.model.Employee;
import com.javaguides.ems.service.EmployeeService;

@RestController
@RequestMapping("/api/v1/")
public class EmployeeController {
	
	@Autowired
	private EmployeeService employeeservice;
	
	@PostMapping("/employees")
	public Employee createEmployee(@RequestBody Employee employee)
	{
		return employeeservice.createEmployee(employee);
	}
	
	@GetMapping("/employees")
	public List<Employee> getEmployees()
	{
		return employeeservice.getEmployees();
	}
	
	@GetMapping("/employees/{id}")
	public Employee getEmployeeByID(@PathVariable Long id)
	{
		return employeeservice.getEmployeeByID(id);
	}
	
	@PutMapping("/employees/{id}")
	public Employee updateEmployee(@PathVariable Long id,@RequestBody Employee new_employee)
	{
		return employeeservice.updateEmployee(id, new_employee);
	}
	
	@DeleteMapping("/employees/{id}")
	public String deleteEmployee(@PathVariable Long id)
	{
		return employeeservice.deleteEmployee(id);
	}
	
	

}
