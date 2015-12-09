package application.domain;

import application.domain.Booking;
import application.util.Time;
import javafx.scene.control.Tab;

import java.util.Date;

public class WalkIn extends Booking {
  public WalkIn(int covers, Table table, Date date, Time time) {
    super(covers, table, date, time);
  }
}
