package org.group9.Prime;

import java.math.BigInteger;

public class Prime {
    public boolean IsPrime(BigInteger n) {
        BigInteger p = new BigInteger("2");
        while (p.compareTo(n) < 0) {
            if (n.mod(p).compareTo(BigInteger.ZERO) == 0) {
                return false;
            }
            p = p.add(new BigInteger("1"));
        }
        return true;
    }
}
