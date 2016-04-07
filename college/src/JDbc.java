import java.sql.*;

/**
 * Created by Keen on 2015/11/2.
 */
public class JDbc {
  public static void main(String[] args) {
    JDBCexample("", "");
  }

  public static void JDBCexample(String userid, String passwd) {
    try {
      String url = "jdbc:mysql://localhost:3306/college?user=root&password=heweidong0977461203";

      Class.forName("com.mysql.jdbc.Driver");
      Connection connection = DriverManager.getConnection(url);
      Statement stmt = connection.createStatement();

      try {
        stmt.executeUpdate("insert into instructor values('7798', 'Kim', 'Physics', 98000)");
      } catch(SQLException sqlError) {
        System.out.println("Could not insert tuple: " + sqlError);
      }

      ResultSet resultSet = stmt.executeQuery(
              "select dept_name, avg(salary) " +
              "from instructor " +
              "group by dept_name");
      while (resultSet.next()) {
        System.out.println(resultSet.getString("dept_name") + " " +
                resultSet.getFloat(2));
      }
      stmt.close();
      connection.close();
    } catch(Exception sqlError) {
      System.out.println("Exception: " + sqlError);
    }
  }
}
