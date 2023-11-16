package org.group9.Extend;

public class Square extends Rectangle {
    @SuppressWarnings("SuspiciousNameCombination")
    public Square(double x) {
        super(x, x);
    }

    @Override
    public double height() {
        return width();
    }

    @Override
    public double area() {
        return x * x;
    }

    @Override
    public double circumference() {
        return 4 * x;
    }
}
