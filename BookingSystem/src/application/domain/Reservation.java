package application.domain;

import application.domain.Booking;
import application.domain.Customer;

import application.util.Time;
import com.sun.istack.internal.NotNull;

import java.util.Date;

public class Reservation extends Booking {
  Time arrivalTime;
  Customer customer;  // the customer who books the reservation

  public Reservation(int covers, Table table, Date date,Time time, @NotNull Customer customer) {
    super(covers, table, date, time);
    this.arrivalTime = null;
    this.customer = customer;
  }

  public void setArrivalTime(Time time) {
    this.arrivalTime = time;
  }
}
