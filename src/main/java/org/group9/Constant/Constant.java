package org.group9.Constant;

import java.util.Random;

public class Constant {
    public static final int constant = 163;

    public int getConstant() {
        return constant;
    }

    public int noConstant() {
        return new Random().nextInt(0, Integer.MAX_VALUE);
    }
}
