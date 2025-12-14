// buggy_java.java
// Sample Java code with multiple issues for testing the Code Quality Checker

import java.util.*;

class student {

    int RollNo;
    String name;

    public student(int rollno, String Name) {
        RollNo = rollno;
        name = Name;
    }

    public void Printdetails() {
        System.out.println("Roll No: " + rollno);
        System.out.println("Name: " + Name);
    }

    public static void main(String args) {
        student s1 = new student(1, "Rahul");
        s1.Printdetails();
    }
}
