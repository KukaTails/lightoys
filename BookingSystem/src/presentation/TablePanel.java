package presentation;

import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.SwingConstants;
import java.awt.GridLayout;

public class TablePanel extends JPanel {
  boolean selected = false;
  private JLabel idLabel;
  private JLabel informationLabel;
  private JButton selectedButton;

  TablePanel(int id) {
    idLabel = new JLabel(Integer.toString(id), SwingConstants.CENTER);
    informationLabel = new JLabel("No information", SwingConstants.CENTER);
    selectedButton = new JButton("Not selected");

    setLayout(new GridLayout(3, 1));
    add(idLabel);
    add(informationLabel);
    add(selectedButton);
  }

  public void setId(int idNo) {
    idLabel.setText(Integer.toString(idNo));
  }

  public void setInfo(String info) {
    informationLabel.setText(info);
  }
}
