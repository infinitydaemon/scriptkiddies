import java.io.*;
import java.net.*;

public class SocketLogger {
    public static void main(String[] args) throws IOException {
        int portNumber = 12345;
        ServerSocket serverSocket = new ServerSocket(portNumber);
        System.out.println("Listening on port " + portNumber);
        
        try (
            Socket clientSocket = serverSocket.accept();
            PrintWriter out = new PrintWriter(new FileWriter("log.txt", true));
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        ) {
            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                out.println(inputLine);
            }
            System.out.println("Data logged to file");
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
