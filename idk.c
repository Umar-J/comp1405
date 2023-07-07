char payload[10000];  // Assuming a maximum payload length of 1000 characters
    Transaction transactions = NULL;
    int numberOfTransactions = 0;

    message[strcspn(message,"\n)")] = '\0';//remove trailing newline character
    char* messageCopy = strdup(message); //makes copy of the message, cuz the strtok inserts null terminators
    char* token = strtok(messageCopy, "|");

    while (token != NULL) {
        transactions = (Transaction)realloc(transactions, (numberOfTransactions +1) * sizeof(Transaction));
        transactions[numberOfTransactions] = (Transaction)malloc(sizeof(Transaction));

        sscanf(token, "T%10[^,],C%8[^,],%lf", transactions[numberOfTransactions]->transactionID, transactions[numberOfTransactions]->customerID, &(transactions[numberOfTransactions]->amount));

        numberOfTransactions++;
        token = strtok(NULL, "|");
    }

    free(messageCopy);
