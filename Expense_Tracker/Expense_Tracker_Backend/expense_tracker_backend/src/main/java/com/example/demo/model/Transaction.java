package com.example.demo.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.Id;

@Entity
public class Transaction {
	
	@Id
	@GeneratedValue()
	private long id;
	private long amount;
	private String description;
	private String type_of_transaction;
	public Transaction()
	{
		
	}
	@Override
	public String toString() {
		return "Transaction [id=" + id + ", amount=" + amount + ", description=" + description
				+ ", type_of_transaction=" + type_of_transaction + "]";
	}
	public Transaction(long amount, String description, String type_of_transaction) {
		super();
		this.amount = amount;
		this.description = description;
		this.type_of_transaction = type_of_transaction;
	}
	public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}
	public long getAmount() {
		return amount;
	}
	public void setAmount(long amount) {
		this.amount = amount;
	}
	public String getDescription() {
		return description;
	}
	public void setDescription(String description) {
		this.description = description;
	}
	public String getType_of_transaction() {
		return type_of_transaction;
	}
	public void setType_of_transaction(String type_of_transaction) {
		this.type_of_transaction = type_of_transaction;
	}
	
	

}
