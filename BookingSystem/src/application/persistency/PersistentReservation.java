package application.persistency;

import application.domain.Customer;
import application.domain.Reservation;
import application.domain.Table;
import application.util.Time;
import com.sun.istack.internal.NotNull;

import java.util.Date;

public class PersistentReservation extends Reservation {
  private int id;

  public PersistentReservation(int covers, Table table, Date date,Time time, @NotNull Customer customer) {
    super(covers, table, date, time, customer);
  }

  public int getId() {
    return id;
  }
}
