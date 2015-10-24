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
                JFrame game_frame = new TictactoeFrame();

                //JFrame frame = new JFrame();

                //frame.add(new PiecesPanel());
                //frame.setVisible(true);
                game_frame.setTitle("Tic-tac-toe");
                game_frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                game_frame.setVisible(true);
            }
        });
    }
}
