package org.mysqltutorial;
import java.sql.*;
import java.util.*;

/**
 *
 * @author mysqltutorial.org
 */
class Main {


    private static DatabaseMetaData MySQLJDBCUtil;

    public static void callIt(int customerId) {
        // 
        String query = "{ call myPrecuder(?) }";
        ResultSet rs;

        try (Connection conn = MySQLJDBCUtil.getConnection();
                CallableStatement stmt = conn.prepareCall(query)) {

            stmt.setInt(1, customerId);

            rs = stmt.executeQuery();
            while (rs.next()) {
                System.out.println(String.format("%s - %s",
                        rs.getString("OrderID") + " "
                        + rs.getString("Profit/Loss"),
                        rs.getString("Amount")));
            }
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
        }
    }


    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.print("Enter id of the costumer: ");
        int id= sc.nextInt();
        callIt(id);
    }
}