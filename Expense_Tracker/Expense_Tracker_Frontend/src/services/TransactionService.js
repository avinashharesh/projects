import axios from 'axios'

const EMPLOYEE_BASE_REST_API_URL = 'http://localhost:8081/api/v1/';

class TransactionService
{
    getTransactions()
    {
        return axios.get(EMPLOYEE_BASE_REST_API_URL)
    }

    getTransactionbyid(transactionId)
    {
        return axios.get(EMPLOYEE_BASE_REST_API_URL+ 'gettransaction/'+transactionId)
    }

    createTransaction(transaction)
    {
        return axios.post(EMPLOYEE_BASE_REST_API_URL+'createTransaction',transaction)
    }

    updateTransaction(transactionId,transaction)
    {
        return axios.put(EMPLOYEE_BASE_REST_API_URL+'updatetransaction/'+transactionId,transaction)
    }

    deleteTransaction(transactionId)
    {
        return axios.delete(EMPLOYEE_BASE_REST_API_URL+'deleteTransaction/'+transactionId)
    }
}

export default new TransactionService