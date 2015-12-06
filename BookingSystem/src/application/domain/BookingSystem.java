package application.domain;

import java.util.Date;
import java.util.Vector;

public class BookingSystem {
  private final static int NOT_SELECTED = 0;
  private final static int SELECTED = 1;

  private Date date;
  private int state = NOT_SELECTED;
  private Vector<Booking> current;
  private Vector<Booking> selected;
  private Restaurant restaurant;

  private static BookingSystem uniqueInstance;

  public static BookingSystem getInstance() {
    if (uniqueInstance == null) {
      uniqueInstance = new BookingSystem();
    }
    return uniqueInstance;
  }

  private BookingSystem() {
  }

  public void dispaly() {

  }

  public void cancel() {

  }

  public Reservation makeReservation() {
    return null;
  }

  public void recordArrival() {

  }

  public void selectBooking() {

  }

  void updateDisplay() {

  }
}