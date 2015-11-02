package board;

import java.util.Hashtable;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Board: used to show tha status of board, and find the best move of AI or MAN
 */
public class Board {
  public static final int NONE = 0;
  public static final int AI = 1;
  public static final int MAN = -1;
  private int[][] record;

  private final int searchDeep = 100;   // the deep of the search tree

  // use to reocrd some boards used to start game or get better serach result
  Hashtable<int[][], Integer> aiTable;
  Hashtable<int[][], Integer> ManTable;

  /**
   * Initialize board to empty
   */
  public Board() {
    record = new int[3][3];

    for (int i = 0; i < record.length; ++ i) {
      for (int j = 0; j < record[i].length; ++j) {
        record[i][j] = NONE;
      }
    }
  }

  public int getSearchDeep() {
    return searchDeep;
  }

  public void setRecord(int i, int j, int side) {
    record[i][j] = side;
  }

  public int[][] getRecord() {
    return record;
  }


  /**
   * Judge if side can move in board
   * @param side the side, AI or MAN
   * @return if side cam move
   */
  private boolean CanMove(int side) {
    boolean can_move = false;
    boolean no_others = true;
    int other = -side;

    for (int i = 0; i < 3; ++ i) {
      no_others = true;
      for (int j = 0; j < 3; ++j) {
        if (record[i][j] == other) {
          no_others = false;
          break;
        }
      }
      if (no_others) {
        can_move = true;
        break;
      }
    }

    for (int j = 0; !can_move && j < 3; ++ j) {
      no_others = true;
      for (int i = 0; i < 3; ++ i) {
        if (record[i][j] == other) {
          no_others = false;
          break;
        }
      }
      if (no_others) {
        can_move = true;
        break;
      }
    }

    no_others = true;
    for (int i = 0; !can_move && i < 3; ++ i) {
      if (record[i][i] == other) {
        no_others = false;
        break;
      }
    }
    if (no_others)
      can_move = true;

    no_others = true;
    for (int i = 0; !can_move && i < 3; ++ i)
      if (record[i][2-i] == other) {
        no_others = false;
        break;
      }
    return can_move;
  }

  /**
   * Judge if side can win
   * @param side the side, AI or MAN
   * @return if side can win
   */
  public boolean IsWin(int side) {
    boolean isWin = false;

    for (int i = 0; !isWin && i < 3; ++ i) {
      if ((record[i][0] + record[i][1] + record[i][2]) / 3 == side)
        isWin = true;
    }
    for (int j = 0; !isWin && j < 3; ++ j) {
      if ((record[0][j] + record[1][j] + record[2][j]) / 3 == side)
        isWin = true;
    }
    if (!isWin && ((record[0][0] + record[1][1] + record[2][2]) / 3) == side)
      isWin = true;
    if (!isWin && ((record[0][2] + record[1][1] + record[2][0]) / 3) == side)
      isWin = true;

    return isWin;
  }

  /**
   * eval the grade of the board
   * @return the grade of the board
   */
  private int Eval() {
    int value = 0;
    int[][] tmpRecord = new int[3][3];

    // dose someone win?
    //if (IsWin(AI))  return Integer.MIN_VALUE - 10;
    //if (IsWin(MAN)) return Integer.MIN_VALUE + 10;

    for (int i = 0; i < 3; ++ i)
      for (int j = 0; j < 3; ++ j) {
        if (record[i][j] == NONE)
          tmpRecord[i][j] = AI;
        else
          tmpRecord[i][j] = record[i][j];
      }
    for (int i = 0; i < 3; ++ i)
      value += ((tmpRecord[i][0] + tmpRecord[i][1] + tmpRecord[i][2]) / 3 == AI) ? 1 : 0;
    for (int j = 0; j < 3; ++ j)
      value += ((tmpRecord[0][j] + tmpRecord[1][j] + tmpRecord[2][j]) / 3 == AI) ? 1 : 0;
    value += ((tmpRecord[0][0] + tmpRecord[1][1] + tmpRecord[2][2]) / 3 == AI) ? 1 : 0;
    value += ((tmpRecord[2][0] + tmpRecord[1][1] + tmpRecord[0][2]) / 3 == AI) ? 1 : 0;

    // if there is a AI in the middle of two MAN, + 5
      /*
      for (int i = 0; i < 3; ++ i) {
          if (tmpRecord[i][0] == MAN && tmpRecord[i][2] == MAN && tmpRecord[i][1] == AI)
              value += 2;
      }
      for (int j = 0; j < 3; ++ j) {
          if (tmpRecord[0][j] == MAN && tmpRecord[2][j] == MAN && tmpRecord[1][j] == AI)
              value += 2;
      }

      if (tmpRecord[0][0] == MAN && tmpRecord[2][2] == MAN && tmpRecord[1][1] == AI)
          value += 3;
      if (tmpRecord[0][2] == MAN && tmpRecord[2][0] == MAN && tmpRecord[1][1] == AI)
          value += 3;
      */

    // other side
    for (int i = 0; i < 3; ++ i)
      for (int j = 0; j < 3; ++ j) {
        if (record[i][j] == NONE)
          tmpRecord[i][j] = MAN;
        else
          tmpRecord[i][j] = record[i][j];
      }
    for (int i = 0; i < 3; ++ i)
      value += ((tmpRecord[i][0] + tmpRecord[i][1] + tmpRecord[i][2]) / 3 == MAN) ? -1 : 0;
    for (int j = 0; j < 3; ++ j)
      value += ((tmpRecord[0][j] + tmpRecord[1][j] + tmpRecord[2][j]) / 3 == MAN) ? -1 : 0;
    value += ((tmpRecord[0][0] + tmpRecord[1][1] + tmpRecord[2][2]) / 3 == MAN) ? -1 : 0;
    value += ((tmpRecord[2][0] + tmpRecord[1][1] + tmpRecord[0][2]) / 3 == MAN) ? -1 : 0;

    for (int i = 0; i < 3; ++ i) {
      if (tmpRecord[i][0] == AI && tmpRecord[i][2] == AI && tmpRecord[i][1] == MAN)
        value += -2;
    }
    for (int j = 0; j < 3; ++ j) {
      if (tmpRecord[0][j] == AI && tmpRecord[2][j] == AI && tmpRecord[1][j] == MAN)
        value += -2;
    }

    if (tmpRecord[0][0] == AI && tmpRecord[2][2] == AI && tmpRecord[1][1] == MAN)
      value += -3;
    if (tmpRecord[0][2] == AI && tmpRecord[2][0] == AI && tmpRecord[1][1] == MAN)
      value += -3;

    return value;
  }

  /**
   * Find the best move of Ai
   * @param deep the deep to search
   * @param bestMove the best move which will be change in function
   * @param value the best move of child tree
   */
  private void AIMove(int deep, AtomicInteger bestMove, AtomicInteger value) {
    AtomicInteger response = new AtomicInteger(0);
    AtomicInteger noCare = new AtomicInteger(0);

    if (deep == 0)
      value.set(Eval());
    else if (!CanMove(AI) && !CanMove(MAN))
      value.set(Eval());
    else if (IsWin(AI))
      value.set(Eval());
    else if (IsWin(MAN))
      value.set(Eval());
    else {
      value.set(Integer.MIN_VALUE);
      for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
          if (record[i][j] == NONE) {
            record[i][j] = AI;
            ManMove(deep - 1, noCare, response);
            record[i][j] = NONE;

            if (response.get() > value.get()) {
              value.set(response.get());
              bestMove.set(3 * i + j);
            }
          }
        }
      }
    }
  }

  /**
   * Find the best move of MAN
   * @param deep the depth to search
   * @param bestMove the best move
   * @param value the value of child search tree
   */
  private void ManMove(int deep, AtomicInteger bestMove, AtomicInteger value)
  {
    AtomicInteger response = new AtomicInteger(0);
    AtomicInteger noCare = new AtomicInteger(0);

    if (deep == 0)
      value.set(Eval());
    else if (!CanMove(AI) && !CanMove(MAN))
      value.set(Eval());
    else if (IsWin(MAN))
      value.set(Eval());
    else if (IsWin(AI))
      value.set(Eval());
    else {
      value.set(Integer.MAX_VALUE);
      for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
          if (record[i][j] == NONE) {
            record[i][j] = MAN;
            AIMove(deep - 1, noCare, response);
            record[i][j] = NONE;

            if (response.get() < value.get()) {
              value.set(response.get());
              bestMove.set(3 * i + j);
            }
          }
        }
      }
    }
  }

  public void AIToMove() {
    AtomicInteger manBestMove = new AtomicInteger(0);
    AtomicInteger manValue = new AtomicInteger(0);
    ManMove(getSearchDeep(), manBestMove, manValue);
    record[manBestMove.get() / 3][manBestMove.get() % 3] = AI;
  }

  // unit test for board
  public static void main(String[] args) {
    int count = 0;
    Board board = new Board();

    while ((!board.IsWin(AI) && !board.IsWin(MAN))
            && (board.CanMove(AI) || board.CanMove(MAN))) {
      System.out.println(count++ + ": ");
      PrintBoard(board);
      if (board.CanMove(MAN) || board.CanMove(AI)) {
        AtomicInteger aiBestMove = new AtomicInteger(0);
        AtomicInteger aiValue = new AtomicInteger(0);
        board.AIMove(board.getSearchDeep(), aiBestMove, aiValue);
        board.record[aiBestMove.get() / 3][aiBestMove.get() % 3] = AI;
      }

      System.out.println(count++ + ": ");
      PrintBoard(board);
      if (board.CanMove(MAN) || board.CanMove(AI)) {
        AtomicInteger manBestMove = new AtomicInteger(0);
        AtomicInteger manValue = new AtomicInteger(0);
        board.ManMove(board.getSearchDeep(), manBestMove, manValue);
        board.record[manBestMove.get() / 3][manBestMove.get() % 3] = MAN;
      }
    }

    System.out.println("\n\nend: ");
    PrintBoard(board);
  }

  /**
   * Print the status of the board
   * @param board board to print
   */
  private static void PrintBoard(Board board) {
    for (int i = 0; i < 3; ++ i) {
      for (int j = 0; j < 3; ++ j) {
        if (board.record[i][j] == AI)
          System.out.printf("%4s", "A");
        else if (board.record[i][j] == MAN)
          System.out.printf("%4s", "M");
        else
          System.out.printf("%4s", "0");
      }
      System.out.println();
    }
  }
}