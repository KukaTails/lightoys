package presentation;

import javax.swing.JPanel;
import java.awt.GridLayout;

public class StaffUI extends JPanel {
  static final int TABLES_NUMBER = 16;
  private TablePanel[] tablePanels;

  StaffUI() {
    setLayout(new GridLayout(4, 4));

    tablePanels = new TablePanel[TABLES_NUMBER];
    for (int i = 0; i < TABLES_NUMBER; ++ i) {
      tablePanels[i] = new TablePanel(i);
      add(tablePanels[i]);
    }
  }
}
