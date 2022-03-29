package org.mysqltutorial;
import java.util.*;  

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.CallableStatement;

/**
 *
 * @author mysqltutorial.org
 */
public class Main {

    /**
     * Get skills by candidate id
     *
     * @param candidateId
     */
    public static void getSkills(int candidateId) {
        // 
        String query = "{ call get_candidate_skill(?) }";
        ResultSet rs;

        try (Connection conn = MySQLJDBCUtil.getConnection();
                CallableStatement stmt = conn.prepareCall(query)) {

            stmt.setInt(1, candidateId);

            rs = stmt.executeQuery();
            while (rs.next()) {
                System.out.println(String.format("%s - %s",
                        rs.getString("first_name") + " "
                        + rs.getString("last_name"),
                        rs.getString("skill")));
            }
        } catch (SQLException ex) {
            System.out.println(ex.getMessage());
        }
    }

    /**
     *
     * @param args
     */
    public static void main(String[] args) {
        getSkills(122);
    }
}