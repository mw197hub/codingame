// https://www.codingame.com/ide/puzzle/calculator

import java.util.*;
import java.io.*;
import java.math.*;

class Solution {

    public static void main(String args[]) {
        Scanner in = new Scanner(System.in);
        
        //ArrayList<String> keyList = new ArrayList<>(Arrays.asList("2", "5", "+","6","-","7","="));
        //ArrayList<String> keyList = new ArrayList<>(Arrays.asList("9", "3", "x","1","2","/","5","="));
        //ArrayList<String> keyList = new ArrayList<>(Arrays.asList("2", "1", "x","3","-","/","9","="));
       // ArrayList<String> keyList = new ArrayList<>(Arrays.asList("8", "x", "3","+","2","=","=","=","2","7","9","/","9","-","4","=","=","="));
        ArrayList<String> keyList = new ArrayList<>(Arrays.asList("7", "9", "x","-","7","+","AC","8","/","3","+","5","=","8","2","5","7","-","5","4","=","=","+","1","2","="));


  /*      int n = in.nextInt();
        if (in.hasNextLine()) {
            in.nextLine();
        }
        for (int i = 0; i < n; i++) {
            String key = in.nextLine();
            keyList.add(key);
        }
    */    
        String erg = "";String zeichen ="";double summe = 0.0;String out="";String vorWert="";
        for (int i = 0; i < keyList.size(); i++) {
            String wert = keyList.get(i);
            if (wert.equals("AC")){
                erg="";summe=0.0;zeichen="";
                out = String.valueOf(summe);
            } else if (wert.equals("=")){
                summe = berechnen(summe,zeichen,erg);
                out = String.valueOf(summe);

            } else if (wert.equals("+")|| wert.equals("-")|| wert.equals("x")|| wert.equals("/") ){
                
                if (zeichen.length() == 0){
                    summe = Double.parseDouble(erg);erg="";
                } else if (erg.length() > 0){
                    if (vorWert.equals("=")) {
                        erg="";
                    } else {
                    summe = berechnen(summe,zeichen,erg);erg="";
                    out = String.valueOf(summe);                    
                    }
                }
                zeichen = wert;  
            } else {
                if (vorWert.equals("=")){
                    erg="";zeichen="";
                }
                if (zeichen.length() == 0){                    
                    erg = erg + wert;
                    out = String.valueOf(erg);
                } else {
                    erg = erg + wert;
                    out = String.valueOf(erg);
                }
            }
            // Write an answer using System.out.println()
            // To debug: System.err.println("Debug messages...");
            if (out.endsWith(".0")){                
                out = out.substring(0, out.length()-2);
            }
            vorWert = wert;
            System.out.println(out);
        }
    }

    static private double berechnen(Double summe,String zeichen, String erg){
        Double zahl = Double.valueOf(erg);
        if (zeichen.equals("+")){
            return summe + zahl;
        } else if (zeichen.equals("-")){
            return summe - zahl;            
        } else if (zeichen.equals("x")){
            return summe * zahl;
        } else {
            Long w = Math.round((summe * 1000) / zahl);
            return Double.valueOf(w) / 1000;
        }

    }
}