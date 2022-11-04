import java.util.*;
import java.io.*;
import java.math.*;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/
class Solution {

    public static void main(String args[]) {
        String dice="123456"; // test1
        String commands = "DLU";
       /*  Scanner in = new Scanner(System.in);
        for (int i = 0; i < 3; i++) {
            String line = in.nextLine(); // One line out of three in the string describing the starting position.
            dice = dice + line;
        }
        String commands = in.nextLine(); // The sequence of ULDR-characters describing the steps to perform.
*/
        System.err.println(dice);
        System.err.println(commands);
        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");
        String[] dArr = null;
        dArr = dice.split("");
        String[] commandsArr = null;
        commandsArr = commands.split("");
        for (int i = 0; i < commandsArr.length;i++){
            if (commandsArr[i].equals("U")){
                String t = dArr[0];dArr[0]=dArr[4];
                dArr[4]=dArr[5];dArr[5]=dArr[2];dArr[2]=t;
            } else if (commandsArr[i].equals("D")){
                String t = dArr[0];dArr[0]=dArr[4];dArr[4]=t;
                t = dArr[1];dArr[1]=dArr[3];dArr[3]=t;
                t = dArr[2];dArr[2]=dArr[5];dArr[5]=t;
            } else if (commandsArr[i].equals("L")){
                String t = dArr[0];dArr[0]=dArr[4];dArr[4]=dArr[3];
                dArr[3]=t;
                t=dArr[1];dArr[1]=dArr[5];
                dArr[5]=dArr[2];dArr[2]=t;
            } else {
                String t = dArr[0];dArr[0]=dArr[4];dArr[4]=dArr[1];
                dArr[1]=t;
                t=dArr[2];dArr[2]=dArr[3];
                dArr[3]=dArr[5];dArr[5]=t;
            }
        }


        // The number on the side you end up on after having performed `commands`.
        System.out.println(dArr[2]);
    }
}