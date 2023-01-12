package com.example.demo.controller;

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

import com.example.demo.model.Transaction;
import com.example.demo.service.TransactionService;

@RestController
@RequestMapping("/api/v1/")
public class TransactionController {
	
	@Autowired
	private TransactionService service;
	
	@GetMapping("/")
	public List<Transaction> getTransactions()
	{
		return service.getTransactions();
	}
	
	@GetMapping("/gettransaction/{id}")
	public Transaction getTransactionbyid(Long id)
	{
		return service.getTransactionbyid(id);
	}
	
	@PostMapping("/createtransaction")
	public Transaction createTransaction(@RequestBody Transaction transaction)
	{
		return service.createTransaction(transaction);
	}
	
	@PutMapping("/updatetransaction/{id}")
	public Transaction updateTransaction(@PathVariable Long id,@RequestBody Transaction new_transaction)
	{
		return service.updateTransaction(id, new_transaction);
	}
	
	@DeleteMapping("/deletetransaction/{id}")
	public String deleteTransaction(@PathVariable Long id)
	{
		return service.deleteTransaction(id);
	}
	
	

}
