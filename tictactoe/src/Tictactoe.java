import tictactoecomponent.TictactoeFrame;

import java.awt.EventQueue;
import javax.swing.JFrame;
import javax.swing.ImageIcon;

/**
 * Main window of game
 */
public class Tictactoe {

  public static void main(String[] args) {
    EventQueue.invokeLater(()->{
      JFrame gameFrame = new TictactoeFrame();

      gameFrame.setTitle("Tic-tac-toe");
      gameFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
      gameFrame.setIconImage(new ImageIcon("icon.png").getImage());
      gameFrame.setVisible(true);
    });
  }
}