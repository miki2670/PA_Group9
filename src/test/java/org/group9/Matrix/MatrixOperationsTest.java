package org.group9.Matrix;

import org.junit.jupiter.api.Test;

import java.math.BigInteger;

import static org.junit.jupiter.api.Assertions.*;

class MatrixOperationsTest {

    @Test
    void multiply() {

        double[][] m1 = { {10.4, 25.2, 1.2, 35.1, 2.33}, {1, 2, 4.8, 8.7, 5}, {7, 26, 4.01, 6.11, 0.11}, {0.3, 3.22, 6.1, 9.5, 22.22} };
        double[][] m2 = { {7, 86.7, 6.5, 1.1}, {2.2, 3.3, 4.4, 5.5}, {1, 25.2, 5.2, 1.1}, {3.2, 1.2, 3.4, 4.4} };
        double[][] expected = { {241.76, 1057.2, 304.06000000000006, 305.8}, {44.04, 224.7, 69.84, 55.66}, {129.762, 801.084, 201.526, 181.995}, {45.684000000000005, 201.756, 80.138, 66.55000000000001} };
        var result = new MatrixOperations().Multiply(m1, m2);
        assertArrayEquals(expected, result);
    }

    @Test
    void rightRotate() {
        double[][] m = { {10.4, 25.2, 1.2, 35.1, 2.33}, {1, 2, 4.8, 8.7, 5}, {7, 26, 4.01, 6.11, 0.11}, {0.3, 3.22, 6.1, 9.5, 22.22} };
        var result = new MatrixOperations().RightRotate(m);
    }

    @Test
    void determinant() {
        double[][] m = { {7, 86.7, 6.5, 1.1}, {2.2, 3.3, 4.4, 5.5}, {1, 25.2, 5.2, 1.1}, {3.2, 1.2, 3.4, 4.4} };
        var result = new MatrixOperations().Determinant(m);
        assertEquals(-6257.248800000001, result);
    }
}