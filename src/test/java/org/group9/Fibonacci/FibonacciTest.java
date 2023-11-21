package org.group9.Fibonacci;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

import static org.junit.jupiter.api.Assertions.assertEquals;


class FibonacciTest {

    @Test
    void calculateFibonacci() {
        assertEquals(1134903170, new Fibonacci().calculateFibonacci(45));
    }
}
