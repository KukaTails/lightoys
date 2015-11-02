package tictactoecomponent;

import board.Board;

import java.io.File;
import java.io.IOException;
import java.awt.Image;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

import javax.swing.JPanel;
import javax.imageio.ImageIO;

/**
 * The Panel of game, which will paint the board
 * and picture to show whether man win or lose
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
  private Image manPiece;
  private Image aiPiece;
  private Image gameWin;
  private Image gameFail;

  Board board;
  boolean manToMove = true;
  boolean isWin = false;
  boolean isFail = false;

  public BackgroundPanel() {
    board = new Board();
    addMouseListener(new MouseHandler());

    try {
      background = ImageIO.read(new File("board.png"));
      manPiece = ImageIO.read(new File("piece_man.png"));
      aiPiece = ImageIO.read(new File("piece_ai.png"));
      gameWin = ImageIO.read(new File("game_win.png"));
      gameFail = ImageIO.read(new File("game_over.png"));
    } catch(IOException e) {
      System.out.println("load image fail in background");
    }
  }

  @Override
  public void paintComponent(Graphics g) {
    g.drawImage(background, 0, 0, this);
    paintPieces(g);
  }

  public void paintPieces(Graphics g) {
    int[][] record = board.getRecord();

    for (int i = 0; i < record.length; ++i) {
      for (int j = 0; j < record[i].length; ++j) {
        int draw_choice = record[i][j];

        if (draw_choice == Board.AI)
          g.drawImage(aiPiece, ADD_WIDTH + j * DISTANCE, ADD_HEIGHT + i * DISTANCE, this);
        else if (draw_choice == Board.MAN)
          g.drawImage(manPiece, ADD_WIDTH + j * DISTANCE, ADD_HEIGHT + i * DISTANCE, this);
      }
    }
    if (isWin) {
      PaintWinPicture(g);
    }else if (isFail) {
      PaintFailPicture(g);
    }
  }

  private class MouseHandler extends MouseAdapter {
    @Override
    public void mouseClicked(MouseEvent event) {
      int[][] record = board.getRecord();
      int x = event.getX() - ADD_WIDTH;
      int y = event.getY() - ADD_HEIGHT;
      int i = y / DISTANCE;
      int j = x / DISTANCE;

      if (!isWin && !isFail && record[i][j] == Board.NONE) {
        board.setRecord(i, j, board.MAN);
        repaint();

        if (board.IsWin(Board.MAN)) {
          isWin = true;
        } else {
          board.AIToMove();
          if (board.IsWin(Board.AI))
            isFail = true;
        }
      }
      repaint();
    }
  }

  public void PaintWinPicture(Graphics g) {
    g.drawImage(gameWin, WIN_WIDTH, WIN_HEIGHT, this);
  }

  public void PaintFailPicture(Graphics g) {
    g.drawImage(gameFail, FAIL_WIDTH, FAIL_HEIGHT, this);
  }
}
