package application.domain;

import application.domain.Booking;

import java.util.Date;

public class WalkIn extends Booking {
  public WalkIn(int covers, Date date) {
    super(covers, date);
  }
}
