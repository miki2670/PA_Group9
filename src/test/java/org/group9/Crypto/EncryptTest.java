package org.group9.Crypto;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class EncryptTest {

    @Test
    void encryptData() throws Exception {
        var simulatedFile = """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras a dolor mollis, interdum tortor imperdiet, dignissim libero. Praesent id mattis metus. In vitae dapibus sem. Aliquam ante enim, porta at tincidunt eget, gravida ac nisl. Suspendisse hendrerit sagittis ultricies. Donec tristique urna vehicula tellus pharetra, non consequat lectus elementum. Vivamus congue magna massa, at tristique erat blandit in. Nulla vel mattis sapien. Sed vitae consequat dui, vel interdum ex. Fusce eu ex quis lorem aliquet dictum. Curabitur rhoncus semper ipsum, et faucibus tortor feugiat posuere.                 
                Praesent efficitur, elit in vehicula pharetra, sapien enim posuere sem, id blandit purus ipsum vitae nulla. Praesent fermentum gravida luctus. Nam dictum nunc sapien, vitae euismod mauris imperdiet semper. Curabitur ipsum turpis, tempus eget finibus vel, tincidunt auctor ipsum. Mauris lectus lacus, convallis id lacus eget, iaculis sodales sem. In arcu eros, volutpat at nibh sit amet, lacinia ultricies neque. Vestibulum non purus sit amet ipsum eleifend tempor vitae eget velit. Donec eget convallis ante. Duis ultricies mattis quam, vel feugiat massa aliquet eu. Morbi elementum cursus odio, ac feugiat ipsum vulputate nec. Vivamus pulvinar ornare enim. Suspendisse potenti. Nullam a urna quis purus imperdiet ultricies.           
                Nunc ac aliquam neque, ac mollis risus. Sed sed est at ipsum egestas placerat. Suspendisse vulputate erat in neque dictum dignissim. Pellentesque id ligula eget ante molestie porttitor laoreet id mi. Proin non mi augue. Nulla facilisi. Mauris consectetur tempor augue, quis commodo risus efficitur consequat. Duis semper ac nisi viverra vestibulum. Phasellus id congue libero, at gravida tortor.          
                Quisque ligula elit, dignissim ac ipsum a, faucibus posuere augue. Nunc eget orci quam. Curabitur hendrerit commodo enim et tempus. Aenean tincidunt tortor eget quam porta, eu ornare nulla aliquam. Proin vel fringilla orci. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Pellentesque mollis eget nisi sed auctor. Cras non mi luctus, placerat nisi vel, molestie nulla. Nam pretium vel justo ac consectetur. Morbi imperdiet dignissim urna nec porttitor. Nunc mi ipsum, tincidunt ut pharetra nec, consectetur a dui. Donec accumsan aliquam magna, quis egestas orci blandit in.             
                Morbi euismod, lorem at tincidunt gravida, felis metus aliquet metus, in finibus velit felis eu tellus. Maecenas a quam nec velit molestie sollicitudin et eget sem. Sed vel odio consectetur, ultrices sapien ac, mollis velit. In ultrices consequat eleifend. Morbi quis massa et elit vulputate gravida. In eu erat non turpis condimentum hendrerit sed id urna. Nunc eu elit ullamcorper, pretium quam nec, porttitor augue. Nam nisi mauris, commodo nec fermentum id, venenatis at ipsum. Morbi ut volutpat turpis.
                """;
        assertDoesNotThrow(() -> new Encrypt().EncryptData(simulatedFile.getBytes()));
    }

    @Test
    void encryptDataFile() {
        assertDoesNotThrow(() -> new Encrypt().EncryptData("./src/test/test.txt"));
    }
}