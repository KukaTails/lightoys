package application.persistency;

import application.domain.Customer;

public class PersistentCustomer extends Customer {
  private int Id;

  public int getCustomerId() {
    return Id;
  }
}
