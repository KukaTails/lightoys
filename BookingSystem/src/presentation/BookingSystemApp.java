package presentation;

import javax.swing.JFrame;

public class BookingSystemApp extends JFrame {
  public BookingSystemApp() {
    add(new StaffUI());
    setSize(600, 400);
  }
}
