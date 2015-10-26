package TictactoeComponent;

import java.util.Hashtable;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Board: record the pieces of the board
 * Created by Keen on 2015/10/23.
 */
public class Board {
    public static final int NONE = 0;
    public static final int AI = 1;
    public static final int MAN = -1;

    private int[][] record;
    // the deep of the search tree
    private final int searchDeep = 100;

    // use to reocrd some boards used to start game
    // or get better serach result
    Hashtable<int[][], Integer> aiTable;
    Hashtable<int[][], Integer> ManTable;

    public Board()
    {
        record = new int[3][3];

        // initialize board to empty
        for (int i = 0; i < record.length; ++ i)
            for (int j = 0; j < record[i].length; ++ j)
                record[i][j] = NONE;
    }

    public int getSearchDeep()
    {
        return searchDeep;
    }

    public int[][] getRecord()
    {
        return record;
    }

    public void setRecord(int i, int j, int side)
    {
        record[i][j] = side;
    }

    // used for unit test
    private static void PrintBoard(Board board)
    {
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

    // Judge if AI or Man can move
    private boolean CanMove(int side)
    {
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

    public boolean IsWin(int side)
    {
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

    private int Eval()
    {
        int value = 0;
        int[][] tmp_record = new int[3][3];

        // dose someone win?
       //if (IsWin(AI))  return Integer.MIN_VALUE - 10;
       //if (IsWin(MAN)) return Integer.MIN_VALUE + 10;

        for (int i = 0; i < 3; ++ i)
            for (int j = 0; j < 3; ++ j) {
                if (record[i][j] == NONE)
                    tmp_record[i][j] = AI;
                else
                    tmp_record[i][j] = record[i][j];
            }
        for (int i = 0; i < 3; ++ i)
            value += ((tmp_record[i][0] + tmp_record[i][1] + tmp_record[i][2]) / 3 == AI) ? 1 : 0;
        for (int j = 0; j < 3; ++ j)
            value += ((tmp_record[0][j] + tmp_record[1][j] + tmp_record[2][j]) / 3 == AI) ? 1 : 0;
        value += ((tmp_record[0][0] + tmp_record[1][1] + tmp_record[2][2]) / 3 == AI) ? 1 : 0;
        value += ((tmp_record[2][0] + tmp_record[1][1] + tmp_record[0][2]) / 3 == AI) ? 1 : 0;

        // if there is a AI in the middle of two MAN, + 5
        /*
        for (int i = 0; i < 3; ++ i) {
            if (tmp_record[i][0] == MAN && tmp_record[i][2] == MAN && tmp_record[i][1] == AI)
                value += 2;
        }
        for (int j = 0; j < 3; ++ j) {
            if (tmp_record[0][j] == MAN && tmp_record[2][j] == MAN && tmp_record[1][j] == AI)
                value += 2;
        }

        if (tmp_record[0][0] == MAN && tmp_record[2][2] == MAN && tmp_record[1][1] == AI)
            value += 3;
        if (tmp_record[0][2] == MAN && tmp_record[2][0] == MAN && tmp_record[1][1] == AI)
            value += 3;
        */

        // other side
        for (int i = 0; i < 3; ++ i)
            for (int j = 0; j < 3; ++ j) {
                if (record[i][j] == NONE)
                    tmp_record[i][j] = MAN;
                else
                    tmp_record[i][j] = record[i][j];
            }
        for (int i = 0; i < 3; ++ i)
            value += ((tmp_record[i][0] + tmp_record[i][1] + tmp_record[i][2]) / 3 == MAN) ? -1 : 0;
        for (int j = 0; j < 3; ++ j)
            value += ((tmp_record[0][j] + tmp_record[1][j] + tmp_record[2][j]) / 3 == MAN) ? -1 : 0;
        value += ((tmp_record[0][0] + tmp_record[1][1] + tmp_record[2][2]) / 3 == MAN) ? -1 : 0;
        value += ((tmp_record[2][0] + tmp_record[1][1] + tmp_record[0][2]) / 3 == MAN) ? -1 : 0;

        for (int i = 0; i < 3; ++ i) {
            if (tmp_record[i][0] == AI && tmp_record[i][2] == AI && tmp_record[i][1] == MAN)
                value += -2;
        }
        for (int j = 0; j < 3; ++ j) {
            if (tmp_record[0][j] == AI && tmp_record[2][j] == AI && tmp_record[1][j] == MAN)
                value += -2;
        }

        if (tmp_record[0][0] == AI && tmp_record[2][2] == AI && tmp_record[1][1] == MAN)
            value += -3;
        if (tmp_record[0][2] == AI && tmp_record[2][0] == AI && tmp_record[1][1] == MAN)
            value += -3;

        return value;
    }

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

    public void AIToMove()
    {
        AtomicInteger manBestMove = new AtomicInteger(0);
        AtomicInteger manValue = new AtomicInteger(0);
        ManMove(getSearchDeep(), manBestMove, manValue);
        record[manBestMove.get() / 3][manBestMove.get() % 3] = AI;
    }


    // unit test for board
    public static void main(String[] args)
    {
        int count = 0;
        Board board = new Board();

        int value = board.Eval();

        while ((!board.IsWin(board.AI) && !board.IsWin(board.MAN))
                && (board.CanMove(board.AI) || board.CanMove(board.MAN))) {
            if (count == 5) {
                int a = 0;
            }
            System.out.println(count++ + ": ");
            PrintBoard(board);
            if (board.CanMove(MAN) || board.CanMove(AI)) {
                AtomicInteger aiBestMove = new AtomicInteger(0);
                AtomicInteger aiValue = new AtomicInteger(0);
                board.AIMove(board.getSearchDeep(), aiBestMove, aiValue);
                board.record[aiBestMove.get() / 3][aiBestMove.get() % 3] = AI;
            }

            if (count == 5) {
                int a = 0;
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
}
