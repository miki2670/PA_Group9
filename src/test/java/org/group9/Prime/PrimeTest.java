package org.group9.Prime;

import org.junit.jupiter.api.Test;

import java.math.BigInteger;

import static org.junit.jupiter.api.Assertions.*;

class PrimeTest {

    @Test
    void isPrime() {
        BigInteger n = new BigInteger("433494437");
        var result = new Prime().IsPrime(n);
        assertTrue(result);
    }
}