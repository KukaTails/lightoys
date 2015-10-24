package TictactoeComponent;

import java.awt.*;
import javax.swing.*;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

/**
 * Created by Keen on 2015/10/23.
 */
public class BackgroundPanel extends JPanel {
    private final int ADD_HEIGHT = 30;
    private final int ADD_WIDTH = 30;
    private final int DISTANCE = 200;

    private final int WIN_WIDTH = 100;
    private final int WIN_HEIGHT = 100;

    private final int FAIL_WIDTH = 50;
    private final int FAIL_HEIGHT = 100;

    private Image background;
    private Image man_piece;
    private Image ai_piece;
    private Image game_win;
    private Image game_fail;

    Board board;
    boolean manToMove = true;
    boolean isWin = false;
    boolean isFail = false;

    public BackgroundPanel()
    {
        board = new Board();

        // initialize background
        addMouseListener(new MouseHandler());

        // get image sources
        try {
            background = ImageIO.read(new File("board.png"));
            man_piece = ImageIO.read(new File("piece_man.png"));
            ai_piece = ImageIO.read(new File("piece_ai.png"));
            game_win = ImageIO.read(new File("game_win.png"));
            game_fail = ImageIO.read(new File("game_over.png"));
        } catch (IOException e) {
            System.out.println("load image fail in background");
        }
    }

    @Override
    public void paintComponent(Graphics g)
    {
        g.drawImage(background, 0, 0, this);
        paintPieces(g);
    }

    public void paintPieces(Graphics g)
    {
        int[][] record = board.getRecord();

        for (int i = 0; i < record.length; ++ i) {
            for (int j = 0; j < record[i].length; ++ j) {
                int draw_choice = record[i][j];

                if (draw_choice == Board.AI)
                    g.drawImage(ai_piece,  ADD_WIDTH + j * DISTANCE, ADD_HEIGHT + i * DISTANCE, this);
                else if (draw_choice == Board.MAN)
                    g.drawImage(man_piece, ADD_WIDTH + j * DISTANCE, ADD_HEIGHT + i * DISTANCE, this);
            }
        }

        if (isWin)
            PaintWinPicture(g);
        if (isFail)
            PaintFailPicture(g);
    }

    private class MouseHandler extends MouseAdapter {
        @Override
        public void mouseClicked(MouseEvent event)
        {
            int[][] record = board.getRecord();
            int x = event.getX() - ADD_WIDTH;
            int y = event.getY() - ADD_HEIGHT;
            int i = y / DISTANCE;
            int j = x / DISTANCE;

            if (!isWin && !isFail && record[i][j] == Board.NONE) {
                board.setRecord(i, j, board.MAN);
                repaint();

                if (board.IsWin(Board.MAN))
                    isWin = true;
                else {
                    board.AIToMove();
                    if (board.IsWin(Board.AI))
                        isFail = true;
                }
            }
            repaint();
        }
    }

    public void PaintWinPicture(Graphics g)
    {
        g.drawImage(game_win, WIN_WIDTH, WIN_HEIGHT, this);
    }

    public void PaintFailPicture(Graphics g)
    {
        g.drawImage(game_fail, FAIL_WIDTH, FAIL_HEIGHT, this);
    }
}