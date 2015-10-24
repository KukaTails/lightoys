package TictactoeComponent;

import javax.swing.*;

/**
 * Created by Keen on 2015/10/23.
 */
public class TictactoeFrame extends JFrame {
    private final int DEFAULT_WIDTH = 615;
    private final int DEFAULT_HEIGHT = 640;

    public TictactoeFrame()
    {
        add(new BackgroundPanel());
        setSize(DEFAULT_WIDTH, DEFAULT_HEIGHT);
    }
}
