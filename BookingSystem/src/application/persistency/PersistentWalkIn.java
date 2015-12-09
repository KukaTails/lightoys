package application.persistency;

import application.domain.Table;
import application.domain.WalkIn;
import application.util.Time;

import java.util.Date;

public class PersistentWalkIn extends WalkIn {
  private int id;

  public PersistentWalkIn(int covers, Table table, Date date, Time time) {
    super(covers, table, date, time);
  }

  public int getId() {
    return id;
  }
}
