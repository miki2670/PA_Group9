package org.group9.Extend;

public class Rectangle extends Shape {
    protected final double x;
    protected final double y;

    public Rectangle(double x, double y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public double width() {
        return x;
    }

    @Override
    public double height() {
        return y;
    }

    @Override
    public double area() {
        return x * y;
    }

    @Override
    public double circumference() {
        return 2 * x + 2 * y;
    }
}

