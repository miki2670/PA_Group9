package org.group9.Crypto;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Encrypt {
    public byte[] EncryptData(byte[] data) throws Exception {
        KeyGenerator keyGen = KeyGenerator.getInstance("AES");
        SecretKey secretKey = keyGen.generateKey();
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(Cipher.ENCRYPT_MODE, secretKey);
        return cipher.doFinal(data);
    }

    public void EncryptData(String fileName) throws Exception {
        try {
            StringBuilder stringBuilder = new StringBuilder();
            File myObj = new File(fileName);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                stringBuilder.append(data);
            }
            myReader.close();
            var data = stringBuilder.toString().getBytes();
            KeyGenerator keyGen = KeyGenerator.getInstance("AES");
            SecretKey secretKey = keyGen.generateKey();
            Cipher cipher = Cipher.getInstance("AES");
            cipher.init(Cipher.ENCRYPT_MODE, secretKey);
            myObj = new File("encrypted.txt");
            if (myObj.createNewFile()) {
                try (FileOutputStream stream = new FileOutputStream("./src/test/encrypted.txt")) {
                    stream.write(cipher.doFinal(data));
                }
                System.out.println("File created: " + myObj.getName());
            } else {
                System.out.println("File already exists.");
            }
        } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}
