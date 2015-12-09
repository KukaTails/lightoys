import presentation.BookingSystemApp;

import javax.swing.JFrame;
import java.awt.EventQueue;

public class Main {
  public static void main(String[] args) {
    EventQueue.invokeLater(()->{
      JFrame bookingFrame = new BookingSystemApp();

      bookingFrame.setTitle("Booking System");
      bookingFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      bookingFrame.setVisible(true);
    });
  }
}
