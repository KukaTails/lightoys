package application.domain;

import application.util.Time;

import java.util.Date;

public abstract class Booking {
  protected int covers;
  protected Table table;
  protected Date date;
  protected Time time;

  protected Booking(int covers, Table table, Date date, Time time) {
    this.date = date;
    this.time = time;
    this.covers = covers;
    this.table = table;
  }

  public Date getDate() {
    return date;
  }

  public void setCovers(int covers) {
    this.covers = covers;
  }

  public void setArrivalTime(Date time) {
  }
}
