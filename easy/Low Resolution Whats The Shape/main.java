import java.util.*;
import java.io.*;
import java.math.*;

class Solution {

    
    public static void main(String args[]) {
        ArrayList<String> mapList = new ArrayList<String>();
        Scanner in = new Scanner(System.in);
        int W = in.nextInt();
        int H = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        for (int i = 0; i < H; i++) {
            String row = in.nextLine();
            mapList.add(i, row);
        }
        System.err.println(mapList);
        // Write an answer using System.out.println()
        // To debug: System.err.println("Debug messages...");

        ArrayList<Long> yList = new ArrayList<>();
        ArrayList<Integer> xList = new ArrayList<>();
        for (int j = 0; j < W; j++){
            xList.add(0);
        }
        boolean recElli = false;
        for (int i = 0; i < mapList.size();i++ ){
            String row = mapList.get(i);
            if (row.contains("/")){
                recElli = true;
            }
            long count = row.chars().filter(ch -> ch == '.').count();
            yList.add(i,count);
            for (int j = 0; j < row.length();j++){
                if (row.substring(j,j+1).equals(".")){
                    int wert = xList.get(j);
                    xList.set(j, wert+1);
                }                                 
            }
        }
        System.err.println(yList);
        System.err.println(xList);

        if (yList.get(0) == yList.get(yList.size()-1)){
            if (yList.get(0) == yList.get((yList.size()/2))){
                if (recElli){
                    System.out.println("Ellipse");
                } else {
                    System.out.println("Rectangle");
                }
            } else {
                if (xList.get(0) == xList.get(xList.size()-1)){
                    System.out.println("Ellipse");
                } else {
                    System.out.println("Triangle");
                }

            }            
        } else {
            System.out.println("Triangle");
        }
    }
}