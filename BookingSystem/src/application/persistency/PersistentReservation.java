package application.persistency;

import application.domain.Reservation;

public class PersistentReservation extends Reservation {
  private int id;

  public PersistentReservation() {
    super();
  }

  public int getId() {
    return id;
  }
}
