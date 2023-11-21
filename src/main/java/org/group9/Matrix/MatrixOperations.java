package org.group9.Matrix;

import java.math.BigInteger;
import java.util.stream.IntStream;

public class MatrixOperations {
    public double[][] Multiply(double[][] firstMatrix, double[][] secondMatrix) {
        double[][] result = new double[firstMatrix.length][secondMatrix[0].length];

        for (int row = 0; row < result.length; row++) {
            for (int col = 0; col < result[row].length; col++) {
                double cell = 0;
                for (int i = 0; i < secondMatrix.length; i++) {
                    cell += firstMatrix[row][i] * secondMatrix[i][col];
                }
                result[row][col] = cell;
            }
        }

        return result;
    }

    public double[][] RightRotate(double[][] matrix) {
        double[][] result = new double[matrix[0].length][matrix.length];

        int m = matrix.length;
        int n = matrix[0].length;
        IntStream.range(0, m).forEach(i ->
                IntStream.range(0, n).forEach(j -> {
                    result[j][m - 1 - i] = matrix[i][j];
                }));
        return result;
    }

    public double Determinant(double[][] matrix){
        double res;
        int n = matrix.length;

        if (n == 1)
        {
            res = matrix[0][0];
        }
        else if (n == 2)
        {
            res = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1];
        }
        else{
            res=0;
            for (int i=0; i < n; i++){
                double[][] m = new double[n-1][];
                for (int j=0; j < (n-1); j++) {
                    m[j] = new double[n-1];
                }

                for (int j=1; j < n; j++){
                    int j1=0;
                    for (int k=0; k<n; k++){
                        if(k == j1)
                            continue;
                        m[j-1][j1] = matrix[j][k];
                        j1++;
                    }
                }
                res += Math.pow(-1.0, 1.0+i+1.0) * matrix[0][i] * Determinant(m);
            }
        }
        return res;
    }
}
