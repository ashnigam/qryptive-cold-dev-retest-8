import java.security.*;
class Example { Object key() throws Exception { return KeyPairGenerator.getInstance("RSA").generateKeyPair(); } }
