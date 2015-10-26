import TictactoeComponent.TictactoeFrame;

import java.awt.*;
import javax.swing.*;

/**
 * Created by Keen on 2015/10/23.
 */
public class Tictactoe {
    public static void main(String[] args)
    {
        EventQueue.invokeLater(new Runnable() {
            @Override
            public void run() {
                JFrame gameFrame = new TictactoeFrame();

                gameFrame.setTitle("Tic-tac-toe");
                gameFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                gameFrame.setIconImage(new ImageIcon("icon.png").getImage());
                gameFrame.setVisible(true);
            }
        });
    }
}
