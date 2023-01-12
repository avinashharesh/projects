package com.example.demo.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.model.Transaction;
import com.example.demo.repository.TransactionRepository;

@Service
public class TransactionService {
	
	@Autowired
	private TransactionRepository repository;
	
	public List<Transaction> getTransactions()
	{
		return repository.findAll();
	}
	
	public Transaction getTransactionbyid(Long id)
	{
		return repository.findById(id).get();
	}
	
	public Transaction createTransaction(Transaction transaction)
	{
		return repository.save(transaction);
	}
	
	public Transaction updateTransaction(Long id, Transaction new_transaction)
	{
		Transaction old_transaction=repository.findById(id).get();
		old_transaction.setAmount(new_transaction.getAmount());
		old_transaction.setDescription(new_transaction.getDescription());
		old_transaction.setType_of_transaction(new_transaction.getDescription());
		return repository.save(old_transaction);
	}
	
	public String deleteTransaction(Long id)
	{
		repository.deleteById(id);
		return "Trasaction "+id+" deleted";
	}

}
